from __future__ import annotations

from asyncio.subprocess import Process
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager


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
