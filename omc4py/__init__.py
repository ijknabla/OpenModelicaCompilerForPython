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

__version__ = "0.3.2"

__all__ = (
    "AsyncSession",
    "GenericSession",
    "Session",
    "TypeName",
    "VariableName",
    "open_session",
)
import re
from os import PathLike
from typing import TYPE_CHECKING, Any, Literal, Tuple, Union, overload

from .exception import OMCRuntimeError
from .interactive import Interactive
from .openmodelica import TypeName, VariableName
from .protocol import (
    Asynchronous,
    Calling,
    SupportsInteractive,
    Synchronous,
    T_Calling,
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
        v_1_23,
    )

    GenericSession = Union[
        v_1_23.GenericSession[T_Calling],  # NOTE: update to latest
        v_1_22.GenericSession[T_Calling],
        v_1_21.GenericSession[T_Calling],
        v_1_20.GenericSession[T_Calling],
        v_1_19.GenericSession[T_Calling],
        v_1_18.GenericSession[T_Calling],
        v_1_17.GenericSession[T_Calling],
        v_1_16.GenericSession[T_Calling],
        v_1_15.GenericSession[T_Calling],
        v_1_14.GenericSession[T_Calling],
        v_1_13.GenericSession[T_Calling],
    ]

    _1_25 = tuple[Literal[1], Literal[25]]
    _1_24 = tuple[Literal[1], Literal[24]]

    _1_23 = tuple[Literal[1], Literal[23]]  # NOTE: update to latest
    _1_22 = tuple[Literal[1], Literal[22]]
    _1_21 = tuple[Literal[1], Literal[21]]
    _1_20 = tuple[Literal[1], Literal[20]]
    _1_19 = tuple[Literal[1], Literal[19]]
    _1_18 = tuple[Literal[1], Literal[18]]
    _1_17 = tuple[Literal[1], Literal[17]]
    _1_16 = tuple[Literal[1], Literal[16]]
    _1_15 = tuple[Literal[1], Literal[15]]
    _1_14 = tuple[Literal[1], Literal[14]]
    _1_13 = tuple[Literal[1], Literal[13]]

else:
    GenericSession = BasicSession

Session = GenericSession[Synchronous]
AsyncSession = GenericSession[Asynchronous]


def _select_session_type(
    version: Tuple[int, int]
) -> Tuple[type[BasicSession[Synchronous]], type[BasicSession[Asynchronous]]]:
    if False:
        pass
    elif (1, 23) <= version:  # NOTE: update to latest
        from . import v_1_23

        return v_1_23.Session, v_1_23.AsyncSession
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


# v1.23  NOTE: update to latest
@overload
def open_session(
    omc: str | PathLike[str] | None = None,
    *,
    version: _1_23 | _1_24 | _1_25,
    asyncio: Literal[False] = False,
) -> v_1_23.Session:
    ...


@overload
def open_session(
    omc: str | PathLike[str] | None = None,
    *,
    version: _1_23 | _1_24 | _1_25,
    asyncio: Literal[True],
) -> v_1_23.AsyncSession:
    ...


@overload
def open_session(
    omc: SupportsInteractive[T_Calling],
    *,
    version: _1_23 | _1_24 | _1_25,
) -> v_1_23.GenericSession[T_Calling]:
    ...


# v1.22
@overload
def open_session(
    omc: str | PathLike[str] | None = None,
    *,
    version: _1_22,
    asyncio: Literal[False] = False,
) -> v_1_22.Session:
    ...


@overload
def open_session(
    omc: str | PathLike[str] | None = None,
    *,
    version: _1_22,
    asyncio: Literal[True],
) -> v_1_22.AsyncSession:
    ...


@overload
def open_session(
    omc: SupportsInteractive[T_Calling],
    *,
    version: _1_22,
) -> v_1_22.GenericSession[T_Calling]:
    ...


# v1.21
@overload
def open_session(
    omc: str | PathLike[str] | None = None,
    *,
    version: _1_21,
    asyncio: Literal[False] = False,
) -> v_1_21.Session:
    ...


@overload
def open_session(
    omc: str | PathLike[str] | None = None,
    *,
    version: _1_21,
    asyncio: Literal[True],
) -> v_1_21.AsyncSession:
    ...


@overload
def open_session(
    omc: SupportsInteractive[T_Calling],
    *,
    version: _1_21,
) -> v_1_21.GenericSession[T_Calling]:
    ...


# v1.20
@overload
def open_session(
    omc: str | PathLike[str] | None = None,
    *,
    version: _1_20,
    asyncio: Literal[False] = False,
) -> v_1_20.Session:
    ...


@overload
def open_session(
    omc: str | PathLike[str] | None = None,
    *,
    version: _1_20,
    asyncio: Literal[True],
) -> v_1_20.AsyncSession:
    ...


@overload
def open_session(
    omc: SupportsInteractive[T_Calling],
    *,
    version: _1_20,
) -> v_1_20.GenericSession[T_Calling]:
    ...


# v1.19
@overload
def open_session(
    omc: str | PathLike[str] | None = None,
    *,
    version: _1_19,
    asyncio: Literal[False] = False,
) -> v_1_19.Session:
    ...


@overload
def open_session(
    omc: str | PathLike[str] | None = None,
    *,
    version: _1_19,
    asyncio: Literal[True],
) -> v_1_19.AsyncSession:
    ...


@overload
def open_session(
    omc: SupportsInteractive[T_Calling],
    *,
    version: _1_19,
) -> v_1_19.GenericSession[T_Calling]:
    ...


# v1.18
@overload
def open_session(
    omc: str | PathLike[str] | None = None,
    *,
    version: _1_18,
    asyncio: Literal[False] = False,
) -> v_1_18.Session:
    ...


@overload
def open_session(
    omc: str | PathLike[str] | None = None,
    *,
    version: _1_18,
    asyncio: Literal[True],
) -> v_1_18.AsyncSession:
    ...


@overload
def open_session(
    omc: SupportsInteractive[T_Calling],
    *,
    version: _1_18,
) -> v_1_18.GenericSession[T_Calling]:
    ...


# v1.17
@overload
def open_session(
    omc: str | PathLike[str] | None = None,
    *,
    version: _1_17,
    asyncio: Literal[False] = False,
) -> v_1_17.Session:
    ...


@overload
def open_session(
    omc: str | PathLike[str] | None = None,
    *,
    version: _1_17,
    asyncio: Literal[True],
) -> v_1_17.AsyncSession:
    ...


@overload
def open_session(
    omc: SupportsInteractive[T_Calling],
    *,
    version: _1_17,
) -> v_1_17.GenericSession[T_Calling]:
    ...


# v1.16
@overload
def open_session(
    omc: str | PathLike[str] | None = None,
    *,
    version: _1_16,
    asyncio: Literal[False] = False,
) -> v_1_16.Session:
    ...


@overload
def open_session(
    omc: str | PathLike[str] | None = None,
    *,
    version: _1_16,
    asyncio: Literal[True],
) -> v_1_16.AsyncSession:
    ...


@overload
def open_session(
    omc: SupportsInteractive[T_Calling],
    *,
    version: _1_16,
) -> v_1_16.GenericSession[T_Calling]:
    ...


# v1.15
@overload
def open_session(
    omc: str | PathLike[str] | None = None,
    *,
    version: _1_15,
    asyncio: Literal[False] = False,
) -> v_1_15.Session:
    ...


@overload
def open_session(
    omc: str | PathLike[str] | None = None,
    *,
    version: _1_15,
    asyncio: Literal[True],
) -> v_1_15.AsyncSession:
    ...


@overload
def open_session(
    omc: SupportsInteractive[T_Calling],
    *,
    version: _1_15,
) -> v_1_15.GenericSession[T_Calling]:
    ...


# v1.14
@overload
def open_session(
    omc: str | PathLike[str] | None = None,
    *,
    version: _1_14,
    asyncio: Literal[False] = False,
) -> v_1_14.Session:
    ...


@overload
def open_session(
    omc: str | PathLike[str] | None = None,
    *,
    version: _1_14,
    asyncio: Literal[True],
) -> v_1_14.AsyncSession:
    ...


@overload
def open_session(
    omc: SupportsInteractive[T_Calling],
    *,
    version: _1_14,
) -> v_1_14.GenericSession[T_Calling]:
    ...


# v1.13
@overload
def open_session(
    omc: str | PathLike[str] | None = None,
    *,
    version: _1_13,
    asyncio: Literal[False] = False,
) -> v_1_13.Session:
    ...


@overload
def open_session(
    omc: str | PathLike[str] | None = None,
    *,
    version: _1_13,
    asyncio: Literal[True],
) -> v_1_13.AsyncSession:
    ...


@overload
def open_session(
    omc: SupportsInteractive[T_Calling],
    *,
    version: _1_13,
) -> v_1_13.GenericSession[T_Calling]:
    ...


# Default
@overload
def open_session(
    omc: str | PathLike[str] | None = None,
    *,
    version: None = None,
    asyncio: Literal[False] = False,
) -> Session:
    ...


@overload
def open_session(
    omc: str | PathLike[str] | None = None,
    *,
    version: None = None,
    asyncio: Literal[True],
) -> AsyncSession:
    ...


@overload
def open_session(
    omc: SupportsInteractive[T_Calling],
    *,
    version: None = None,
) -> GenericSession[T_Calling]:
    ...


def open_session(
    omc: str | PathLike[str] | SupportsInteractive[T_Calling] | None = None,
    *,
    version: Tuple[int, int] | None = None,
    asyncio: bool = False,
) -> Any:
    interactive: SupportsInteractive[Synchronous] | SupportsInteractive[
        Asynchronous
    ]
    if isinstance(omc, SupportsInteractive):
        interactive = omc
    elif not asyncio:
        interactive = Interactive.open(omc, Calling.synchronous)
    else:
        interactive = Interactive.open(omc, Calling.asynchronous)

    try:
        session_type, async_session_type = _select_session_type(
            _get_version(interactive.synchronous)
        )
    except Exception:
        if interactive is not omc:
            interactive.close()
        raise

    if interactive.calling is Calling.synchronous:
        return session_type(interactive)
    else:
        return async_session_type(interactive)


def _get_version(
    interactive: SupportsInteractive[Synchronous],
) -> Tuple[int, int]:
    version = interactive.evaluate("getVersion()")
    matched = re.search(r"(\d+)\.(\d+)", version)
    if matched is None:
        raise OMCRuntimeError(f"Invalid version string {version!r}")
    major, minor = tuple(map(int, matched.groups()))
    return major, minor
