import neo.session.aio
from neo.modelica import external, package

from . import one

class Session(neo.session.aio.Session):
    @external(".OpenModelica.Scripting.loadFile")
    @staticmethod
    async def loadFile(fileName: str) -> bool:
        raise NotImplementedError()

class EmptySession(Session):
    @external(".empty")
    @staticmethod
    async def empty() -> None:
        raise NotImplementedError()

class OneSession(Session):
    @external(".one")
    @staticmethod
    async def one() -> one:
        raise NotImplementedError()

@external(".Nested")
class Nested(package):
    @external(".Nested.level")
    @staticmethod
    async def level() -> int:
        raise NotImplementedError()
    @external(".Nested.Nested")
    class Nested(package):
        @external(".Nested.Nested.level")
        @staticmethod
        async def level() -> int:
            raise NotImplementedError()
        @external(".Nested.Nested.Nested")
        class Nested(package):
            @external(".Nested.Nested.Nested.level")
            @staticmethod
            async def level() -> int:
                raise NotImplementedError()

class NestedSession(Session):
    Nested = Nested

    level_1 = staticmethod(Nested.level)
    level_2 = staticmethod(Nested.Nested.level)
    level_3 = staticmethod(Nested.Nested.Nested.level)
