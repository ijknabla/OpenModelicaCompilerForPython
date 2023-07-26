from __future__ import annotations

import sys
from asyncio import run
from collections.abc import Callable, Coroutine
from functools import wraps
from typing import IO, Any, TypeVar

import click
import yaml
from typing_extensions import ParamSpec

from .interface import create_interface

_P = ParamSpec("_P")
_T = TypeVar("_T")


def run_decorator(
    f: Callable[_P, Coroutine[Any, Any, _T]]
) -> Callable[_P, _T]:
    @wraps(f)
    def wrapped(*args: _P.args, **kwargs: _P.kwargs) -> _T:
        return run(f(*args, **kwargs))

    return wrapped


@click.group()
def main() -> None:
    ...


@main.command()
@click.option("-n", type=int, default=1)
@click.option(
    "-o",
    type=click.File("w", encoding="utf-8", lazy=True),
    default=sys.stdout,
)
@run_decorator
async def interface(n: int, o: IO[str]) -> None:
    n = max(1, n)
    yaml.safe_dump(
        await create_interface(n),
        o,
        sort_keys=False,
    )


if __name__ == "__main__":
    main()
