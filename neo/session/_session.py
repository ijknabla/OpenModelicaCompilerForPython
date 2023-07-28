from __future__ import annotations

from contextlib import closing
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, List, Union

from omc4py.string import to_omc_literal

from ..openmodelica import Component, TypeName
from ..parser import cast, parse
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

    if TYPE_CHECKING:

        def getComponents(self, name: Union[TypeName, str]) -> List[Component]:
            ...

    else:

        def getComponents(self, name):
            expression = (
                f"getComponents({to_omc_literal(cast(TypeName, name))})"
            )
            literal = self.__omc_interactive__.evaluate(expression)
            if isinstance(literal, str):
                return parse(List[Component], literal)
            else:

                async def getComponents():
                    return parse(List[Component], await literal)

                return getComponents()
