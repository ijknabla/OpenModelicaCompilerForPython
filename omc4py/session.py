
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

__all__ = ("cast_value",)
from .compiler import cast_value


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


class OMCSessionMinimal(
    OMCSessionBase,
):
    def __omc_check__(
        self,
    ) -> None:
        while True:
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


def OMCSession__open(
    OMCSessionType: typing.Type[OMCSessionBase],
    omc_command: typing.Optional[compiler.StrOrPathLike] = None,
) -> OMCSessionBase:
    omc = compiler.OMCInteractive.open(
        omc_command=omc_command,
    )
    return OMCSessionType(omc)


def OMCSession__close(
    self: OMCSessionBase
):
    self._omc.close()


PositionalArguments = typing.List[typing.Any]
KeywordArguments = typing.Dict[str, typing.Any]


def OMCSession__call(
    self: OMCSessionBase,
    funcName: str,
    *,
    parse: bool = True,
    args: typing.Optional[PositionalArguments] = None,
    kwrds: typing.Optional[KeywordArguments] = None,
) -> typing.Any:
    argument_literals: typing.List[str] = []
    if args is not None:
        for arg in args:
            argument_literals.append(
                string.to_omc_literal(arg)
            )
    if kwrds is not None:
        for ident, value in kwrds.items():
            if value is None:
                continue
            value_literal = string.to_omc_literal(
                value
            )
            argument_literals.append(
                f"{ident}={value_literal}"
            )

    arguments_literal = ", ".join(argument_literals)

    result_literal = self._omc.evaluate(
        f"{funcName}({arguments_literal})"
    )

    error = self._omc.find_error()

    if error is not None:
        if isinstance(error, Warning):
            warnings.warn(error)
        else:
            raise error

    if parse:
        return parser.parse_OMCValue(result_literal)
    else:
        return result_literal
