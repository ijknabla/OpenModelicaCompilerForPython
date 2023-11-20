from __future__ import annotations

import atexit
import logging
import shutil
import tempfile
import uuid
from asyncio import Lock
from collections.abc import Coroutine, Generator
from contextlib import ExitStack, contextmanager, suppress
from dataclasses import dataclass, field
from os import PathLike
from pathlib import Path
from subprocess import DEVNULL, PIPE, Popen
from typing import TYPE_CHECKING, AnyStr, Generic, overload

import zmq.asyncio

from .protocol import (
    Asynchronous,
    Synchronous,
    T_Calling,
    asynchronous,
    synchronous,
)

if TYPE_CHECKING:
    from typing_extensions import Self

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class Interactive(Generic[T_Calling]):
    _exit_stack: ExitStack
    _dual_interactive: _DualInteractive
    calling: T_Calling

    @classmethod
    def open(
        cls,
        omc_command: str | PathLike[str],
        calling: T_Calling,
    ) -> Self:
        exit_stack = ExitStack()
        atexit.register(exit_stack.close)

        try:
            return cls(
                exit_stack,
                exit_stack.enter_context(_DualInteractive.open(omc_command)),
                calling,
            )

        except Exception:
            exit_stack.close()
            raise

    def close(self) -> None:
        self._exit_stack.close()

    @property
    def synchronous(
        self: Interactive[Asynchronous],
    ) -> Interactive[Synchronous]:
        return Interactive(
            _exit_stack=self._exit_stack,
            _dual_interactive=self._dual_interactive,
            calling=synchronous,
        )

    @property
    def asynchronous(self) -> Interactive[Asynchronous]:
        return Interactive(
            _exit_stack=self._exit_stack,
            _dual_interactive=self._dual_interactive,
            calling=asynchronous,
        )

    @overload
    def evaluate(
        self: Interactive[Synchronous],
        expression: str,
    ) -> str:
        ...

    @overload
    async def evaluate(
        self: Interactive[Asynchronous],
        expression: str,
    ) -> str:
        ...

    def evaluate(self, expression: str) -> str | Coroutine[None, None, str]:
        if self.calling is asynchronous:
            return self._dual_interactive.asynchronous_evaluate(expression)
        else:
            return self._dual_interactive.synchronous_evaluate(expression)


@dataclass(frozen=True)
class _DualInteractive:
    synchronous: zmq.Socket
    asynchronous: zmq.asyncio.Socket
    process: Popen[str]
    lock: Lock = field(default_factory=Lock)

    @classmethod
    @contextmanager
    def open(
        cls,
        omc_command: str | PathLike[str],
    ) -> Generator[Self, None, None]:
        with ExitStack() as stack:
            enter = stack.enter_context

            process, port = enter(_create_omc_interactive(omc_command))

            yield cls(
                *enter(cls.__open_socket(process=process, port=port)),
                process,
                Lock(),
            )

    @staticmethod
    @contextmanager
    def __open_socket(
        process: Popen[str], port: str
    ) -> Generator[tuple[zmq.Socket, zmq.asyncio.Socket], None, None]:
        try:
            with ExitStack() as stack:
                enter = stack.enter_context
                synchronous = enter(zmq.Context().socket(zmq.REQ))
                synchronous.connect(port)
                asynchronous = enter(zmq.asyncio.Context().socket(zmq.REQ))
                asynchronous.connect(port)

                logger.info(
                    f"(pid={process.pid}) Connect zmq sokcet via {port}"
                )
                yield synchronous, asynchronous
        finally:
            logger.info(f"(pid={process.pid}) Close zmq sokcet")

    def synchronous_evaluate(self, expression: str) -> str:
        socket = self.synchronous
        logger.debug(f"(pid={self.process.pid}) >>> {expression}")
        socket.send_string(expression)
        result = socket.recv_string()
        logger.debug(f"(pid={self.process.pid}) {result}")
        return result

    async def asynchronous_evaluate(self, expression: str) -> str:
        socket = self.asynchronous
        async with self.lock:
            logger.debug(f"(pid={self.process.pid}) >>> {expression}")
            await socket.send_string(expression)
            result = await socket.recv_string()
            logger.debug(f"(pid={self.process.pid}) {result}")
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
