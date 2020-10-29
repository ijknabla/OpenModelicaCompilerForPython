
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
