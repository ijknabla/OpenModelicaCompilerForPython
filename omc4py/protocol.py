from __future__ import annotations

import enum
from collections.abc import Hashable
from typing import (
    TYPE_CHECKING,
    Literal,
    Protocol,
    TypeVar,
    overload,
    runtime_checkable,
)

if TYPE_CHECKING:
    from typing_extensions import TypeAlias
else:
    TypeAlias = ...


class SupportsClose(Protocol):
    def close(self) -> None:
        ...


@runtime_checkable
class SupportsToOMCLiteral(Protocol):
    def __to_omc_literal__(self) -> str:
        ...


class Calling(enum.Enum):
    synchronous = enum.auto()
    asynchronous = enum.auto()


Synchronous = Literal[Calling.synchronous]
Asynchronous = Literal[Calling.asynchronous]

synchronous: Synchronous = Calling.synchronous
asynchronous: Asynchronous = Calling.asynchronous

T_Calling = TypeVar(
    "T_Calling",
    Synchronous,
    Asynchronous,
    covariant=True,
)


@runtime_checkable
class SupportsInteractive(SupportsClose, Hashable, Protocol[T_Calling]):
    @overload
    def evaluate(
        self: SupportsInteractive[Synchronous],
        expression: str,
    ) -> str:
        ...

    @overload
    async def evaluate(
        self: SupportsInteractive[Asynchronous],
        expression: str,
    ) -> str:
        ...


SupportsAnyInteractive: TypeAlias = (
    "SupportsInteractive[Synchronous] | SupportsInteractive[Asynchronous]"
)


@runtime_checkable
class SupportsInteractiveProperty(Protocol[T_Calling]):
    @property
    def __omc_interactive__(self) -> SupportsInteractive[T_Calling]:
        ...
