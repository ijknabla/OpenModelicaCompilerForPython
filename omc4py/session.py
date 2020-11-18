
import typing
import warnings

from omc4py import (
    classes,
    compiler,
    exception,
    parser,
    string,
    types,
)

from .classes import Component
from .types import (
    String,
)


class OMCSessionBase(
    classes.AbstractOMCSession,
):
    def getComponents(
        self,
        name: types.TypeName
    ) -> typing.List[parser.ComponentTuple]:
        __result = parser.parse_components(
            self.__omc__.evaluate(f"getComponents({types.TypeName(name)})")
        )
        self.__omc_check__()
        return __result


def parse_OMCError(
    error_message_literal: str,
) -> typing.Optional[exception.OMCException]:
    error_message = string.unquote_modelica_string(
        error_message_literal.rstrip()
    )
    if not error_message or error_message.isspace():
        return None

    matched = compiler.omc_error_pattern.match(
        error_message
    )
    if not matched:
        raise exception.OMCRuntimeError(
            f"Unexpected error message format: {error_message!r}"
        )
    # info = matched.group("info")
    kind = matched.group("kind")
    # message = matched.group("message")

    if kind == "Error":
        return exception.OMCError(error_message)
    else:
        return exception.OMCWarning(error_message)


class OMCSessionMinimal(
    OMCSessionBase,
):
    def __omc_check__(
        self,
    ) -> None:
        error_optional = parse_OMCError(
            self.__omc__.evaluate("getErrorString()")
        )
        if error_optional is None:
            return

        error = error_optional
        if isinstance(error, Warning):
            warnings.warn(error)
        else:
            raise error

        self.__omc_check__()

    def getVersion(
        self,
    ) -> str:
        __result = self.__omc__.call_function(
            funcName="getVersion",
            inputArguments=[
            ],
            outputArguments=[
                (Component(String), "version"),
            ]
        )
        self.__omc_check__()
        return str(__result)
