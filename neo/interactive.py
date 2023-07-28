from __future__ import annotations

import atexit
import logging
from asyncio import Lock
from collections.abc import Callable
from contextlib import ExitStack
from dataclasses import dataclass
from os import PathLike

import zmq.asyncio

from omc4py.compiler import _create_omc_interactive

logger = logging.getLogger(__name__)


def open_interactives(
    omc_command: str | PathLike[str],
) -> tuple[Interactive, AsyncInteractive]:
    stack = ExitStack()
    atexit.register(stack.close)

    try:
        process, port = stack.enter_context(
            _create_omc_interactive(omc_command)
        )
        pid = process.pid

        stack.callback(lambda: logger.info(f"(pid={pid}) Close zmq sokcet"))

        socket = stack.enter_context(zmq.Context().socket(zmq.REQ))
        socket.connect(port)
        async_socket = stack.enter_context(
            zmq.asyncio.Context().socket(zmq.REQ)
        )
        async_socket.connect(port)
        logger.info(f"(pid={pid}) Connect zmq sokcet via {port}")

        lock = Lock()

        return (
            Interactive(stack.close, pid, socket),
            AsyncInteractive(stack.close, pid, async_socket, lock),
        )

    except Exception:
        stack.close()
        raise


@dataclass(frozen=True)
class Interactive:
    close: Callable[[], None]
    pid: int
    socket: zmq.Socket

    def evaluate(self, expression: str) -> str:
        logger.debug(f"(pid={self.pid}) >>> {expression}")
        self.socket.send_string(expression)
        result = self.socket.recv_string()
        logger.debug(f"(pid={self.pid}) {result}")
        return result


@dataclass(frozen=True)
class AsyncInteractive:
    close: Callable[[], None]
    pid: int
    socket: zmq.asyncio.Socket
    lock: Lock

    async def evaluate(self, expression: str) -> str:
        async with self.lock:
            logger.debug(f"(pid={self.pid}) >>> {expression}")
            await self.socket.send_string(expression)
            result = await self.socket.recv_string()
            logger.debug(f"(pid={self.pid}) {result}")
        return result
