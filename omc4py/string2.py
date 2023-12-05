from __future__ import annotations

import types
from contextlib import suppress
from functools import lru_cache
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
