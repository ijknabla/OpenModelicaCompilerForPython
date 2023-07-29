from __future__ import annotations

from collections.abc import Awaitable, Callable, Coroutine
from functools import wraps
from typing import Any, TypeVar

_T_1 = TypeVar("_T_1")
_T_2 = TypeVar("_T_2")


def bind_to_awaitable(
    f: Callable[[_T_1], _T_2]
) -> (
    Callable[[_T_1], _T_2]
    | Callable[[Awaitable[_T_1]], Coroutine[Any, Any, _T_2]]
):
    @wraps(f)
    def wrapped(x: _T_1 | Awaitable[_T_1]) -> _T_2 | Coroutine[Any, Any, _T_2]:
        if isinstance(x, Awaitable):

            @wraps(f)
            async def bind(x: Awaitable[_T_1]) -> _T_2:
                return f(await x)

            return bind(x)
        else:
            return f(x)

    return wrapped  # type: ignore
