from __future__ import annotations

__all__ = (
    "TypeName",
    "VariableName",
    "open_session",
)
import re
from os import PathLike
from typing import TYPE_CHECKING, Any, overload

from typing_extensions import Literal

import omc4py.exception

from . import session
from .interactive import open_interactives
from .openmodelica import TypeName, VariableName
from .protocol import SupportsInteractive

if TYPE_CHECKING:
    from . import (
        latest,
        v_1_13,
        v_1_14,
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
    Version__1_21 = tuple[Literal[1], Literal[21]] | Literal["1.21", "1_21"]
    Version__1_20 = tuple[Literal[1], Literal[20]] | Literal["1.20", "1_20"]
    Version__1_19 = tuple[Literal[1], Literal[19]] | Literal["1.19", "1_19"]
    Version__1_18 = tuple[Literal[1], Literal[18]] | Literal["1.18", "1_18"]
    Version__1_17 = tuple[Literal[1], Literal[17]] | Literal["1.17", "1_17"]
    Version__1_16 = tuple[Literal[1], Literal[16]] | Literal["1.16", "1_16"]
    Version__1_15 = tuple[Literal[1], Literal[15]] | Literal["1.15", "1_15"]
    Version__1_14 = tuple[Literal[1], Literal[14]] | Literal["1.14", "1_14"]
    Version__1_13 = tuple[Literal[1], Literal[13]] | Literal["1.13", "1_13"]
    Version__1_12 = tuple[Literal[1], Literal[12]] | Literal["1.12", "1_12"]
    Version__1_11 = tuple[Literal[1], Literal[11]] | Literal["1.11", "1_11"]
    Version__1_10 = tuple[Literal[1], Literal[10]] | Literal["1.10", "1_10"]
    Version__1_9 = tuple[Literal[1], Literal[9]] | Literal["1.9", "1_9"]
    Version__1_8 = tuple[Literal[1], Literal[8]] | Literal["1.8", "1_8"]
    Version__1_7 = tuple[Literal[1], Literal[7]] | Literal["1.7", "1_7"]
    Version__1_6 = tuple[Literal[1], Literal[6]] | Literal["1.6", "1_6"]
    Version__1_5 = tuple[Literal[1], Literal[5]] | Literal["1.5", "1_5"]
    Version__1_4 = tuple[Literal[1], Literal[4]] | Literal["1.4", "1_4"]
    Version__1_3 = tuple[Literal[1], Literal[3]] | Literal["1.3", "1_3"]
    Version__1_2 = tuple[Literal[1], Literal[2]] | Literal["1.2", "1_2"]
    Version__1_1 = tuple[Literal[1], Literal[1]] | Literal["1.1", "1_1"]
    Version__1_0 = tuple[Literal[1], Literal[0]] | Literal["1.0", "1_0"]
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


# v1.14
@overload
def open_session(
    omc_command: Command | None = None,
    *,
    version: Version__1_15 | Version__1_14,
    asyncio: Literal[False] = False,
) -> v_1_14.Session:
    ...


@overload
def open_session(
    omc_command: Command | None = None,
    *,
    version: Version__1_15 | Version__1_14,
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
    version: tuple[int, int] | str | None = None,
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


def _get_version(interactive: SupportsInteractive[str]) -> tuple[int, int]:
    version = interactive.evaluate("getVersion()")
    matched = re.search(r"(\d+)\.(\d+)", version)
    if matched is None:
        raise omc4py.exception.OMCRuntimeError(
            f"Invalid version string {version!r}"
        )
    return tuple(map(int, matched.groups()))  # type: ignore
