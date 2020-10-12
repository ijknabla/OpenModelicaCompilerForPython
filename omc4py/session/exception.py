
__all__ = (
    "OMCError",
    "OMCException",
    "OMCWarning",
)

import re
import typing

from . import (
    InteractiveOMC,
    string,
)


class OMCException(
    Exception,
):
    ...


class OMCWarning(
    OMCException,
    Warning,
):
    ...


class OMCError(
    OMCException,
):
    ...


class OMCRuntimeError(
    OMCError,
    RuntimeError,
):
    ...


omc_error_pattern = re.compile(
    r"\[(?P<info>[^]]*)\]\s+(?P<kind>\w+):\s+(?P<message>.*)"
)


def parse_omc_error_message(
    error_message: str
) -> typing.Optional[OMCException]:
    error_message = error_message.rstrip()
    if not error_message:
        return None

    matched = omc_error_pattern.match(
        error_message
    )
    if not matched:
        raise OMCRuntimeError(
            f"Unexpected error message format: {error_message!r}"
        )
    # info = matched.group("info")
    kind = matched.group("kind")
    # message = matched.group("message")

    if kind == "Error":
        return OMCError(error_message)
    elif kind == "Warning":
        return OMCWarning(error_message)
    else:
        raise NotImplementedError(
            "Unexpected omc error kind: {kind!r}"
        )


def find_omc_error(
    omc: InteractiveOMC
) -> typing.Optional[OMCException]:
    error_message = omc.execute("getErrorString()").rstrip()
    return parse_omc_error_message(
        string.unquote_modelica_string(error_message)
    )
