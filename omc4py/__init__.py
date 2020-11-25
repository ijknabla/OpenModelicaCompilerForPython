
__license__ = '''
/*
 * This file is part of OpenModelica.
 *
 * Copyright (c) 1998-CurrentYear, Open Source Modelica Consortium (OSMC),
 * c/o Linköpings universitet, Department of Computer and Information Science,
 * SE-58183 Linköping, Sweden.
 *
 * All rights reserved.
 *
 * THIS PROGRAM IS PROVIDED UNDER THE TERMS OF GPL VERSION 3 LICENSE OR
 * THIS OSMC PUBLIC LICENSE (OSMC-PL) VERSION 1.2.
 * ANY USE, REPRODUCTION OR DISTRIBUTION OF THIS PROGRAM CONSTITUTES
 * RECIPIENT'S ACCEPTANCE OF THE OSMC PUBLIC LICENSE OR THE GPL VERSION 3,
 * ACCORDING TO RECIPIENTS CHOICE.
 *
 * The OpenModelica software and the Open Source Modelica
 * Consortium (OSMC) Public License (OSMC-PL) are obtained
 * from OSMC, either from the above address,
 * from the URLs: http://www.ida.liu.se/projects/OpenModelica or
 * http://www.openmodelica.org, and in the OpenModelica distribution.
 * GNU version 3 is obtained from: http://www.gnu.org/copyleft/gpl.html.
 *
 * This program is distributed WITHOUT ANY WARRANTY; without
 * even the implied warranty of  MERCHANTABILITY or FITNESS
 * FOR A PARTICULAR PURPOSE, EXCEPT AS EXPRESSLY SET FORTH
 * IN THE BY RECIPIENT SELECTED SUBSIDIARY LICENSE CONDITIONS OF OSMC-PL.
 *
 * See the full OSMC Public License conditions for more details.
 *
 */
'''

from contextlib import contextmanager
import typing

from . import (
    classes,
    compiler,
    session,
)


@contextmanager
def open_session(
    omc_command: typing.Optional[compiler.StrOrPathLike] = None,
) -> typing.Iterator[classes.AbstractOMCSession]:
    with compiler.OMCInteractive.open(omc_command) as omc:
        sessionMinimal = session.OMCSessionMinimal(omc)
        version = sessionMinimal.getVersionTuple()
        if version[:2] <= (1, 13):
            from . import v_1_13
            yield v_1_13.OMCSession(omc)
        elif version[:2] == (1, 14):
            from . import v_1_14
            yield v_1_14.OMCSession(omc)
        elif version[:2] == (1, 15):
            from . import v_1_15
            yield v_1_15.OMCSession(omc)
        elif version[:2] >= (1, 16):
            from . import v_1_16
            yield v_1_16.OMCSession(omc)


def __select_session_type(
    omc: classes.AbstractOMCInteractive,
) -> typing.Type[classes.AbstractOMCSession]:
    version = session.OMCSessionMinimal(omc).getVersionTuple()
    if version[:2] <= (1, 13):
        from . import v_1_13
        return v_1_13.OMCSession
    elif version[:2] == (1, 14):
        from . import v_1_14
        return v_1_14.OMCSession
    elif version[:2] == (1, 15):
        from . import v_1_15
        return v_1_15.OMCSession
    else:  # version[:2] >= (1, 16):
        from . import v_1_16
        return v_1_16.OMCSession


def open_session2(
    omc_command: typing.Optional[compiler.StrOrPathLike] = None,
    *,
    session_type: typing.Optional[
        typing.Type[classes.AbstractOMCSession]
    ] = None,
) -> classes.AbstractOMCSession:
    omc = compiler.OMCInteractive.open(omc_command)

    if session_type is None:
        session_type = __select_session_type(omc)
    else:
        if not issubclass(session_type, classes.AbstractOMCSession):
            raise TypeError(
                "session_type must be "
                f"subclass of {classes.AbstractOMCSession}, "
                f"got {session_type}"
            )

    return session_type(omc)
