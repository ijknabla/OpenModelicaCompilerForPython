
import abc
import re
import typing
import warnings

from . import (
    exception,
    compiler,
)

from .classes import (
    AbstractOMCInteractive,
    AbstractOMCSession,
    Component,
    String,
    TypeName,
)

from .parser import (
    ComponentTuple,
    parse_OMCExceptions,
    parse_OMCValue,
    parse_components,
)


def __select_session_type(
    omc: AbstractOMCInteractive,
) -> typing.Type[AbstractOMCSession]:
    """
Session class selector.
Update this after new omc version supported!!!
    """
    version = OMCSessionMinimal(omc).getVersionTuple()
    if version[:2] <= (1, 13):
        from . import v_1_13
        return v_1_13.OMCSession
    elif version[:2] == (1, 14):
        from . import v_1_14
        return v_1_14.OMCSession
    elif version[:2] == (1, 15):
        from . import v_1_15
        return v_1_15.OMCSession
    elif version[:2] == (1, 16):
        from . import v_1_16
        return v_1_16.OMCSession
    else:  # version[:2] >= (1, 17):
        from . import v_1_17
        return v_1_17.OMCSession


def open_session(
    omc_command: typing.Optional[compiler.StrOrPathLike] = None,
    *,
    session_type: typing.Optional[
        typing.Type[AbstractOMCSession]
    ] = None,
) -> AbstractOMCSession:
    omc = compiler.OMCInteractive.open(omc_command)

    try:
        if session_type is None:
            session_type = __select_session_type(omc)
        else:
            if not issubclass(session_type, AbstractOMCSession):
                raise TypeError(
                    "session_type must be "
                    f"subclass of {AbstractOMCSession}, "
                    f"got {session_type}"
                )

        return session_type(omc)

    except Exception:
        omc.close()
        raise


class OMCSessionBase(
    AbstractOMCSession,
):
    def getComponents(
        self,
        name: TypeName
    ) -> typing.Optional[typing.List[ComponentTuple]]:
        result_literal = self.__omc__.evaluate(
            f"getComponents({TypeName(name)})"
        )

        # return None if result_literal == "\n"
        if not result_literal or result_literal.isspace():
            return None

        try:
            result_value = parse_components(result_literal)
        except Exception:
            excs = list(parse_OMCExceptions(result_literal))
            if not excs:
                raise exception.OMCRuntimeError(
                    result_literal
                ) from None
            else:
                for exc in excs:
                    if isinstance(exc, Warning):
                        warnings.warn(exc)
                    else:
                        raise exc from None
                else:
                    return None

        return result_value


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
        for exc in parse_OMCExceptions(self.getErrorString()):
            if isinstance(exc, Warning):
                warnings.warn(exc)
            else:
                raise exc

    def getComponents(
        self,
        name: TypeName
    ) -> typing.Optional[typing.List[ComponentTuple]]:
        result = super().getComponents(name)
        self.__check__()
        return result

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
