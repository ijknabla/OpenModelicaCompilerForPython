import enum
from typing import ClassVar

from .openmodelica import TypeName


class enumeration(enum.Enum):
    __omc_class__: ClassVar[TypeName]


class record:
    __omc_class__: ClassVar[TypeName]
