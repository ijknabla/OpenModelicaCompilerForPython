from __future__ import annotations as _

from typing import Coroutine, Union, overload

from omc4py.modelica import external, package
from omc4py.openmodelica import TypeName
from omc4py.protocol import (
    Asynchronous,
    SupportsInteractiveProperty,
    Synchronous,
    T_Calling,
)

from . import Architecture as architecture


@overload
def ClockConstructor(self: SupportsInteractiveProperty[Synchronous]) -> None:
    ...


@overload
async def ClockConstructor(
    self: SupportsInteractiveProperty[Asynchronous],
) -> None:
    ...


@external("OpenModelica.Internal.ClockConstructor")
def ClockConstructor(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[None, Coroutine[None, None, None]]:
    ...


@overload
def intervalInferred(self: SupportsInteractiveProperty[Synchronous]) -> float:
    ...


@overload
async def intervalInferred(
    self: SupportsInteractiveProperty[Asynchronous],
) -> float:
    ...


@external("OpenModelica.Internal.intervalInferred")
def intervalInferred(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[float, Coroutine[None, None, float]]:
    """
    .. code-block:: modelica

        function intervalInferred
          output Real interval;
        end intervalInferred;"""
    return ...  # type: ignore


@overload
def delay2(
    self: SupportsInteractiveProperty[Synchronous],
    expr: float,
    delayTime: float,
) -> float:
    ...


@overload
async def delay2(
    self: SupportsInteractiveProperty[Asynchronous],
    expr: float,
    delayTime: float,
) -> float:
    ...


@external("OpenModelica.Internal.delay2")
def delay2(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    expr: float,
    delayTime: float,
) -> Union[float, Coroutine[None, None, float]]:
    """
    .. code-block:: modelica

        impure function delay2
          input Real expr;
          parameter input Real delayTime;
          output Real value;
        end delay2;"""
    return ...  # type: ignore


@overload
def delay3(
    self: SupportsInteractiveProperty[Synchronous],
    expr: float,
    delayTime: float,
    delayMax: float,
) -> float:
    ...


@overload
async def delay3(
    self: SupportsInteractiveProperty[Asynchronous],
    expr: float,
    delayTime: float,
    delayMax: float,
) -> float:
    ...


@external("OpenModelica.Internal.delay3")
def delay3(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    expr: float,
    delayTime: float,
    delayMax: float,
) -> Union[float, Coroutine[None, None, float]]:
    """
    .. code-block:: modelica

        impure function delay3
          input Real expr, delayTime;
          parameter input Real delayMax;
          output Real value;
        end delay3;"""
    return ...  # type: ignore


@overload
def intAbs(self: SupportsInteractiveProperty[Synchronous], v: int) -> int:
    ...


@overload
async def intAbs(
    self: SupportsInteractiveProperty[Asynchronous], v: int
) -> int:
    ...


@external("OpenModelica.Internal.intAbs")
def intAbs(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    v: int,
) -> Union[int, Coroutine[None, None, int]]:
    """
    .. code-block:: modelica

        function intAbs
          input Integer v;
          output Integer o;
        end intAbs;"""
    return ...  # type: ignore


@overload
def realAbs(self: SupportsInteractiveProperty[Synchronous], v: float) -> float:
    ...


@overload
async def realAbs(
    self: SupportsInteractiveProperty[Asynchronous], v: float
) -> float:
    ...


@external("OpenModelica.Internal.realAbs")
def realAbs(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    v: float,
) -> Union[float, Coroutine[None, None, float]]:
    """
    .. code-block:: modelica

        function realAbs
          input Real v;
          output Real o;
        end realAbs;"""
    return ...  # type: ignore


@overload
def intDiv(
    self: SupportsInteractiveProperty[Synchronous], x: int, y: int
) -> int:
    ...


@overload
async def intDiv(
    self: SupportsInteractiveProperty[Asynchronous], x: int, y: int
) -> int:
    ...


@external("OpenModelica.Internal.intDiv")
def intDiv(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    x: int,
    y: int,
) -> Union[int, Coroutine[None, None, int]]:
    """
    .. code-block:: modelica

        function intDiv
          input Integer x;
          input Integer y;
          output Integer z;
        end intDiv;"""
    return ...  # type: ignore


@overload
def realDiv(
    self: SupportsInteractiveProperty[Synchronous], x: float, y: float
) -> float:
    ...


@overload
async def realDiv(
    self: SupportsInteractiveProperty[Asynchronous], x: float, y: float
) -> float:
    ...


@external("OpenModelica.Internal.realDiv")
def realDiv(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    x: float,
    y: float,
) -> Union[float, Coroutine[None, None, float]]:
    """
    .. code-block:: modelica

        function realDiv
          input Real x;
          input Real y;
          output Real z;
        end realDiv;"""
    return ...  # type: ignore


@overload
def intMod(
    self: SupportsInteractiveProperty[Synchronous], x: int, y: int
) -> int:
    ...


@overload
async def intMod(
    self: SupportsInteractiveProperty[Asynchronous], x: int, y: int
) -> int:
    ...


@external("OpenModelica.Internal.intMod")
def intMod(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    x: int,
    y: int,
) -> Union[int, Coroutine[None, None, int]]:
    """
    .. code-block:: modelica

        function intMod
          input Integer x;
          input Integer y;
          output Integer z;
        end intMod;"""
    return ...  # type: ignore


@overload
def realMod(
    self: SupportsInteractiveProperty[Synchronous], x: float, y: float
) -> float:
    ...


@overload
async def realMod(
    self: SupportsInteractiveProperty[Asynchronous], x: float, y: float
) -> float:
    ...


@external("OpenModelica.Internal.realMod")
def realMod(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    x: float,
    y: float,
) -> Union[float, Coroutine[None, None, float]]:
    """
    .. code-block:: modelica

        function realMod
          input Real x;
          input Real y;
          output Real z;
        end realMod;"""
    return ...  # type: ignore


@overload
def intRem(
    self: SupportsInteractiveProperty[Synchronous], x: int, y: int
) -> int:
    ...


@overload
async def intRem(
    self: SupportsInteractiveProperty[Asynchronous], x: int, y: int
) -> int:
    ...


@external("OpenModelica.Internal.intRem")
def intRem(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    x: int,
    y: int,
) -> Union[int, Coroutine[None, None, int]]:
    """
    .. code-block:: modelica

        function intRem
          input Integer x;
          input Integer y;
          output Integer z;
        end intRem;"""
    return ...  # type: ignore


@overload
def realRem(
    self: SupportsInteractiveProperty[Synchronous], x: float, y: float
) -> float:
    ...


@overload
async def realRem(
    self: SupportsInteractiveProperty[Asynchronous], x: float, y: float
) -> float:
    ...


@external("OpenModelica.Internal.realRem")
def realRem(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    x: float,
    y: float,
) -> Union[float, Coroutine[None, None, float]]:
    """
    .. code-block:: modelica

        function realRem
          input Real x;
          input Real y;
          output Real z;
        end realRem;"""
    return ...  # type: ignore


class Architecture(package[T_Calling]):
    __omc_class__ = TypeName("OpenModelica.Internal.Architecture")
    numBits = architecture.numBits
    integerMax = architecture.integerMax
