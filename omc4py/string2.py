from __future__ import annotations

from contextlib import suppress
from typing import TYPE_CHECKING, Any, Tuple, Type, Union

if TYPE_CHECKING:
    from typing import _SpecialForm

    from typing_extensions import TypeGuard

from .modelica import enumeration, record
from .openmodelica import Component, TypeName, VariableName

_Primitive = Union[float, int, bool, str, TypeName, VariableName, Component]
_Defined = Union[record, enumeration, Tuple[Any, ...]]
_StringableType = Union[Type[Union[_Primitive, _Defined]], None]


def _is_none(obj: Any) -> TypeGuard[None | type[None]]:
    return obj is None or _issubclass(obj, (type(None),))


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
