from __future__ import annotations

from collections.abc import Awaitable, Callable, Coroutine
from functools import wraps
from typing import Any, TypeVar

T_a = TypeVar("T_a")
T_b = TypeVar("T_b")


def bind_to_awaitable(
    f: Callable[[T_a], T_b]
) -> (
    Callable[[T_a], T_b] | Callable[[Awaitable[T_a]], Coroutine[Any, Any, T_b]]
):
    @wraps(f)
    def wrapped(x: T_a | Awaitable[T_a]) -> T_b | Coroutine[Any, Any, T_b]:
        if isinstance(x, Awaitable):

            @wraps(f)
            async def bind(x: Awaitable[T_a]) -> T_b:
                return f(await x)

            return bind(x)
        else:
            return f(x)

    return wrapped  # type: ignore
