from __future__ import annotations

import types
from collections.abc import Coroutine, Generator, Sequence
from contextlib import suppress
from functools import lru_cache
from itertools import chain
from typing import (
    TYPE_CHECKING,
    Any,
    Literal,
    Tuple,
    Type,
    Union,
    get_args,
    get_origin,
    get_type_hints,
)

if TYPE_CHECKING:
    from typing import _SpecialForm

    from typing_extensions import TypeGuard

from .modelica import enumeration, record
from .openmodelica import Component, TypeName, VariableName
from .protocol import PathLike

_Primitive = Union[float, int, bool, str, TypeName, VariableName, Component]
_Defined = Union[record, enumeration, Tuple[Any, ...]]
_StringableType = Union[Type[Union[_Primitive, _Defined]], None]


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
