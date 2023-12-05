from __future__ import annotations

import types
from contextlib import suppress
from functools import lru_cache
from typing import (
    TYPE_CHECKING,
    Any,
    Literal,
    Type,
    Union,
    get_args,
    get_origin,
)

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
SupportedType = Union[PrimitiveType, None]


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
