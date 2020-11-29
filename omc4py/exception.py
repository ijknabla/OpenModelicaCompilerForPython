
__all__ = (
    "OMCError",
    "OMCException",
    "OMCRuntimeError",
    "OMCWarning",
)

import typing
import warnings


def warn_always(
    warning_type: typing.Type[Warning],
) -> typing.Type[Warning]:
    warnings.simplefilter("always", warning_type)
    return warning_type


class OMCException(
    Exception,
):
    ...


@warn_always
class OMCNotification(
    OMCException,
    Warning,
):
    ...


@warn_always
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
