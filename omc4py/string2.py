from __future__ import annotations

import types
from collections.abc import Callable, Coroutine, Generator, Sequence
from contextlib import suppress
from dataclasses import dataclass
from functools import lru_cache, partial
from itertools import chain
from typing import (
    TYPE_CHECKING,
    Any,
    ClassVar,
    DefaultDict,
    Literal,
    Set,
    Tuple,
    Type,
    TypeVar,
    Union,
    get_args,
    get_origin,
    get_type_hints,
    overload,
)

from arpeggio import (
    EOF,
    Optional,
    ParserPython,
    PTNodeVisitor,
    RegExMatch,
    Terminal,
    ZeroOrMore,
    visit_parse_tree,
)
from modelicalang import v3_4

from .modelica import enumeration, record
from .openmodelica import Component, TypeName, VariableName
from .protocol import PathLike
from .string import unquote_modelica_string

if TYPE_CHECKING:
    from typing import _SpecialForm

    from arpeggio import _ParsingExpressionLike
    from typing_extensions import Never, ParamSpec, Self, TypeGuard

    T = TypeVar("T")
    P = ParamSpec("P")


_Primitive = Union[float, int, bool, str, TypeName, VariableName, Component]
_Defined = Union[record, enumeration, Tuple[Any, ...]]
_StringableType = Union[Type[Union[_Primitive, _Defined]], None]


def parse(typ: Any, s: str) -> Any:
    root_type = _get_type(typ)
    root_ndim = _get_ndim(typ)
    with _Syntax:
        parser = _Syntax.get_parser(
            root_type=root_type,  # type: ignore
            root_ndim=root_ndim,
        )
        visitor = _Visistor.get_visitor(
            root_type=root_type,  # type: ignore
            root_ndim=root_ndim,
        )
        return visit_parse_tree(parser.parse(s), visitor)


@dataclass
class _Syntax(v3_4.Syntax):
    root_type: _StringableType
    root_ndim: int

    def __post_init__(self) -> None:
        for t, n in _iter_all_types(self.root_type, self.root_ndim):
            if 0 < n:
                _runtime_method(self, _to_rule_name(t, ndim=n))(
                    partial(self.sequence_rule, t, n)
                )

    @classmethod
    @lru_cache
    def get_parser(
        cls, root_type: _StringableType, root_ndim: int
    ) -> ParserPython:
        return ParserPython(cls(root_type, root_ndim).root)

    def root(self) -> _ParsingExpressionLike:
        return (
            getattr(self, _to_rule_name(self.root_type, ndim=self.root_ndim)),
            EOF,
        )

    def sequence_rule(
        self, _type: _StringableType, _ndim: int
    ) -> _ParsingExpressionLike:
        return (
            "{",
            ZeroOrMore(
                getattr(self, _to_rule_name(_type, ndim=_ndim - 1)), sep=","
            ),
            "}",
        )

    # Dialects

    @classmethod
    def IDENT(cls) -> _ParsingExpressionLike:
        return [super().IDENT(), RegExMatch(r"\$\w*")]

    # Primitives

    @classmethod
    def none(cls) -> _ParsingExpressionLike:
        return ""

    @classmethod
    def real(cls) -> _ParsingExpressionLike:
        return Optional(cls.SIGN), cls.UNSIGNED_NUMBER

    @classmethod
    def integer(cls) -> _ParsingExpressionLike:
        return Optional(cls.SIGN), cls.UNSIGNED_INTEGER

    @classmethod
    def SIGN(cls) -> _ParsingExpressionLike:
        return RegExMatch(r"[+-]")

    @classmethod
    def boolean(cls) -> _ParsingExpressionLike:
        return [cls.TRUE, cls.FALSE]


if TYPE_CHECKING:

    class _Children(Sequence[Any]):
        SIGN: Literal["+", "-"]
        UNSIGNED_INTEGER: list[str]
        UNSIGNED_NUMBER: list[str]


class _Visistor(PTNodeVisitor):
    root_type: _StringableType
    root_ndim: int

    def __init__(
        self,
        *args: Any,
        root_type: _StringableType,
        root_ndim: int,
        **kwargs: Any,
    ) -> None:
        super().__init__(*args, **kwargs)
        self.root_type = root_type
        self.root_ndim = root_ndim

        for t, n in _iter_all_types(root_type, root_ndim):
            visit_method = f"visit_{_to_rule_name(t, ndim=n)}"
            if hasattr(self, visit_method):
                continue

            if 0 < n:
                _runtime_method(self, visit_method)(
                    partial(self._visit_sequence)
                )

    @classmethod
    @lru_cache
    def get_visitor(cls, root_type: _StringableType, root_ndim: int) -> Self:
        return cls(root_type=root_type, root_ndim=root_ndim)

    def _visit_sequence(self, _: Never, children: _Children) -> list[Any]:
        return list(children[::2])

    def visit_none(self, _1: Never, _2: Never) -> None:
        return

    def visit_none__1D(self, _1: Never, children: _Children) -> list[None]:
        return [None] * (len(children) + 1)

    def visit_real(self, _: Never, children: _Children) -> float:
        (value,) = map(float, children.UNSIGNED_NUMBER)
        if "-" in children.SIGN:
            value = -value

        return value

    def visit_integer(self, _: Never, children: _Children) -> int:
        (value,) = map(int, children.UNSIGNED_INTEGER)
        if "-" in children.SIGN:
            value = -value

        return value

    def visit_boolean(self, node: Terminal, _: Never) -> bool:
        return {
            "true": True,
            "false": False,
        }[node.value]

    def visit_STRING(self, node: Terminal, _: Never) -> str:
        return unquote_modelica_string(node.value)


@overload
def _to_rule_name(_type: _StringableType, /) -> str:
    ...


@overload
def _to_rule_name(_type: _StringableType, /, *, ndim: int) -> str:
    ...


@overload
def _to_rule_name(_type: _StringableType, /, *, attribute: str) -> str:
    ...


def _to_rule_name(
    _type: _StringableType,
    /,
    *,
    ndim: int | None = None,
    attribute: str | None = None,
) -> str:
    if _is_primitive(_type) or _type is None:
        stem = {
            float: "real",
            int: "integer",
            bool: "boolean",
            str: "STRING",
            TypeName: "typename",
            VariableName: "variablename",
            Component: "component",
            None: "none",
        }[_type]
    elif _is_defined(_type):
        stem = f"_{_type.__module__}.{_type.__name__}".lower().replace(
            ".", "__"
        )
    else:
        raise TypeError(_type)

    parts: list[str] = [stem]

    if ndim is not None and 0 < ndim:
        parts.append(f"{ndim}D")
    if attribute is not None:
        parts.append(attribute)

    return "__".join(parts)


def _runtime_method(
    self: Any, name: str
) -> Callable[[Callable[P, T]], Callable[P, T]]:
    def decorator(f: Callable[P, T]) -> Callable[P, T]:
        f.__name__ = name
        setattr(self, name, f)
        return f

    return decorator


def _iter_all_types(
    _type: _StringableType, ndim: int
) -> Generator[tuple[_StringableType, int], None, None]:
    result = DefaultDict[_StringableType, Set[int]](set)
    queue = [(_type, ndim)]
    while queue:
        t, n = queue.pop(0)
        if t not in result:
            for _, (tt, nn) in _iter_attribute_types(t):
                queue.append((tt, nn))
        result[t].add(n)

    for k, vs in result.items():
        for v in range(max(vs) + 1):
            yield k, v


def _iter_attribute_types(
    typ: _StringableType,
) -> Generator[tuple[str, tuple[_StringableType, int]], None, None]:
    if typ is None or _issubclass(typ, (TypeName, VariableName)):
        return
    for k, v in get_type_hints(typ).items():
        if _issubclass(get_origin(v), (ClassVar,)):
            continue
        yield k, (_get_type(v), _get_ndim(v))


def _get_type(obj: Any) -> _StringableType:
    types = set(_iter_types(obj))
    if types > {str}:
        types -= {str}
    if types > {None}:
        types -= {None}

    if len(types) == 1:
        (typ,) = types
        return typ

    raise TypeError(f"Types are ambigious or undefinable. got {types}")


def _iter_types(obj: Any) -> Generator[_StringableType, None, None]:
    for unpacked in _unpack(obj):
        if _is_none(unpacked):
            yield None
        elif _is_path_like(unpacked):
            yield str
        elif _is_primitive(unpacked) or _is_defined(unpacked):
            yield unpacked
        elif _is_sequence(unpacked):
            yield from _iter_types(get_args(unpacked)[0])


def _get_ndim(obj: Any) -> int:
    ndims = set(_iter_ndims(obj, ndim=0))

    if len(ndims) == 1:
        (ndim,) = ndims
        return ndim

    raise TypeError(f"Dimensions are ambigious or undefinable. got {ndims}")


def _iter_ndims(obj: Any, ndim: int) -> Generator[int, None, None]:
    for unpacked in _unpack(obj):
        if _is_sequence(unpacked):
            yield from _iter_ndims(get_args(unpacked)[0], ndim=ndim + 1)
        else:
            yield ndim


def _unpack(obj: Any) -> Generator[Any, None, None]:
    """
    Unpack Literal, Union and Coroutine

    match:
        case Literal[*args]:
            for arg in args:
                yield from _unpack(typ(arg))
        case Union[*args]:
            for arg in args:
                yield from _unpack(arg)
        case Coroutine[Any, Any, T]:
            yield from _unpack(T)
        case T:
            yield T
    """
    if _is_literal(obj):
        yield from chain.from_iterable(
            _unpack(type(arg)) for arg in get_args(obj)
        )
    elif _is_union(obj):
        yield from chain.from_iterable(_unpack(arg) for arg in get_args(obj))
    elif _is_coroutine(obj):
        yield from _unpack(get_args(obj)[2])
    else:
        yield obj


def _is_none(obj: Any) -> TypeGuard[None | type[None]]:
    return obj is None or _issubclass(obj, (type(None),))


def _is_literal(obj: Any) -> bool:
    return _issubclass(get_origin(obj), (Literal,))


def _is_union(obj: Any) -> bool:
    try:
        return _issubclass(get_origin(obj), (Union, types.UnionType))
    except AttributeError:
        return _issubclass(get_origin(obj), (Union,))


def _is_path_like(obj: Any) -> TypeGuard[type[PathLike[Any]]]:
    return _issubclass(get_origin(obj), (PathLike,)) or _issubclass(
        obj, (PathLike,)
    )


def _is_component(obj: Any) -> TypeGuard[type[Component]]:
    return _issubclass(obj, (Component,))


def _is_primitive(obj: Any) -> TypeGuard[type[_Primitive]]:
    return _issubclass(obj, _primitive_types())


@lru_cache
def _primitive_types() -> tuple[type[_Primitive], ...]:
    return tuple(get_args(_Primitive))


def _is_named_tuple(obj: Any) -> TypeGuard[type[tuple[Any, ...]]]:
    return (
        _issubclass(obj, (tuple,))
        and bool(get_type_hints(obj))
        and not _issubclass(obj, (Component,))
    )


def _is_defined(obj: Any) -> TypeGuard[type[_Defined]]:
    return _issubclass(obj, (record, enumeration)) or _is_named_tuple(obj)


def _is_sequence(obj: Any) -> TypeGuard[type[Sequence[Any]]]:
    return (
        _issubclass(get_origin(obj), (Sequence,))
        and not _is_component(obj)
        and not _is_named_tuple(obj)
    )


def _is_coroutine(obj: Any) -> TypeGuard[type[Coroutine[Any, Any, Any]]]:
    return _issubclass(get_origin(obj), (Coroutine,))


def _issubclass(
    obj: Any, class_: tuple[type[Any] | _SpecialForm, ...], /
) -> bool:
    if obj in class_:
        return True
    with suppress(TypeError):
        return isinstance(obj, type) and issubclass(
            obj, tuple(c for c in class_ if isinstance(c, type))
        )
    return False
