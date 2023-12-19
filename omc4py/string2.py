from __future__ import annotations

import types
from collections.abc import Coroutine, Generator, Sequence
from contextlib import suppress
from dataclasses import dataclass
from functools import lru_cache
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
    Union,
    get_args,
    get_origin,
    get_type_hints,
)

from arpeggio import EOF, ParserPython, PTNodeVisitor, visit_parse_tree
from modelicalang import v3_4

if TYPE_CHECKING:
    from typing import _SpecialForm

    from typing_extensions import TypeGuard, Self
    from arpeggio import _ParsingExpressionLike

from .modelica import enumeration, record
from .openmodelica import Component, TypeName, VariableName
from .protocol import PathLike

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

    @classmethod
    @lru_cache
    def get_parser(
        cls, root_type: _StringableType, root_ndim: int
    ) -> ParserPython:
        return ParserPython(cls(root_type, root_ndim).root)

    def root(self) -> _ParsingExpressionLike:
        return EOF


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

    @classmethod
    @lru_cache
    def get_visitor(cls, root_type: _StringableType, root_ndim: int) -> Self:
        return cls(root_type=root_type, root_ndim=root_ndim)


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
