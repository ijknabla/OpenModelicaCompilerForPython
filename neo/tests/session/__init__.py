from typing import TYPE_CHECKING, NamedTuple

import neo.session
from neo.modelica import enumeration, external, package


class Session(neo.session.Session):
    @external(".OpenModelica.Scripting.loadFile")
    @staticmethod
    def loadFile(fileName: str) -> bool:
        raise NotImplementedError()


class EmptySession(Session):
    @external(".empty")
    @staticmethod
    def empty() -> None:
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


class OneSession(Session):
    @external(".one")
    @staticmethod
    def one() -> one:
        raise NotImplementedError()


@external(".Nested")
class Nested(package):
    @external(".Nested.level")
    @staticmethod
    def level() -> int:
        raise NotImplementedError()

    @external(".Nested.Nested")
    class Nested(package):
        @external(".Nested.Nested.level")
        @staticmethod
        def level() -> int:
            raise NotImplementedError()

        @external(".Nested.Nested.Nested")
        class Nested(package):
            @external(".Nested.Nested.Nested.level")
            @staticmethod
            def level() -> int:
                raise NotImplementedError()


class NestedSession(Session):
    Nested = Nested

    if TYPE_CHECKING:
        level_1 = staticmethod(Nested.level)
        level_2 = staticmethod(Nested.Nested.level)
        level_3 = staticmethod(Nested.Nested.Nested.level)
    else:
        level_1 = Nested.level
        level_2 = Nested.Nested.level
        level_3 = Nested.Nested.Nested.level
