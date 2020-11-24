
import re
import typing
import warnings

from omc4py import (
    exception,
)

from .classes import (
    AbstractOMCSession,
    Component,
)
from .parser import (
    ComponentTuple,
    parse_components,
)
from .classes import (
    String,
    TypeName,
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
        self.__omc_check__()
        return __result


omc_error_pattern = re.compile(
    r"(\[(?P<info>[^]]*)\]\s+)?(?P<kind>\w+):\s+(?P<message>.*)"
)


def parse_OMCError(
    error_string: str,
) -> typing.Optional[exception.OMCException]:
    if not error_string or error_string.isspace():
        return None

    matched = omc_error_pattern.match(
        error_string
    )
    if not matched:
        raise exception.OMCRuntimeError(
            f"Unexpected error message format: {error_string!r}"
        )
    # info = matched.group("info")
    kind = matched.group("kind")
    # message = matched.group("message")

    if kind == "Error":
        return exception.OMCError(error_string)
    else:
        return exception.OMCWarning(error_string)


class OMCSessionMinimal(
    OMCSessionBase,
):
    def __omc_check__(
        self,
    ) -> None:
        error_optional = parse_OMCError(self.getErrorString())
        error: exception.OMCException
        if error_optional is None:
            return
        else:
            error = error_optional

        if isinstance(error, Warning):
            warnings.warn(error)
        else:
            raise error

        self.__omc_check__()

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
            ]
        )
        self.__omc_check__()
        return str(__result)
