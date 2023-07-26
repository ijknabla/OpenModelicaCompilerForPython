from __future__ import annotations

import sys
from asyncio import run
from collections.abc import Callable, Coroutine, Sequence
from functools import wraps
from pathlib import Path
from typing import IO, Any, TypeVar

import click
import yaml
from typing_extensions import ParamSpec

from .interface import create_interface, create_interface_by_docker

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


@main.command()
@click.option("-i", "--image", type=str, required=True)
@click.option("-n", type=int, default=1)
@click.option(
    "-o",
    "--output-dir",
    type=click.Path(
        exists=True, file_okay=False, dir_okay=True, path_type=Path
    ),
    default=Path("."),
)
@click.option(
    "--pip-cache-dir",
    type=click.Path(
        exists=True, file_okay=False, dir_okay=True, path_type=Path
    ),
)
@click.argument(
    "tag",
    type=str,
    nargs=-1,
)
@run_decorator
async def interface_docker(
    image: str,
    tag: Sequence[str],
    n: int,
    output_dir: Path,
    pip_cache_dir: Path | None,
) -> None:
    await create_interface_by_docker(
        image=[f"{image}:{t}" for t in tag],
        n=n,
        output_dir=output_dir,
        pip_cache_dir=pip_cache_dir,
    )


if __name__ == "__main__":
    main()
