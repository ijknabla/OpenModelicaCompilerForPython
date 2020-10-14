
__all__ = (
    "OMCError",
    "OMCException",
    "OMCWarning",
    "find_omc_error",
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


def find_omc_error(
    omc: InteractiveOMC
) -> typing.Optional[OMCException]:
    error_message = string.unquote_modelica_string(
        omc.evaluate("getErrorString()").rstrip()
    )
    if not error_message or error_message.isspace():
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
