from __future__ import annotations

from asyncio import CancelledError, Task
from asyncio.subprocess import Process
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager, suppress
from typing import TypeVar

_T = TypeVar("_T")


@asynccontextmanager
async def aterminating(
    process: Process,
) -> AsyncGenerator[Process, None]:
    try:
        yield process
    finally:
        if process.returncode is None:
            process.terminate()
        await process.wait()


@asynccontextmanager
async def ensure_cancel(task: Task[_T]) -> AsyncGenerator[Task[_T], None]:
    try:
        yield task
    finally:
        task.cancel()
        with suppress(CancelledError):
            await task
