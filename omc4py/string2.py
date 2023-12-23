from __future__ import annotations

import types
from collections import ChainMap
from collections.abc import Callable, Coroutine, Generator, Mapping, Sequence
from contextlib import suppress
from dataclasses import dataclass
from enum import Enum
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
    NonTerminal,
    Optional,
    ParserPython,
    PTNodeVisitor,
    RegExMatch,
    StrMatch,
    Terminal,
    UnorderedGroup,
    ZeroOrMore,
    visit_parse_tree,
)
from exceptiongroup import ExceptionGroup
from modelicalang import v3_4

from .modelica import enumeration, record
from .openmodelica import (
    Component,
    TypeName,
    VariableName,
    _BaseTypeName,
    _BaseVariableName,
)
from .protocol import PathLike
from .string import quote_py_string, unquote_modelica_string

if TYPE_CHECKING:
    from typing import _SpecialForm

    from arpeggio import _ParsingExpressionLike
    from typing_extensions import Never, ParamSpec, Self, TypeGuard

    T = TypeVar("T")
    P = ParamSpec("P")


_Primitive = Union[float, int, bool, str, TypeName, VariableName, Component]
_Defined = Union[record, enumeration, Tuple[Any, ...]]
_StringableType = Union[Type[Union[_Primitive, _Defined]], None]


def unparse(typ: Any, obj: Any) -> str:
    return _unparse(_get_type(typ), _get_ndim(typ), (), obj)


def _unparse(
    t: _StringableType, n: int, attrs: tuple[str, ...], obj: Any
) -> str:
    try:
        if 0 < n:
            return _unparse_sequence(t, n, attrs, obj)
        elif obj is None:
            return ""
        elif t is None:
            return str(obj)
        elif issubclass(t, Component):
            return _unparse_component(t, n, attrs, obj)
        elif issubclass(t, tuple):
            return _unparse_tuple(t, n, attrs, obj)
        elif issubclass(t, record):
            return _unparse_record(t, n, attrs, obj)
        elif issubclass(t, enumeration):
            return _unparse_enumeration(t, n, attrs, obj)
        else:
            return _unparse_primitive(t, n, attrs, obj)
    except ExceptionGroup:
        raise
    except Exception as e:
        print(attrs)
        if not attrs:
            unparse_error = UnparseError("Can't unparse obj, obj={obj!r}")
        else:
            unparse_error = UnparseError(
                "Can't unparse "
                f"obj{''.join(attrs)}, obj{''.join(attrs[-1])}={obj}"
            )
        raise ExceptionGroup("Unparse failed", [unparse_error, e])


class UnparseError(ValueError):
    ...


def _unparse_sequence(
    t: _StringableType, n: int, attrs: tuple[str, ...], obj: Any
) -> str:
    assert 0 < n
    return (
        "{"
        + ",".join(
            _unparse(t, n - 1, attrs + (f"[{i}]",), obj[i])
            for i in range(len(obj))
        )
        + "}"
    )


def _unparse_component(
    t: _StringableType, n: int, attrs: tuple[str, ...], obj: Any
) -> str:
    assert n <= 0
    return (
        "{"
        + ",".join(
            _unparse(
                tt if attr != "dimensions" else None,
                nn,
                attrs + (f".{attr}",),
                getattr(obj, attr),
            )
            for attr, (tt, nn) in _iter_attribute_types(t)
        )
        + "}"
    )


def _unparse_tuple(
    t: _StringableType, n: int, attrs: tuple[str, ...], obj: Any
) -> str:
    assert n <= 0
    return (
        "("
        + ",".join(
            _unparse(tt, nn, attrs + (f"[{i}]",), obj[i])
            for i, (_, (tt, nn)) in enumerate(_iter_attribute_types(t))
        )
        + ")"
    )


def _unparse_record(
    t: type[record], n: int, attrs: tuple[str, ...], obj: Any
) -> str:
    assert n <= 0

    def items() -> Generator[str, None, None]:
        for attr, (tt, nn) in _iter_attribute_types(t):
            if isinstance(obj, Mapping):
                value = _unparse(tt, nn, attrs + (f"[{attr}!r]",), obj[attr])
            else:
                value = _unparse(
                    tt, nn, attrs + (f".{attr}",), getattr(obj, attr)
                )

            yield f"{attr}={value}"

    return (
        f"record {t.__omc_class__} "
        + ",".join(items())
        + f" end {t.__omc_class__};"
    )


def _unparse_enumeration(
    t: type[enumeration], n: int, attrs: tuple[str, ...], obj: Any
) -> str:
    assert n <= 0
    if isinstance(obj, Enum):
        name = obj.name
    elif isinstance(obj, int):
        name = t(obj).name
    else:
        name = str(obj)

    return f"{t.__omc_class__}.{name}"


def _unparse_primitive(
    t: type[float]
    | type[int]
    | type[bool]
    | type[str]
    | type[TypeName]
    | type[VariableName],
    n: int,
    attrs: tuple[str, ...],
    obj: Any,
) -> str:
    assert n <= 0
    if issubclass(t, str):
        if isinstance(obj, PathLike):
            obj = obj.__fspath__()
        return quote_py_string(str(obj))
    elif issubclass(t, bool):
        return "true" if obj else "false"
    else:
        return str(obj)


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
            method = _to_rule_name(t, ndim=n)
            if hasattr(self, method):
                continue

            if 0 < n:
                _runtime_method(self, method)(
                    partial(self.sequence_rule, t, n)
                )
            elif t is not None and issubclass(t, record):
                _runtime_method(self, method)(partial(self.record_rule, t))
                for attr, (tt, nn) in _iter_attribute_types(t):
                    _runtime_method(self, _to_rule_name(t, attribute=attr))(
                        partial(self.record_attr_rule, attr, tt, nn)
                    )
            elif t is not None and issubclass(t, enumeration):
                _runtime_method(self, method)(
                    partial(self.enumeration_rule, t)
                )
            elif t is not None and _is_named_tuple(t):
                _runtime_method(self, method)(
                    partial(self.named_tuple_rule, t)
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

    def record_rule(self, record_type: type[record]) -> _ParsingExpressionLike:
        name = StrMatch(f"{record_type.__omc_class__}")
        return (
            self.RECORD,
            name,
            UnorderedGroup(
                *(
                    getattr(self, _to_rule_name(record_type, attribute=attr))
                    for attr, _ in _iter_attribute_types(record_type)
                ),
                sep=",",
            ),
            self.END,
            name,
            ";",
        )

    def record_attr_rule(
        self, _attribute: str, _type: _StringableType, _ndim: int
    ) -> _ParsingExpressionLike:
        return (
            RegExMatch(f"_*{_attribute}_*", ignore_case=True),
            "=",
            getattr(self, _to_rule_name(_type, ndim=_ndim)),
        )

    def enumeration_rule(
        self, enumeration_type: type[enumeration]
    ) -> _ParsingExpressionLike:
        return (
            Optional("."),
            f"{enumeration_type.__omc_class__}.",
            [e.name for e in enumeration_type],
        )

    def named_tuple_rule(
        self, named_tuple_type: type[tuple[Any, ...]]
    ) -> _ParsingExpressionLike:
        elements = [
            getattr(self, _to_rule_name(t, ndim=n))
            for _, (t, n) in _iter_attribute_types(named_tuple_type)
        ]

        return (
            "(",
            *chain.from_iterable((element, ",") for element in elements[:-1]),
            elements[-1],
            ")",
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

    @classmethod
    def typename(cls) -> _ParsingExpressionLike:
        return cls.type_specifier

    @classmethod
    def variablename(cls) -> _ParsingExpressionLike:
        return cls.IDENT

    @classmethod
    def component(cls) -> _ParsingExpressionLike:
        return (
            "{",
            (
                *(cls.typename, ","),  # className
                *(cls.variablename, ","),  # name
                *(cls.STRING, ","),  # comment
                *(cls.STRING, ","),  # protected
                *(cls.boolean, ","),  # isFinal
                *(cls.boolean, ","),  # isFlow
                *(cls.boolean, ","),  # isStream
                *(cls.boolean, ","),  # isReplaceable
                *(cls.STRING, ","),  # variability
                *(cls.STRING, ","),  # innerOuter
                *(cls.STRING, ","),  # inputOutput
                cls.subscript_list,  # dimensions
            ),
            "}",
        )

    @classmethod
    def subscript_list(cls) -> _ParsingExpressionLike:
        return "{", ZeroOrMore(cls.subscript, sep=","), "}"


if TYPE_CHECKING:

    class _Children(Sequence[Any]):
        IDENT: list[str]
        SIGN: Literal["+", "-"]
        UNSIGNED_INTEGER: list[str]
        UNSIGNED_NUMBER: list[str]
        name: list[list[str]]


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
            method = f"visit_{_to_rule_name(t, ndim=n)}"
            if hasattr(self, method):
                continue

            if 0 < n:
                _runtime_method(self, method)(partial(self._visit_sequence))
            elif t is not None and issubclass(t, record):
                _runtime_method(self, method)(
                    partial(self._visit_record, record_type=t)
                )
                for attr, _ in _iter_attribute_types(t):
                    _runtime_method(
                        self, f"visit_{_to_rule_name(t, attribute=attr)}"
                    )(partial(self._visit_record_attr, attribute=attr))
            elif t is not None and issubclass(t, enumeration):
                _runtime_method(self, method)(
                    partial(self._visit_enumeration, enumeration_type=t)
                )
            elif t is not None and _is_named_tuple(t):
                _runtime_method(self, method)(
                    partial(self._visit_named_tuple, named_tuple_type=t)
                )

    @classmethod
    @lru_cache
    def get_visitor(cls, root_type: _StringableType, root_ndim: int) -> Self:
        return cls(root_type=root_type, root_ndim=root_ndim)

    def _visit_sequence(self, _: Never, children: _Children) -> list[Any]:
        return list(children[::2])

    def _visit_record(
        self, _: Never, children: _Children, *, record_type: type[record]
    ) -> record:
        return record_type(
            **ChainMap(
                *(child for child in children if isinstance(child, dict))
            )
        )

    def _visit_record_attr(
        self, _: Never, children: _Children, *, attribute: str
    ) -> dict[str, Any]:
        _, value = children
        return {attribute: value}

    def _visit_enumeration(
        self,
        _: Never,
        children: _Children,
        *,
        enumeration_type: type[enumeration],
    ) -> enumeration:
        return enumeration_type[children[-1]]

    def _visit_named_tuple(
        self,
        _: Never,
        children: _Children,
        *,
        named_tuple_type: type[enumeration],
    ) -> enumeration:
        return named_tuple_type(*children)

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

    def visit_typename(
        self, node: NonTerminal, children: _Children
    ) -> TypeName:
        parts = tuple(ident for name in children.name for ident in name)
        if isinstance(node[0], Terminal) and node[0].value == ".":
            parts = (".",) + parts

        return _BaseTypeName.__new__(TypeName, parts)

    def visit_name(self, _: Never, children: _Children) -> list[str]:
        return children.IDENT

    def visit_variablename(
        self, _: Never, children: _Children
    ) -> VariableName:
        (identifier,) = children
        return _BaseVariableName.__new__(VariableName, identifier)

    def visit_component(self, _: Never, children: _Children) -> Component:
        return Component(*children)

    def visit_subscript_list(self, node: NonTerminal, _: Never) -> list[str]:
        return [n.flat_str() for n in node[1::2]]  # type: ignore


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
