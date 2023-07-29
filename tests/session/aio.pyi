from omc4py.latest.aio import Session as BasicSession
from omc4py.modelica import external, package

from . import one

class EmptySession(BasicSession):
    @external(".empty")
    @classmethod
    async def empty(_) -> None:
        raise NotImplementedError()

class OneSession(BasicSession):
    @external(".one")
    @classmethod
    async def one(_) -> one:
        raise NotImplementedError()

@external(".Nested")
class Nested(package):
    @external(".Nested.level")
    @classmethod
    async def level(_) -> int:
        raise NotImplementedError()
    @external(".Nested.Nested")
    class Nested(package):
        @external(".Nested.Nested.level")
        @classmethod
        async def level(_) -> int:
            raise NotImplementedError()
        @external(".Nested.Nested.Nested")
        class Nested(package):
            @external(".Nested.Nested.Nested.level")
            @classmethod
            async def level(_) -> int:
                raise NotImplementedError()

class NestedSession(BasicSession):
    Nested = Nested

    level_1 = staticmethod(Nested.level)
    level_2 = staticmethod(Nested.Nested.level)
    level_3 = staticmethod(Nested.Nested.Nested.level)
