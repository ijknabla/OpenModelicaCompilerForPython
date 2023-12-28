from __future__ import annotations

from asyncio import (
    FIRST_COMPLETED,
    CancelledError,
    Event,
    Queue,
    Task,
    create_task,
    wait,
)
from asyncio.subprocess import Process
from collections.abc import AsyncGenerator, AsyncIterator
from contextlib import AsyncExitStack, asynccontextmanager, suppress
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path
from typing import TYPE_CHECKING, Generic, TypeVar

if TYPE_CHECKING:
    from importlib.resources import as_file, files
else:
    from importlib_resources import as_file, files

_T = TypeVar("_T")


@dataclass(frozen=True)
class QueueingIteration(Generic[_T]):
    _queue: Queue[_T] = field(default_factory=Queue)
    _put_done: Event = field(default_factory=Event)

    async def put(self, item: _T) -> None:
        await self._queue.put(item)

    def put_done(self) -> None:
        self._put_done.set()

    async def __aiter__(self) -> AsyncIterator[_T]:
        async with AsyncExitStack() as stack:
            enter = stack.enter_async_context
            stop_task = await enter(
                ensure_cancel(create_task(self.__wait_stop()))
            )

            while True:
                get_task = await enter(
                    ensure_cancel(create_task(self._queue.get()))
                )
                done, _ = await wait(
                    {get_task, stop_task}, return_when=FIRST_COMPLETED
                )
                if get_task in done:
                    self._queue.task_done()
                    yield get_task.result()
                else:
                    break

    async def __wait_stop(self) -> None:
        await self._put_done.wait()
        await self._queue.join()


@asynccontextmanager
async def ensure_cancel(task: Task[_T]) -> AsyncGenerator[Task[_T], None]:
    try:
        yield task
    finally:
        task.cancel()
        with suppress(CancelledError):
            await task


@asynccontextmanager
async def ensure_terminate(
    process: Process,
) -> AsyncGenerator[Process, None]:
    try:
        yield process
    finally:
        if process.returncode is None:
            process.terminate()
        await process.wait()


@lru_cache
def get_root() -> Path:
    with as_file(files(__name__)) as child0:
        return child0.parents[0].resolve()
