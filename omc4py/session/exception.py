

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
