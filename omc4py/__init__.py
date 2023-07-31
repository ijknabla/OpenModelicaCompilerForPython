from __future__ import annotations

__license__ = """
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
"""

__version__ = "0.3.0a0"

__all__ = (
    "TypeName",
    "VariableName",
    "__license__",
    "__version__",
    "open_session",
)
import re
from os import PathLike
from typing import TYPE_CHECKING, Any, overload

from typing_extensions import Literal

from . import session
from .exception import OMCRuntimeError
from .interactive import open_interactives
from .openmodelica import TypeName, VariableName
from .protocol import SupportsInteractive

if TYPE_CHECKING:
    from . import (
        latest,
        v_1_13,
        v_1_14,
        v_1_15,
        v_1_16,
        v_1_17,
        v_1_18,
        v_1_19,
        v_1_20,
        v_1_21,
    )

    Command = str | PathLike[str]

    Version__2_X = tuple[Literal[2], int]
    Version__1_X = tuple[
        Literal[1], Literal[22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
    ]
    Version__1_21 = tuple[Literal[1], Literal[21]]
    Version__1_20 = tuple[Literal[1], Literal[20]]
    Version__1_19 = tuple[Literal[1], Literal[19]]
    Version__1_18 = tuple[Literal[1], Literal[18]]
    Version__1_17 = tuple[Literal[1], Literal[17]]
    Version__1_16 = tuple[Literal[1], Literal[16]]
    Version__1_15 = tuple[Literal[1], Literal[15]]
    Version__1_14 = tuple[Literal[1], Literal[14]]
    Version__1_13 = tuple[Literal[1], Literal[13]]
    Version__1_12 = tuple[Literal[1], Literal[12]]
    Version__1_11 = tuple[Literal[1], Literal[11]]
    Version__1_10 = tuple[Literal[1], Literal[10]]
    Version__1_9 = tuple[Literal[1], Literal[9]]
    Version__1_8 = tuple[Literal[1], Literal[8]]
    Version__1_7 = tuple[Literal[1], Literal[7]]
    Version__1_6 = tuple[Literal[1], Literal[6]]
    Version__1_5 = tuple[Literal[1], Literal[5]]
    Version__1_4 = tuple[Literal[1], Literal[4]]
    Version__1_3 = tuple[Literal[1], Literal[3]]
    Version__1_2 = tuple[Literal[1], Literal[2]]
    Version__1_1 = tuple[Literal[1], Literal[1]]
    Version__1_0 = tuple[Literal[1], Literal[0]]
    Version__0_X = tuple[Literal[0], int]


def _select_session_type(
    version: tuple[int, int]
) -> tuple[type[session.Session], type[session.aio.Session]]:
    if (1, 21) <= version:
        from . import v_1_21

        return v_1_21.Session, v_1_21.aio.Session
    elif (1, 20) <= version:
        from . import v_1_20

        return v_1_20.Session, v_1_20.aio.Session
    elif (1, 19) <= version:
        from . import v_1_19

        return v_1_19.Session, v_1_19.aio.Session
    elif (1, 18) <= version:
        from . import v_1_18

        return v_1_18.Session, v_1_18.aio.Session
    elif (1, 17) <= version:
        from . import v_1_17

        return v_1_17.Session, v_1_17.aio.Session
    elif (1, 16) <= version:
        from . import v_1_16

        return v_1_16.Session, v_1_16.aio.Session
    elif (1, 15) <= version:
        from . import v_1_15

        return v_1_15.Session, v_1_15.aio.Session
    elif (1, 14) <= version:
        from . import v_1_14

        return v_1_14.Session, v_1_14.aio.Session
    else:
        from . import v_1_13

        return v_1_13.Session, v_1_13.aio.Session


# Latest
@overload
def open_session(
    omc_command: Command | None = None,
    *,
    version: Version__2_X | Version__1_X | None = None,
    asyncio: Literal[False] = False,
) -> latest.Session:
    ...


@overload
def open_session(
    omc_command: Command | None = None,
    *,
    version: Version__2_X | Version__1_X | None = None,
    asyncio: Literal[True],
) -> latest.aio.Session:
    ...


# v1.21
@overload
def open_session(
    omc_command: Command | None = None,
    *,
    version: Version__1_21,
    asyncio: Literal[False] = False,
) -> v_1_21.Session:
    ...


@overload
def open_session(
    omc_command: Command | None = None,
    *,
    version: Version__1_21,
    asyncio: Literal[True],
) -> v_1_21.aio.Session:
    ...


# v1.20
@overload
def open_session(
    omc_command: Command | None = None,
    *,
    version: Version__1_20,
    asyncio: Literal[False] = False,
) -> v_1_20.Session:
    ...


@overload
def open_session(
    omc_command: Command | None = None,
    *,
    version: Version__1_20,
    asyncio: Literal[True],
) -> v_1_20.aio.Session:
    ...


# v1.19
@overload
def open_session(
    omc_command: Command | None = None,
    *,
    version: Version__1_19,
    asyncio: Literal[False] = False,
) -> v_1_19.Session:
    ...


@overload
def open_session(
    omc_command: Command | None = None,
    *,
    version: Version__1_19,
    asyncio: Literal[True],
) -> v_1_19.aio.Session:
    ...


# v1.18
@overload
def open_session(
    omc_command: Command | None = None,
    *,
    version: Version__1_18,
    asyncio: Literal[False] = False,
) -> v_1_18.Session:
    ...


@overload
def open_session(
    omc_command: Command | None = None,
    *,
    version: Version__1_18,
    asyncio: Literal[True],
) -> v_1_18.aio.Session:
    ...


# v1.17
@overload
def open_session(
    omc_command: Command | None = None,
    *,
    version: Version__1_17,
    asyncio: Literal[False] = False,
) -> v_1_17.Session:
    ...


@overload
def open_session(
    omc_command: Command | None = None,
    *,
    version: Version__1_17,
    asyncio: Literal[True],
) -> v_1_17.aio.Session:
    ...


# v1.16
@overload
def open_session(
    omc_command: Command | None = None,
    *,
    version: Version__1_16,
    asyncio: Literal[False] = False,
) -> v_1_16.Session:
    ...


@overload
def open_session(
    omc_command: Command | None = None,
    *,
    version: Version__1_16,
    asyncio: Literal[True],
) -> v_1_16.aio.Session:
    ...


# v1.15
@overload
def open_session(
    omc_command: Command | None = None,
    *,
    version: Version__1_15,
    asyncio: Literal[False] = False,
) -> v_1_15.Session:
    ...


@overload
def open_session(
    omc_command: Command | None = None,
    *,
    version: Version__1_15,
    asyncio: Literal[True],
) -> v_1_15.aio.Session:
    ...


# v1.14
@overload
def open_session(
    omc_command: Command | None = None,
    *,
    version: Version__1_14,
    asyncio: Literal[False] = False,
) -> v_1_14.Session:
    ...


@overload
def open_session(
    omc_command: Command | None = None,
    *,
    version: Version__1_14,
    asyncio: Literal[True],
) -> v_1_14.aio.Session:
    ...


# v1.13
@overload
def open_session(
    omc_command: Command | None = None,
    *,
    version: Version__1_13
    | Version__1_12
    | Version__1_11
    | Version__1_10
    | Version__1_9
    | Version__1_8
    | Version__1_7
    | Version__1_6
    | Version__1_5
    | Version__1_4
    | Version__1_3
    | Version__1_2
    | Version__1_1
    | Version__1_0
    | Version__0_X,
    asyncio: Literal[False] = False,
) -> v_1_13.Session:
    ...


@overload
def open_session(
    omc_command: Command | None = None,
    *,
    version: Version__1_13
    | Version__1_12
    | Version__1_11
    | Version__1_10
    | Version__1_9
    | Version__1_8
    | Version__1_7
    | Version__1_6
    | Version__1_5
    | Version__1_4
    | Version__1_3
    | Version__1_2
    | Version__1_1
    | Version__1_0
    | Version__0_X,
    asyncio: Literal[True],
) -> v_1_13.aio.Session:
    ...


def open_session(
    omc_command: Command | None = None,
    *,
    version: tuple[int, int] | None = None,
    asyncio: bool = False,
) -> Any:
    interactive, aio_interactive = open_interactives(
        "omc" if omc_command is None else omc_command
    )

    try:
        session_type, aio_session_type = _select_session_type(
            _get_version(interactive)
        )
    except Exception:
        interactive.close()
        aio_interactive.close()
        raise

    if asyncio:
        return aio_session_type(aio_interactive)
    else:
        return session_type(interactive)


def _get_version(interactive: SupportsInteractive) -> tuple[int, int]:
    version = interactive.evaluate("getVersion()")
    matched = re.search(r"(\d+)\.(\d+)", version)
    if matched is None:
        raise OMCRuntimeError(f"Invalid version string {version!r}")
    return tuple(map(int, matched.groups()))  # type: ignore
