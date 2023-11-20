from __future__ import annotations

from typing import Coroutine, Union, overload

from omc4py.modelica2 import external, package
from omc4py.openmodelica import TypeName
from omc4py.protocol import (
    Asynchronous,
    SupportsInteractiveProperty,
    Synchronous,
    T_Calling,
)

from . import Nested as nested


@overload
def level(self: SupportsInteractiveProperty[Synchronous]) -> int:
    ...


@overload
async def level(self: SupportsInteractiveProperty[Asynchronous]) -> int:
    ...


@external(".Nested.level")
def level(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[int, Coroutine[None, None, int]]:
    return ...  # type: ignore


class Nested(package[T_Calling]):
    __omc_class__ = TypeName(".Nested.Nested")

    level = nested.level

    @property
    def Nested(self) -> nested.Nested[T_Calling]:
        return nested.Nested(self.__omc_interactive__)
