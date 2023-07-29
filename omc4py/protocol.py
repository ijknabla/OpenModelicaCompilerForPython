from __future__ import annotations

from collections.abc import Hashable
from typing import Any, Coroutine, TypeVar, Union

from typing_extensions import Protocol, runtime_checkable

_T_evaluate = TypeVar(
    "_T_evaluate", str, Coroutine[Any, Any, str], covariant=True
)


class SupportsClose(Protocol):
    def close(self) -> None:
        ...


@runtime_checkable
class SupportsToOMCLiteral(Protocol):
    def __to_omc_literal__(self) -> str:
        ...


@runtime_checkable
class _GenericInteractiveProtocol(
    SupportsClose, Hashable, Protocol[_T_evaluate]
):
    def evaluate(self, expression: str) -> _T_evaluate:
        ...


SupportsInteractive = _GenericInteractiveProtocol[str]
SupportsAsyncInteractive = _GenericInteractiveProtocol[
    Coroutine[Any, Any, str]
]
SupportsAnyInteractive = Union[SupportsInteractive, SupportsAsyncInteractive]


@runtime_checkable
class SupportsInteractiveProperty(Protocol[_T_evaluate]):
    @property
    def __omc_interactive__(self) -> _GenericInteractiveProtocol[_T_evaluate]:
        ...
