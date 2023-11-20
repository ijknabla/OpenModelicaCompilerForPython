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
from typing import TYPE_CHECKING, Any
from typing import Literal
from typing import Literal as L
from typing import Tuple
from typing import Tuple as T
from typing import Union, overload

from .exception import OMCRuntimeError
from .interactive import Interactive
from .openmodelica import TypeName, VariableName
from .protocol import (
    Asynchronous,
    SupportsInteractive,
    Synchronous,
    synchronous,
)
from .session import BasicSession

if TYPE_CHECKING:
    from . import (
        v_1_13,
        v_1_14,
        v_1_15,
        v_1_16,
        v_1_17,
        v_1_18,
        v_1_19,
        v_1_20,
        v_1_21,
        v_1_22,
    )

    Command = Union[str, PathLike[str]]


def _select_session_type(
    version: Tuple[int, int]
) -> Tuple[type[BasicSession[Synchronous]], type[BasicSession[Asynchronous]]]:
    if False:
        pass
    elif (1, 22) <= version:
        from . import v_1_22

        return v_1_22.Session, v_1_22.AsyncSession
    elif (1, 21) <= version:
        from . import v_1_21

        return v_1_21.Session, v_1_21.AsyncSession
    elif (1, 20) <= version:
        from . import v_1_20

        return v_1_20.Session, v_1_20.AsyncSession
    elif (1, 19) <= version:
        from . import v_1_19

        return v_1_19.Session, v_1_19.AsyncSession
    elif (1, 18) <= version:
        from . import v_1_18

        return v_1_18.Session, v_1_18.AsyncSession
    elif (1, 17) <= version:
        from . import v_1_17

        return v_1_17.Session, v_1_17.AsyncSession
    elif (1, 16) <= version:
        from . import v_1_16

        return v_1_16.Session, v_1_16.AsyncSession
    elif (1, 15) <= version:
        from . import v_1_15

        return v_1_15.Session, v_1_15.AsyncSession
    elif (1, 14) <= version:
        from . import v_1_14

        return v_1_14.Session, v_1_14.AsyncSession
    else:
        from . import v_1_13

        return v_1_13.Session, v_1_13.AsyncSession


# Latest
@overload
def open_session(
    omc_command: Command | None = None,
    *,
    version: T[L[1], L[22]] | T[L[1], L[23]] | T[L[1], L[24]] | None = None,
    asyncio: Literal[False] = False,
) -> v_1_22.Session:
    ...


@overload
def open_session(
    omc_command: Command | None = None,
    *,
    version: T[L[1], L[22]] | T[L[1], L[23]] | T[L[1], L[24]] | None = None,
    asyncio: Literal[True],
) -> v_1_22.AsyncSession:
    ...


# v1.21
@overload
def open_session(
    omc_command: Command | None = None,
    *,
    version: T[L[1], L[21]],
    asyncio: Literal[False] = False,
) -> v_1_21.Session:
    ...


@overload
def open_session(
    omc_command: Command | None = None,
    *,
    version: T[L[1], L[21]],
    asyncio: Literal[True],
) -> v_1_21.AsyncSession:
    ...


# v1.20
@overload
def open_session(
    omc_command: Command | None = None,
    *,
    version: T[L[1], L[20]],
    asyncio: Literal[False] = False,
) -> v_1_20.Session:
    ...


@overload
def open_session(
    omc_command: Command | None = None,
    *,
    version: T[L[1], L[20]],
    asyncio: Literal[True],
) -> v_1_20.AsyncSession:
    ...


# v1.19
@overload
def open_session(
    omc_command: Command | None = None,
    *,
    version: T[L[1], L[19]],
    asyncio: Literal[False] = False,
) -> v_1_19.Session:
    ...


@overload
def open_session(
    omc_command: Command | None = None,
    *,
    version: T[L[1], L[19]],
    asyncio: Literal[True],
) -> v_1_19.AsyncSession:
    ...


# v1.18
@overload
def open_session(
    omc_command: Command | None = None,
    *,
    version: T[L[1], L[18]],
    asyncio: Literal[False] = False,
) -> v_1_18.Session:
    ...


@overload
def open_session(
    omc_command: Command | None = None,
    *,
    version: T[L[1], L[18]],
    asyncio: Literal[True],
) -> v_1_18.AsyncSession:
    ...


# v1.17
@overload
def open_session(
    omc_command: Command | None = None,
    *,
    version: T[L[1], L[17]],
    asyncio: Literal[False] = False,
) -> v_1_17.Session:
    ...


@overload
def open_session(
    omc_command: Command | None = None,
    *,
    version: T[L[1], L[17]],
    asyncio: Literal[True],
) -> v_1_17.AsyncSession:
    ...


# v1.16
@overload
def open_session(
    omc_command: Command | None = None,
    *,
    version: T[L[1], L[16]],
    asyncio: Literal[False] = False,
) -> v_1_16.Session:
    ...


@overload
def open_session(
    omc_command: Command | None = None,
    *,
    version: T[L[1], L[16]],
    asyncio: Literal[True],
) -> v_1_16.AsyncSession:
    ...


# v1.15
@overload
def open_session(
    omc_command: Command | None = None,
    *,
    version: T[L[1], L[15]],
    asyncio: Literal[False] = False,
) -> v_1_15.Session:
    ...


@overload
def open_session(
    omc_command: Command | None = None,
    *,
    version: T[L[1], L[15]],
    asyncio: Literal[True],
) -> v_1_15.AsyncSession:
    ...


# v1.14
@overload
def open_session(
    omc_command: Command | None = None,
    *,
    version: T[L[1], L[14]],
    asyncio: Literal[False] = False,
) -> v_1_14.Session:
    ...


@overload
def open_session(
    omc_command: Command | None = None,
    *,
    version: T[L[1], L[14]],
    asyncio: Literal[True],
) -> v_1_14.AsyncSession:
    ...


# v1.13
@overload
def open_session(
    omc_command: Command | None = None,
    *,
    version: T[L[1], L[13]],
    asyncio: Literal[False] = False,
) -> v_1_13.Session:
    ...


@overload
def open_session(
    omc_command: Command | None = None,
    *,
    version: T[L[1], L[13]],
    asyncio: Literal[True],
) -> v_1_13.AsyncSession:
    ...


def open_session(
    omc_command: Command | None = None,
    *,
    version: Tuple[int, int] | None = None,
    asyncio: bool = False,
) -> Any:
    interactive = Interactive.open(
        "omc" if omc_command is None else omc_command,
        synchronous,
    )

    try:
        session_type, aio_session_type = _select_session_type(
            _get_version(interactive)
        )
    except Exception:
        interactive.close()
        raise

    if asyncio:
        return aio_session_type(interactive.asynchronous)
    else:
        return session_type(interactive)


def _get_version(
    interactive: SupportsInteractive[Synchronous],
) -> Tuple[int, int]:
    version = interactive.evaluate("getVersion()")
    matched = re.search(r"(\d+)\.(\d+)", version)
    if matched is None:
        raise OMCRuntimeError(f"Invalid version string {version!r}")
    major, minor = tuple(map(int, matched.groups()))
    return major, minor
