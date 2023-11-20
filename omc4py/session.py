from __future__ import annotations

from collections.abc import Coroutine
from contextlib import closing
from functools import partial
from typing import TYPE_CHECKING, Any, List, Union, overload
from warnings import warn

from exceptiongroup import ExceptionGroup

from .algorithm import bind_to_awaitable
from .exception import OMCError, OMCWarning
from .openmodelica import Component, TypeName
from .parser import cast, parse
from .protocol import Asynchronous, HasInteractive, Synchronous, T_Calling
from .string import to_omc_literal

if TYPE_CHECKING:
    from typing_extensions import Self

    from .v_1_21.OpenModelica.Scripting import (  # NOTE: update to latest
        ErrorMessage,
    )


class BasicSession(HasInteractive[T_Calling]):
    def close(self) -> None:
        self.__omc_interactive__.close()

    __close__ = close

    def __enter__(self) -> Self:
        return closing(self).__enter__()

    def __exit__(self, *exc_info: Any) -> None:
        return closing(self).__exit__()

    @property
    def synchronous(self) -> BasicSession[Synchronous]:
        return type(self)(
            self.__omc_interactive__.synchronous,  # type: ignore
        )

    @property
    def asynchronous(self) -> BasicSession[Asynchronous]:
        return type(self)(
            self.__omc_interactive__.asynchronous,  # type: ignore
        )

    @overload
    def getComponents(
        self: BasicSession[Synchronous],
        name: Union[TypeName, str],
    ) -> List[Component]:
        ...

    @overload
    async def getComponents(
        self: BasicSession[Asynchronous],
        name: Union[TypeName, str],
    ) -> List[Component]:
        ...

    def getComponents(
        self: BasicSession[Synchronous] | BasicSession[Asynchronous],
        name: Union[TypeName, str],
    ) -> List[Component] | Coroutine[None, None, List[Component]]:
        expression = f"getComponents({to_omc_literal(cast(TypeName, name))})"
        literal = self.__omc_interactive__.evaluate(expression)
        bound_parse = bind_to_awaitable(partial(parse, List[Component]))
        return bound_parse(literal)  # type: ignore

    @overload
    def getMessagesStringInternal(
        self: BasicSession[Synchronous],
        unique: Union[bool, None] = None,
    ) -> List[Any]:
        ...

    @overload
    async def getMessagesStringInternal(
        self: BasicSession[Asynchronous],
        unique: Union[bool, None] = None,
    ) -> List[Any]:
        ...

    def getMessagesStringInternal(
        self: BasicSession[Asynchronous],
        unique: Union[bool, None] = None,
    ) -> List[Any] | Coroutine[None, None, List[Any]]:
        raise NotImplementedError()

    @overload
    def check(self: BasicSession[Synchronous]) -> None:
        ...

    @overload
    async def check(self: BasicSession[Asynchronous]) -> None:
        ...

    def check(self) -> None | Coroutine[None, None, None]:
        return _check_messages(
            self.getMessagesStringInternal(),  # type: ignore
        )

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
