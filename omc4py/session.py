
import abc
import re
import typing
import warnings

from omc4py import (
    exception,
)

from .classes import (
    AbstractOMCSession,
    Component,
    String,
    TypeName,
)
from .parser import (
    ComponentTuple,
    parse_OMCError,
    parse_OMCValue,
    parse_components,
)


class OMCSessionBase(
    AbstractOMCSession,
):
    def getComponents(
        self,
        name: TypeName
    ) -> typing.List[ComponentTuple]:
        __result = parse_components(
            self.__omc__.evaluate(f"getComponents({TypeName(name)})")
        )
        self.__check__()
        return __result


class OMCSessionBase__v_1_13(
    OMCSessionBase,
):
    @abc.abstractmethod
    def getMessagesStringInternal(
        self,
        unique: bool,
    ) -> typing.Iterable:
        ...

    def __check__(
        self,
    ):
        for messageString in self.getMessagesStringInternal(unique=True):
            message = str(messageString.message)
            kind = messageString.kind.name
            py_message = f"{kind!s}: {message!r}"
            level = messageString.level.name

            if level == "notification":
                warnings.warn(
                    exception.OMCNotification(py_message)
                )
            elif level == "warning":
                warnings.warn(
                    exception.OMCWarning(py_message)
                )
            elif level == "error":
                raise exception.OMCError(py_message)
            else:
                raise exception.OMCRuntimeError(
                    f"Unexpected message level, got {level}"
                )


class OMCSessionMinimal(
    OMCSessionBase,
):
    def __check__(
        self,
    ) -> None:
        for errorString in self.getErrorString().splitlines():
            error = parse_OMCError(errorString)
            if error is None:
                return

            if isinstance(error, Warning):
                warnings.warn(error)
            else:
                raise error

    def getErrorString(
        self,
    ) -> str:
        __result = self.__omc__.call_function(
            funcName="getErrorString",
            inputArguments=[
            ],
            outputArguments=[
                (Component(String), "errorString")
            ],
            parser=parse_OMCValue,
        )
        return str(__result)

    def getVersion(
        self,
    ) -> str:
        __result = self.__omc__.call_function(
            funcName="getVersion",
            inputArguments=[
            ],
            outputArguments=[
                (Component(String), "version"),
            ],
            parser=parse_OMCValue,
        )
        self.__check__()
        return str(__result)

    def getVersionTuple(
        self,
    ) -> typing.Tuple[int, int, int]:
        versionMatch = re.search(
            r"(?P<major>\d+)\.(?P<minor>\d+)\.(?P<build>\d+)",
            self.getVersion(),
        )
        if versionMatch is None:
            raise ValueError("Can't parse version string")

        return (
            int(versionMatch.group("major")),
            int(versionMatch.group("minor")),
            int(versionMatch.group("build")),
        )
