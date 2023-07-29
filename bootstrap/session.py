from typing import List, Union

import omc4py.session.aio
from omc4py import TypeName
from omc4py.modelica import external


class Session(omc4py.session.aio.Session):
    @external(".OpenModelica.Scripting.getVersion")
    @classmethod
    async def getVersion(_) -> str:
        raise NotImplementedError()

    @external(".OpenModelica.Scripting.list")
    @classmethod
    async def list(
        _, class_: Union[TypeName, str], interfaceOnly: bool
    ) -> str:
        raise NotImplementedError()

    @external(".OpenModelica.Scripting.getClassNames")
    @classmethod
    async def getClassNames(
        _,
        class_: Union[TypeName, str],
        builtin: bool,
        showProtected: bool,
    ) -> List[TypeName]:
        raise NotImplementedError()

    @external(".OpenModelica.Scripting.getClassRestriction")
    @classmethod
    async def getClassRestriction(_, cl: Union[TypeName, str]) -> str:
        raise NotImplementedError()

    @external(".OpenModelica.Scripting.isType")
    @classmethod
    async def isType(_, cl: Union[TypeName, str]) -> bool:
        raise NotImplementedError()

    @external(".OpenModelica.Scripting.isPackage")
    @classmethod
    async def isPackage(_, cl: Union[TypeName, str]) -> bool:
        raise NotImplementedError()

    @external(".OpenModelica.Scripting.isRecord")
    @classmethod
    async def isRecord(_, cl: Union[TypeName, str]) -> bool:
        raise NotImplementedError()

    @external(".OpenModelica.Scripting.isFunction")
    @classmethod
    async def isFunction(_, cl: Union[TypeName, str]) -> bool:
        raise NotImplementedError()

    @external(".OpenModelica.Scripting.isEnumeration")
    @classmethod
    async def isEnumeration(_, cl: Union[TypeName, str]) -> bool:
        raise NotImplementedError()
