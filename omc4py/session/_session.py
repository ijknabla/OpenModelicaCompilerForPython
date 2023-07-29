from __future__ import annotations

from contextlib import closing
from dataclasses import dataclass
from functools import partial
from typing import TYPE_CHECKING, Any, List, Union
from warnings import warn

from exceptiongroup import ExceptionGroup

from ..algorithm import bind_to_awaitable
from ..exception import OMCError, OMCWarning
from ..openmodelica import Component, TypeName
from ..parser import cast, parse
from ..protocol import SupportsInteractive
from ..string import to_omc_literal

if TYPE_CHECKING:
    from typing_extensions import Self, TypeAlias

    from ..v_1_21._interface import OpenModelica

    ErrorMessage: TypeAlias = OpenModelica.Scripting.ErrorMessage


@dataclass
class Session:
    __omc_interactive__: SupportsInteractive

    def close(self) -> None:
        self.__omc_interactive__.close()

    __close__ = close

    def __enter__(self) -> Self:
        return closing(self).__enter__()

    def __exit__(self, *exc_info: Any) -> None:
        return closing(self).__exit__()

    def getComponents(self, name: Union[TypeName, str]) -> List[Component]:
        expression = f"getComponents({to_omc_literal(cast(TypeName, name))})"
        literal = self.__omc_interactive__.evaluate(expression)
        bound_parse = bind_to_awaitable(partial(parse, List[Component]))
        return bound_parse(literal)  # type: ignore

    def check(self) -> None:
        messages: list[ErrorMessage]
        messages = getattr(
            self,
            "getMessagesStringInternal",
            lambda: [],
        )()  # type: ignore
        return _check_messages(messages)  # type: ignore

    __check__ = check


@bind_to_awaitable
def _check_messages(messages: list[ErrorMessage]) -> None:
    errors: list[OMCError] = []

    for record in messages:
        level = record.level.name
        kind = record.kind.name
        message = record.message

        args = (f"[level={level}, kind={kind}] {message}",)
        if level == "error":
            errors.append(OMCError(*args))
        else:
            warn(OMCWarning(*args))

    if len(errors) == 0:
        return
    elif len(errors) == 1:
        raise errors[0]
    else:
        raise ExceptionGroup("Multiple OMCErrors raised", errors)
