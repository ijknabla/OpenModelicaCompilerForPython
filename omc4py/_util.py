from __future__ import annotations

from collections.abc import Generator
from contextlib import contextmanager, suppress
from pathlib import Path
from subprocess import Popen
from typing import AnyStr


@contextmanager
def terminating(
    process: Popen[AnyStr],
) -> Generator[Popen[AnyStr], None, None]:
    try:
        yield process
    finally:
        process.terminate()
        process.wait()


@contextmanager
def unlinking(path: Path) -> Generator[Path, None, None]:
    try:
        yield path
    finally:
        with suppress(FileNotFoundError):
            path.unlink()
