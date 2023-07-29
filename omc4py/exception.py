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
