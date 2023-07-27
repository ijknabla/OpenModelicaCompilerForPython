import neo.session.aio
from neo.modelica import external, package

from . import one

class Session(neo.session.aio.Session):
    @external(".OpenModelica.Scripting.loadFile")
    @classmethod
    async def loadFile(_, fileName: str) -> bool:
        raise NotImplementedError()

class EmptySession(Session):
    @external(".empty")
    @classmethod
    async def empty(_) -> None:
        raise NotImplementedError()

class OneSession(Session):
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

class NestedSession(Session):
    Nested = Nested

    level_1 = staticmethod(Nested.level)
    level_2 = staticmethod(Nested.Nested.level)
    level_3 = staticmethod(Nested.Nested.Nested.level)