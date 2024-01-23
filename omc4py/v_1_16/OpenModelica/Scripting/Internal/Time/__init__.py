from __future__ import annotations as _

from typing import Coroutine, Union, overload

from omc4py.modelica import external
from omc4py.protocol import (
    Asynchronous,
    SupportsInteractiveProperty,
    Synchronous,
)


@overload
def readableTime(
    self: SupportsInteractiveProperty[Synchronous], sec: float
) -> str:
    ...


@overload
async def readableTime(
    self: SupportsInteractiveProperty[Asynchronous], sec: float
) -> str:
    ...


@external("OpenModelica.Scripting.Internal.Time.readableTime")
def readableTime(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    sec: float,
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function readableTime
          input Real sec;
          output String str;
        end readableTime;"""
    return ...  # type: ignore


@overload
def timerTick(
    self: SupportsInteractiveProperty[Synchronous], index: int
) -> None:
    ...


@overload
async def timerTick(
    self: SupportsInteractiveProperty[Asynchronous], index: int
) -> None:
    ...


@external("OpenModelica.Scripting.Internal.Time.timerTick")
def timerTick(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    index: int,
) -> Union[None, Coroutine[None, None, None]]:
    """
    .. code-block:: modelica

        function timerTick
          input Integer index;
        end timerTick;"""


@overload
def timerTock(
    self: SupportsInteractiveProperty[Synchronous], index: int
) -> float:
    ...


@overload
async def timerTock(
    self: SupportsInteractiveProperty[Asynchronous], index: int
) -> float:
    ...


@external("OpenModelica.Scripting.Internal.Time.timerTock")
def timerTock(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    index: int,
) -> Union[float, Coroutine[None, None, float]]:
    """
    .. code-block:: modelica

        function timerTock
          input Integer index;
          output Real elapsed;
        end timerTock;"""
    return ...  # type: ignore


@overload
def timerClear(
    self: SupportsInteractiveProperty[Synchronous], index: int
) -> None:
    ...


@overload
async def timerClear(
    self: SupportsInteractiveProperty[Asynchronous], index: int
) -> None:
    ...


@external("OpenModelica.Scripting.Internal.Time.timerClear")
def timerClear(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    index: int,
) -> Union[None, Coroutine[None, None, None]]:
    """
    .. code-block:: modelica

        function timerClear
          input Integer index;
        end timerClear;"""
