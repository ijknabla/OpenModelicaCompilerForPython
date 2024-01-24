from __future__ import annotations

from contextlib import closing
from typing import TYPE_CHECKING, Any, Coroutine, List, Union, overload
from warnings import warn

from exceptiongroup import ExceptionGroup

from .algorithm import fmap
from .exception import OMCError, OMCWarning
from .modelica import external
from .openmodelica import Component, TypeName
from .protocol import Asynchronous, HasInteractive, Synchronous, T_Calling

if TYPE_CHECKING:
    from typing_extensions import Self

    from .v_1_23.OpenModelica.Scripting import (  # NOTE: update to latest
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
        if TYPE_CHECKING:
            cls = BasicSession[Synchronous]
        else:
            cls = type(self)
        return cls(self.__omc_interactive__.synchronous)

    @property
    def asynchronous(self) -> BasicSession[Asynchronous]:
        if TYPE_CHECKING:
            cls = BasicSession[Asynchronous]
        else:
            cls = type(self)
        return cls(self.__omc_interactive__.asynchronous)

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

    @external("getComponents")
    def getComponents(
        self: Union[BasicSession[Synchronous], BasicSession[Asynchronous]],
        name: Union[TypeName, str],
    ) -> Union[List[Component], Coroutine[None, None, List[Component]]]:
        return ...  # type: ignore

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
        return fmap(
            _check_messages,
            self.getMessagesStringInternal(),
        )

    __check__ = check


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
