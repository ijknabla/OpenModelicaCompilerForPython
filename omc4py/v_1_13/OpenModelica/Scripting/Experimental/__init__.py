from __future__ import annotations as _

from typing import Coroutine, Sequence, Union, overload

from omc4py.modelica import external
from omc4py.protocol import (
    Asynchronous,
    PathLike,
    SupportsInteractiveProperty,
    Synchronous,
)


@overload
def relocateFunctions(
    self: SupportsInteractiveProperty[Synchronous],
    fileName: Union[PathLike[str], str],
    names: Sequence[Sequence[str]],
) -> bool:
    ...


@overload
async def relocateFunctions(
    self: SupportsInteractiveProperty[Asynchronous],
    fileName: Union[PathLike[str], str],
    names: Sequence[Sequence[str]],
) -> bool:
    ...


@external("OpenModelica.Scripting.Experimental.relocateFunctions")
def relocateFunctions(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    fileName: Union[PathLike[str], str],
    names: Sequence[Sequence[str]],
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function relocateFunctions
          input String fileName;
          input String names[:, 2];
          output Boolean success;
        end relocateFunctions;"""
    return ...  # type: ignore
