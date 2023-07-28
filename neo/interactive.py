from __future__ import annotations

import atexit
import logging
import shutil
import tempfile
import uuid
from asyncio import Lock
from collections.abc import Callable, Generator
from contextlib import ExitStack, contextmanager, suppress
from dataclasses import dataclass
from os import PathLike
from pathlib import Path
from subprocess import DEVNULL, PIPE, Popen
from typing import AnyStr

import zmq.asyncio

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


@contextmanager
def _create_omc_interactive(
    omc_command: str | PathLike[str],
) -> Generator[tuple[Popen[str], str], None, None]:
    with ExitStack() as stack:
        suffix = str(uuid.uuid4())

        command = [
            f"{_resolve_command(omc_command)}",
            "--interactive=zmq",
            "--locale=C",
            f"-z={suffix}",
        ]

        stack.callback(lambda: logger.info(f"(pid={process.pid}) Stop omc"))
        process: Popen[str] = stack.enter_context(
            _terminating(
                Popen(command, stdout=PIPE, stderr=DEVNULL, encoding="utf-8")
            )
        )
        assert process.stdout is not None
        logger.info(f"(pid={process.pid}) Start omc :: {' '.join(command)}")

        first_line = process.stdout.readline()
        logger.debug(f"(pid={process.pid}) >>> {first_line}")

        with _unlinking(
            _find_openmodelica_zmq_port_filepath(suffix)
        ) as port_filepath:
            logger.info(
                f"(pid={process.pid}) Find zmq port file at {port_filepath}"
            )
            port = port_filepath.read_text()
        logger.info(
            f"(pid={process.pid}) Remove zmq port file at {port_filepath}"
        )

        yield process, port


def _resolve_command(
    command: str | PathLike[str],
) -> Path:
    executable = shutil.which(command)
    if executable is None:
        raise FileNotFoundError(f"Can't find executable of {command}")

    return Path(executable).resolve()


def _find_openmodelica_zmq_port_filepath(suffix: str | None) -> Path:
    temp_dir = Path(tempfile.gettempdir())

    pattern_of_name = "openmodelica*.port"
    if suffix is not None:
        pattern_of_name += f".{suffix}"

    candidates = tuple(temp_dir.glob(pattern_of_name))

    if not candidates:
        raise ValueError(
            f"Can't find openmodelica port file " f"at {temp_dir}"
        )
    elif len(candidates) >= 2:
        raise ValueError(
            f"Ambiguous openmodelica port file {candidates}" f"at {temp_dir}"
        )

    return candidates[0]


@contextmanager
def _terminating(
    process: Popen[AnyStr],
) -> Generator[Popen[AnyStr], None, None]:
    try:
        yield process
    finally:
        process.terminate()
        process.wait()


@contextmanager
def _unlinking(path: Path) -> Generator[Path, None, None]:
    try:
        yield path
    finally:
        with suppress(FileNotFoundError):
            path.unlink()
