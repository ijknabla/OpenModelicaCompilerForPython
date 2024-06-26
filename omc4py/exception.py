from __future__ import annotations

__all__ = (
    "OMCError",
    "OMCException",
    "OMCRuntimeError",
    "OMCWarning",
)

import warnings


def warn_always(
    warning_type: type[Warning],
) -> type[Warning]:
    warnings.simplefilter("always", warning_type)
    return warning_type


class OMCException(
    Exception,
):
    pass


@warn_always
class OMCNotification(
    OMCException,
    Warning,
):
    pass


@warn_always
class OMCWarning(
    OMCException,
    Warning,
):
    pass


class OMCError(
    OMCException,
):
    pass


class OMCRuntimeError(
    OMCException,
    RuntimeError,
):
    pass
