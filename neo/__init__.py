from __future__ import annotations

__all__ = ("TypeName", "VariableName")
from os import PathLike
from typing import Any, Union, overload

from typing_extensions import Literal

from omc4py.compiler import OMCInteractive

from . import v_1_21 as latest
from .openmodelica import TypeName, VariableName

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
    return latest.Session(OMCInteractive.open(omc_command))
