from typing import List, Union

import neo.session.aio
from neo import TypeName
from neo.modelica import external


class Session(neo.session.aio.Session):
    @external(".OpenModelica.Scripting.getVersion")
    @staticmethod
    async def getVersion() -> str:
        raise NotImplementedError()

    @external(".OpenModelica.Scripting.list")
    @staticmethod
    async def list(class_: Union[TypeName, str], interfaceOnly: bool) -> str:
        raise NotImplementedError()

    @external(".OpenModelica.Scripting.getClassNames")
    @staticmethod
    async def getClassNames(
        class_: Union[TypeName, str],
        builtin: bool,
        showProtected: bool,
    ) -> List[TypeName]:
        raise NotImplementedError()

    @external(".OpenModelica.Scripting.getClassRestriction")
    @staticmethod
    async def getClassRestriction(cl: Union[TypeName, str]) -> str:
        raise NotImplementedError()

    @external(".OpenModelica.Scripting.isType")
    @staticmethod
    async def isType(cl: Union[TypeName, str]) -> bool:
        raise NotImplementedError()

    @external(".OpenModelica.Scripting.isPackage")
    @staticmethod
    async def isPackage(cl: Union[TypeName, str]) -> bool:
        raise NotImplementedError()

    @external(".OpenModelica.Scripting.isRecord")
    @staticmethod
    async def isRecord(cl: Union[TypeName, str]) -> bool:
        raise NotImplementedError()

    @external(".OpenModelica.Scripting.isFunction")
    @staticmethod
    async def isFunction(cl: Union[TypeName, str]) -> bool:
        raise NotImplementedError()

    @external(".OpenModelica.Scripting.isEnumeration")
    @staticmethod
    async def isEnumeration(cl: Union[TypeName, str]) -> bool:
        raise NotImplementedError()
