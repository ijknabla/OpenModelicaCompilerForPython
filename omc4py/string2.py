from __future__ import annotations

from contextlib import suppress
from typing import TYPE_CHECKING, Any, Literal, get_origin

if TYPE_CHECKING:
    from typing import _SpecialForm

    from typing_extensions import TypeAlias, TypeGuard

SupportedType: TypeAlias = None


def _is_none(obj: Any) -> TypeGuard[None]:
    return obj is None or _issubclass(obj, (type(None),))


def _is_literal(obj: Any) -> bool:
    return _issubclass(get_origin(obj), (Literal,))


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
