
__all__ = (
    "open_session",
    "Real",
    "Integer",
    "Boolean",
    "String",
    "VariableName",
    "TypeName",
    "OpenModelica",
    "OMCSession",
)

import functools
import omc4py.session

from ._omc_interface import (
    Boolean,
    Integer,
    OMCSession,
    OpenModelica,
    Real,
    String,
    TypeName,
    VariableName,
)


open_session = functools.partial(
    omc4py.session.open_session,
    session_type=OMCSession,
)
