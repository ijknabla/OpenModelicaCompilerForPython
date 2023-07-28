from __future__ import annotations

import logging
from asyncio import Lock
from collections.abc import Callable
from dataclasses import dataclass

import zmq

logger = logging.getLogger(__name__)


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
