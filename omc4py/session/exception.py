
__all__ = (
    "OMCError",
    "OMCException",
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
