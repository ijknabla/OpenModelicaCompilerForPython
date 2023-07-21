from __future__ import annotations

import enum
from collections.abc import Callable
from functools import partial
from typing import ClassVar, TypeVar

from .openmodelica import TypeName

_T = TypeVar("_T")
_T_class = TypeVar("_T_class", "enumeration", "record")


def external(class_name: str) -> Callable[[_T], _T]:
    return partial(_external, class_name=class_name)  # type: ignore


class enumeration(enum.Enum):
    __omc_class__: ClassVar[TypeName]


class record:
    __omc_class__: ClassVar[TypeName]


def _external(typ: type[_T_class], class_name: str) -> type[_T_class]:
    typ.__omc_class__ = TypeName(class_name)
    return typ
