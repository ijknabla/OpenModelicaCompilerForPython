from __future__ import annotations

from typing import Coroutine, Union, overload

from omc4py.modelica2 import external
from omc4py.protocol import (
    Asynchronous,
    SupportsInteractiveProperty,
    Synchronous,
)


@overload
def level(self: SupportsInteractiveProperty[Synchronous]) -> int:
    ...


@overload
async def level(self: SupportsInteractiveProperty[Asynchronous]) -> int:
    ...


@external(".Nested.Nested.Nested.level")
def level(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[int, Coroutine[None, None, int]]:
    return ...  # type: ignore
