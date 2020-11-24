
__all__ = (
    "OMCError",
    "OMCException",
    "OMCRuntimeError",
    "OMCWarning",
)


class OMCException(
    Exception,
):
    ...


class OMCNotification(
    OMCException,
    Warning,
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
