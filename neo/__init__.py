from __future__ import annotations

__all__ = ("TypeName", "VariableName")
from os import PathLike
from typing import TYPE_CHECKING, Any, Union, overload

from typing_extensions import Literal

from omc4py.compiler import OMCInteractive

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
    from . import latest

    return latest.Session(OMCInteractive.open(omc_command))
