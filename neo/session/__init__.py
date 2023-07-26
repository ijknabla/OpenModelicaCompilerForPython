from __future__ import annotations

from contextlib import closing
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

from ..protocol import SupportsInteractive

if TYPE_CHECKING:
    from typing_extensions import Self


@dataclass
class Session:
    __omc_interactive__: SupportsInteractive[str]

    def close(self) -> None:
        self.__omc_interactive__.close()

    def __enter__(self) -> Self:
        return closing(self).__enter__()

    def __exit__(self, *exc_info: Any) -> None:
        return closing(self).__exit__()
