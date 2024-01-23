from __future__ import annotations as _

from typing import Coroutine, Union, overload

from omc4py.modelica import enumeration, external, package
from omc4py.openmodelica import TypeName
from omc4py.protocol import (
    Asynchronous,
    SupportsInteractiveProperty,
    Synchronous,
    T_Calling,
)

from . import Time as time


class Time(package[T_Calling]):
    __omc_class__ = TypeName("OpenModelica.Scripting.Internal.Time")
    readableTime = time.readableTime
    timerTick = time.timerTick
    timerTock = time.timerTock
    timerClear = time.timerClear


class FileType(enumeration):
    """
    .. code-block:: modelica

        type FileType = enumeration(NoFile, RegularFile, Directory, SpecialFile);
    """

    __omc_class__ = TypeName("OpenModelica.Scripting.Internal.FileType")
    NoFile = 1
    RegularFile = 2
    Directory = 3
    SpecialFile = 4


@overload
def stat(
    self: SupportsInteractiveProperty[Synchronous], name: str
) -> FileType:
    ...


@overload
async def stat(
    self: SupportsInteractiveProperty[Asynchronous], name: str
) -> FileType:
    ...


@external("OpenModelica.Scripting.Internal.stat")
def stat(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    name: str,
) -> Union[FileType, Coroutine[None, None, FileType]]:
    """
    .. code-block:: modelica

        function stat
          input String name;
          output FileType fileType;
        end stat;"""
    return ...  # type: ignore
