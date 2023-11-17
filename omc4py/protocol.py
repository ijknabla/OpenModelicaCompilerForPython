from __future__ import annotations

import enum
from collections.abc import Hashable
from dataclasses import InitVar, dataclass, field
from typing import (
    Generic,
    Literal,
    Protocol,
    TypeVar,
    overload,
    runtime_checkable,
)


@runtime_checkable
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
        self: SupportsInteractive[Synchronous], expression: str
    ) -> str:
        ...

    @overload
    async def evaluate(
        self: SupportsInteractive[Asynchronous], expression: str
    ) -> str:
        ...


@runtime_checkable
class SupportsInteractiveProperty(Protocol[T_Calling]):
    @property
    def __omc_interactive__(self) -> SupportsInteractive[T_Calling]:
        ...


@dataclass(frozen=True)
class HasInteractive(Generic[T_Calling]):
    interactive: InitVar[SupportsInteractive[T_Calling]]
    __omc_interactive__: SupportsInteractive[T_Calling] = field(init=False)

    def __post_init__(
        self, interactive: SupportsInteractive[T_Calling]
    ) -> None:
        super().__setattr__("__omc_interactive__", interactive)
