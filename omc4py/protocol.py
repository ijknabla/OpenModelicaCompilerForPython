from __future__ import annotations

from collections.abc import Hashable
from typing import TYPE_CHECKING, Awaitable, TypeVar

from typing_extensions import Protocol, runtime_checkable

_T_evaluate = TypeVar("_T_evaluate", str, Awaitable[str], covariant=True)


class SupportsClose(Protocol):
    def close(self) -> None:
        ...


@runtime_checkable
class SupportsInteractive(SupportsClose, Hashable, Protocol[_T_evaluate]):
    def evaluate(self, expression: str) -> _T_evaluate:
        ...


if TYPE_CHECKING:
    SupportsAnyInteractive = (
        SupportsInteractive[str] | SupportsInteractive[Awaitable[str]]
    )
else:
    SupportsAnyInteractive = ...


@runtime_checkable
class SupportsInteractiveProperty(Protocol[_T_evaluate]):
    @property
    def __omc_interactive__(self) -> SupportsInteractive[_T_evaluate]:
        ...


@runtime_checkable
class SupportsToOMCLiteral(Protocol):
    def __to_omc_literal__(self) -> str:
        ...
