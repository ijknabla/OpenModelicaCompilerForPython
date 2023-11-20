from __future__ import annotations

from collections.abc import Callable, Coroutine
from typing import TypeVar

T_a = TypeVar("T_a")
T_b = TypeVar("T_b")


def fmap(
    f: Callable[[T_a], T_b], a: T_a | Coroutine[None, None, T_a]
) -> T_b | Coroutine[None, None, T_b]:
    if isinstance(a, Coroutine):
        return _fmap(f, a)
    else:
        return f(a)


async def _fmap(f: Callable[[T_a], T_b], a: Coroutine[None, None, T_a]) -> T_b:
    return f(await a)
