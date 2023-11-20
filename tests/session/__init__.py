from __future__ import annotations

from collections.abc import Coroutine
from typing import TYPE_CHECKING, NamedTuple, Union, overload

from omc4py import modelica2
from omc4py.latest import Session as BasicSession
from omc4py.modelica import enumeration, external, package
from omc4py.protocol import (
    Asynchronous,
    SupportsInteractiveProperty,
    Synchronous,
)


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


class EmptySession(BasicSession):
    @external(".empty")
    @classmethod
    def empty(_) -> None:
        raise NotImplementedError()


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
