from __future__ import annotations

from typing import Coroutine, List, NamedTuple, Union, overload

from omc4py.modelica import enumeration, external, package
from omc4py.openmodelica import TypeName
from omc4py.protocol import (
    Asynchronous,
    SupportsInteractiveProperty,
    Synchronous,
    T_Calling,
)
from omc4py.session import BasicSession
from omc4py.v_1_22.OpenModelica.Scripting import (  # NOTE: update to latest
    ErrorMessage,
)

from . import Nested as nested


@overload
def loadFile(
    self: SupportsInteractiveProperty[Synchronous], fileName: str
) -> bool:
    ...


@overload
async def loadFile(
    self: SupportsInteractiveProperty[Asynchronous], fileName: str
) -> bool:
    ...


@external("loadFile")
def loadFile(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    fileName: str,
) -> Union[bool, Coroutine[None, None, bool]]:
    return ...  # type: ignore


@overload
def getMessagesStringInternal(
    self: SupportsInteractiveProperty[Synchronous],
    unique: Union[bool, None] = None,
) -> List[ErrorMessage]:
    ...


@overload
async def getMessagesStringInternal(
    self: SupportsInteractiveProperty[Asynchronous],
    unique: Union[bool, None] = None,
) -> List[ErrorMessage]:
    ...


@external("getMessagesStringInternal")
def getMessagesStringInternal(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    unique: Union[bool, None] = None,
) -> Union[List[ErrorMessage], Coroutine[None, None, List[ErrorMessage]]]:
    return ...  # type: ignore


@overload
def empty(self: SupportsInteractiveProperty[Synchronous]) -> None:
    ...


@overload
async def empty(self: SupportsInteractiveProperty[Asynchronous]) -> None:
    ...


@external(".empty")
def empty(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[None, Coroutine[None, None, None]]:
    ...


class GenericEmptySession(BasicSession[T_Calling]):
    loadFile = loadFile
    getMessagesStringInternal = getMessagesStringInternal
    empty = empty


EmptySession = GenericEmptySession[Synchronous]
AsyncEmptySession = GenericEmptySession[Asynchronous]


class Enum(enumeration):
    __omc_class__ = TypeName(".one.Enum")

    One = 1


class One(NamedTuple):
    real: float
    integer: int
    boolean: bool
    string: str
    enum: Enum


@overload
def one(self: SupportsInteractiveProperty[Synchronous]) -> One:
    ...


@overload
async def one(self: SupportsInteractiveProperty[Asynchronous]) -> One:
    ...


@external(".one")
def one(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[One, Coroutine[None, None, One]]:
    return ...  # type: ignore


class GenericOneSession(BasicSession[T_Calling]):
    loadFile = loadFile
    getMessagesStringInternal = getMessagesStringInternal
    one = one


OneSession = GenericOneSession[Synchronous]
AsyncOneSession = GenericOneSession[Asynchronous]


class Nested(package[T_Calling]):
    __omc_class__ = TypeName(".Nested")

    level = nested.level

    @property
    def Nested(self) -> nested.Nested[T_Calling]:
        return nested.Nested(self.__omc_interactive__)


class GenericNestedSession(BasicSession[T_Calling]):
    loadFile = loadFile
    getMessagesStringInternal = getMessagesStringInternal

    @property
    def Nested(self) -> Nested[T_Calling]:
        return Nested(self.__omc_interactive__)


NestedSession = GenericNestedSession[Synchronous]
AsyncNestedSession = GenericNestedSession[Asynchronous]
