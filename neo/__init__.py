from __future__ import annotations

__all__ = (
    "TypeName",
    "VariableName",
)
import re
from os import PathLike
from typing import TYPE_CHECKING, Any, Union, overload

from typing_extensions import Literal

import omc4py.exception

from . import session
from .interactive import open_interactives
from .openmodelica import TypeName, VariableName
from .protocol import SupportsInteractive

Command = Union[str, "PathLike[str]"]
if TYPE_CHECKING:
    from . import latest


def _select_session_type(
    version: tuple[int, int]
) -> tuple[type[session.Session], type[session.aio.Session]]:
    if version <= (1, 13):
        from . import v_1_13

        return v_1_13.Session, v_1_13.aio.Session
    elif version <= (1, 14):
        from . import v_1_14

        return v_1_14.Session, v_1_14.aio.Session
    elif version <= (1, 16):
        from . import v_1_16

        return v_1_16.Session, v_1_16.aio.Session
    elif version <= (1, 17):
        from . import v_1_17

        return v_1_17.Session, v_1_17.aio.Session
    elif version <= (1, 18):
        from . import v_1_18

        return v_1_18.Session, v_1_18.aio.Session
    elif version <= (1, 19):
        from . import v_1_19

        return v_1_19.Session, v_1_19.aio.Session
    elif version <= (1, 20):
        from . import v_1_20

        return v_1_20.Session, v_1_20.aio.Session
    elif version <= (1, 21):
        from . import v_1_21

        return v_1_21.Session, v_1_21.aio.Session
    else:
        from . import latest

        return latest.Session, latest.aio.Session


@overload
def open_session(
    omc_command: Command | None = None,
    *,
    asyncio: Literal[False] = False,
) -> latest.Session:
    ...


@overload
def open_session(
    omc_command: Command | None = None,
    *,
    asyncio: Literal[True],
) -> latest.aio.Session:
    ...


def open_session(
    omc_command: Command | None = None,
    *,
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
