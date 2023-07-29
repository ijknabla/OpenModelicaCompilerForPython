from typing import TYPE_CHECKING, NamedTuple

import omc4py.session
from omc4py.modelica import enumeration, external, package


class Session(omc4py.session.Session):
    @external(".OpenModelica.Scripting.loadFile")
    @classmethod
    def loadFile(_, fileName: str) -> bool:
        raise NotImplementedError()


class EmptySession(Session):
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


class OneSession(Session):
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
