from __future__ import annotations

import types
from collections.abc import Generator, Sequence
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

from . import protocol
from .modelica import enumeration, record
from .openmodelica import Component, TypeName, VariableName

if TYPE_CHECKING:
    from typing import _SpecialForm

    from typing_extensions import TypeGuard

PrimitiveType = Union[
    Type[int],
    Type[float],
    Type[bool],
    Type[str],
    Type[VariableName],
    Type[TypeName],
    Type[record],
    Type[enumeration],
    Type[Component],
]
NamedTupleType = Type[Tuple[Any, ...]]
SupportedType = Union[PrimitiveType, NamedTupleType, None]


def get_type(obj: Any) -> SupportedType:
    if _is_named_tuple(obj):
        return obj

    types = set(_get_types(obj))
    if any(_issubclass(typ, (TypeName, VariableName)) for typ in types):
        types -= {str}
    if types - {None}:
        types -= {None}

    if len(types) == 1:
        (typ,) = types
        return typ

    raise TypeError(f"Types are ambigious or undefinable. got {types}")


def _get_types(obj: Any) -> Generator[PrimitiveType | None, None, None]:
    for unpacked in _unpack(obj):
        if _is_none(unpacked):
            yield None
        elif _is_primitive(unpacked):
            yield unpacked
        elif _is_path_like(unpacked):
            yield str
        elif _is_sequence(unpacked):
            yield from _get_types(get_args(unpacked)[0])


def get_ndim(obj: Any) -> int:
    if _is_named_tuple(obj):
        return 0

    ndims = set(_get_ndims(obj, ndim=0))

    if len(ndims) == 1:
        (ndim,) = ndims
        return ndim

    raise TypeError(f"Dimensions are ambigious or undefinable. got {ndims}")


def _get_ndims(obj: Any, ndim: int) -> Generator[int, None, None]:
    for unpacked in _unpack(obj):
        if _is_sequence(unpacked):
            yield from _get_ndims(get_args(unpacked)[0], ndim=ndim + 1)
        else:
            yield ndim


def _unpack(obj: Any) -> Generator[Any, None, None]:
    """
    Unpack Literal and Union

    match:
        case Literal[*args]:
            for arg in args:
                yield from _unpack(typ(arg))
        case Union[*args]:
            for arg in args:
                yield from _unpack(arg)
        case T:
            yield T
    """
    if _is_literal(obj):
        yield from chain.from_iterable(
            _unpack(type(arg)) for arg in get_args(obj)
        )
    elif _is_union(obj):
        yield from chain.from_iterable(_unpack(arg) for arg in get_args(obj))
    else:
        yield obj


def _is_none(obj: Any) -> TypeGuard[None]:
    return obj is None or _issubclass(obj, (type(None),))


def _is_literal(obj: Any) -> bool:
    return _issubclass(get_origin(obj), (Literal,))


def _is_union(obj: Any) -> bool:
    try:
        return _issubclass(get_origin(obj), (Union, types.UnionType))
    except AttributeError:
        return _issubclass(get_origin(obj), (Union,))


def _is_primitive(obj: Any) -> TypeGuard[PrimitiveType]:
    return _issubclass(obj, _primitive_types())


@lru_cache
def _primitive_types() -> tuple[PrimitiveType, ...]:
    return tuple(j for i in get_args(PrimitiveType) for j in get_args(i))


def _is_path_like(obj: Any) -> bool:
    return _issubclass(get_origin(obj), (protocol.PathLike,)) or _issubclass(
        obj, (protocol.PathLike,)
    )


def _is_sequence(obj: Any) -> TypeGuard[Type[Sequence[Any]]]:
    return (
        _issubclass(get_origin(obj), (Sequence,))
        and not _issubclass(obj, (Component,))
        and not _is_named_tuple(obj)
    )


def _is_named_tuple(obj: Any) -> TypeGuard[NamedTupleType]:
    return (
        _issubclass(obj, (tuple,))
        and bool(get_type_hints(obj))
        and not _issubclass(obj, (Component,))
    )


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
