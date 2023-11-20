from __future__ import annotations

from collections.abc import Coroutine
from typing import TYPE_CHECKING, List, NamedTuple, Union, overload

from omc4py import modelica2, openmodelica2
from omc4py.latest import Session as BasicSession
from omc4py.modelica import enumeration, external, package
from omc4py.protocol import (
    Asynchronous,
    SupportsInteractiveProperty,
    Synchronous,
    T_Calling,
)
from omc4py.v_1_21._interface import OpenModelica  # NOTE: update to latest


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


@modelica2.external("loadFile")
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
    self: SupportsInteractiveProperty[Synchronous], unique: bool | None = None
) -> List[OpenModelica.Scripting.ErrorMessage]:
    ...


@overload
async def getMessagesStringInternal(
    self: SupportsInteractiveProperty[Asynchronous], unique: bool | None = None
) -> List[OpenModelica.Scripting.ErrorMessage]:
    ...


@modelica2.external("getMessagesStringInternal")
def getMessagesStringInternal(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    unique: bool | None = None,
) -> Union[
    List[OpenModelica.Scripting.ErrorMessage],
    Coroutine[None, None, List[OpenModelica.Scripting.ErrorMessage]],
]:
    return ...  # type: ignore


@overload
def empty(self: SupportsInteractiveProperty[Synchronous]) -> None:
    ...


@overload
async def empty(self: SupportsInteractiveProperty[Asynchronous]) -> None:
    ...


@modelica2.external(".empty")
def empty(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[None, Coroutine[None, None, None]]:
    ...


class GenericEmptySession(openmodelica2.BasicSession[T_Calling]):
    loadFile = loadFile
    getMessagesStringInternal = getMessagesStringInternal
    empty = empty


EmptySession = GenericEmptySession[Synchronous]
AsyncEmptySession = GenericEmptySession[Asynchronous]


@external(".one.Enum")
class Enum(enumeration):
    One = 1


class one(NamedTuple):
    real: float
    integer: int
    boolean: bool
    string: str
    enum: Enum


class OneSession(BasicSession):
    @external(".one")
    @classmethod
    def one(_) -> one:
        raise NotImplementedError()


@external(".Nested")
class Nested(package):
    @external(".Nested.level")
    @classmethod
    def level(_) -> int:
        raise NotImplementedError()

    @external(".Nested.Nested")
    class Nested(package):
        @external(".Nested.Nested.level")
        @classmethod
        def level(_) -> int:
            raise NotImplementedError()

        @external(".Nested.Nested.Nested")
        class Nested(package):
            @external(".Nested.Nested.Nested.level")
            @classmethod
            def level(_) -> int:
                raise NotImplementedError()


class NestedSession(BasicSession):
    Nested = Nested

    if TYPE_CHECKING:
        level_1 = staticmethod(Nested.level)
        level_2 = staticmethod(Nested.Nested.level)
        level_3 = staticmethod(Nested.Nested.Nested.level)
    else:
        level_1 = Nested.level
        level_2 = Nested.Nested.level
        level_3 = Nested.Nested.Nested.level
