from __future__ import annotations as _

from typing import Coroutine, Union, overload

from omc4py.modelica import external
from omc4py.protocol import (
    Asynchronous,
    SupportsInteractiveProperty,
    Synchronous,
)


@overload
def numBits(self: SupportsInteractiveProperty[Synchronous]) -> int:
    ...


@overload
async def numBits(self: SupportsInteractiveProperty[Asynchronous]) -> int:
    ...


@external("OpenModelica.Internal.Architecture.numBits")
def numBits(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[int, Coroutine[None, None, int]]:
    """
    .. code-block:: modelica

        function numBits
          output Integer numBit;
        end numBits;"""
    return ...  # type: ignore


@overload
def integerMax(self: SupportsInteractiveProperty[Synchronous]) -> int:
    ...


@overload
async def integerMax(self: SupportsInteractiveProperty[Asynchronous]) -> int:
    ...


@external("OpenModelica.Internal.Architecture.integerMax")
def integerMax(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[int, Coroutine[None, None, int]]:
    """
    .. code-block:: modelica

        function integerMax
          output Integer max;
        end integerMax;"""
    return ...  # type: ignore
