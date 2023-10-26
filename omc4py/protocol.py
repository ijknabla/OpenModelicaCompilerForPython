from __future__ import annotations

import enum
from collections.abc import Hashable
from typing import (
    Any,
    Coroutine,
    Literal,
    Protocol,
    TypeVar,
    Union,
    runtime_checkable,
)

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
