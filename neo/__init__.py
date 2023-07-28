from __future__ import annotations

__all__ = ("TypeName", "VariableName")
from os import PathLike
from typing import TYPE_CHECKING, Any, Union, overload

from typing_extensions import Literal

from .interactive import open_interactives
from .openmodelica import TypeName, VariableName

if TYPE_CHECKING:
    from . import latest

Command = Union[str, "PathLike[str]"]


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

    from . import latest

    if asyncio:
        return latest.aio.Session(aio_interactive)
    else:
        return latest.Session(interactive)
