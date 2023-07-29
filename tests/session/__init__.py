from typing import TYPE_CHECKING, NamedTuple

from omc4py.latest import Session as BasicSession
from omc4py.modelica import enumeration, external, package


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
