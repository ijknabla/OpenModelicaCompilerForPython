__all__ = ("Session",)

from dataclasses import dataclass
from typing import Any, Awaitable, List, Union

from typing_extensions import Self

from ..openmodelica import Component, TypeName
from ..protocol import SupportsInteractive

@dataclass
class Session:
    __omc_interactive__: SupportsInteractive[Awaitable[str]]

    def close(self) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, *exc_info: Any) -> None: ...
    async def getComponents(
        self, name: Union[TypeName, str]
    ) -> List[Component]: ...
