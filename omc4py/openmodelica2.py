from __future__ import annotations

from collections.abc import Coroutine
from contextlib import closing
from functools import partial
from typing import TYPE_CHECKING, Any, List, Union, overload

if TYPE_CHECKING:
    from typing_extensions import Self

from .algorithm import bind_to_awaitable
from .openmodelica import Component, TypeName
from .parser import cast, parse
from .protocol import Asynchronous, HasInteractive, Synchronous, T_Calling
from .session._session import _check_messages
from .string import to_omc_literal


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
