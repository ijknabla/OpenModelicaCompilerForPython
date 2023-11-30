from __future__ import annotations

import atexit
import logging
import platform
import re
import shutil
import tempfile
import uuid
from asyncio import Lock
from collections.abc import Coroutine, Generator
from contextlib import ExitStack, contextmanager, suppress
from dataclasses import dataclass, field, replace
from glob import glob
from os import PathLike
from pathlib import Path
from subprocess import DEVNULL, PIPE, Popen
from typing import TYPE_CHECKING, AnyStr, Generic, Literal, NewType, overload

import zmq.asyncio

from .protocol import Asynchronous, Calling, Synchronous, T_Calling

if TYPE_CHECKING:
    from typing_extensions import Self

Port = NewType("Port", str)

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class Interactive(Generic[T_Calling]):
    _exit_stack: ExitStack
    _dual_interactive: _DualInteractive
    calling: T_Calling

    @classmethod
    def open(
        cls,
        omc: str | PathLike[str] | None,
        calling: T_Calling,
    ) -> Self:
        omc = _resolve_omc("omc" if omc is None else omc)

        exit_stack = ExitStack()
        atexit.register(exit_stack.close)

        try:
            process, _, socket, asyncio_socket = exit_stack.enter_context(
                _create_omc_interactive(omc)
            )

            return cls(
                exit_stack,
                _DualInteractive(
                    synchronous=socket,
                    asynchronous=asyncio_socket,
                    process=process,
                ),
                calling,
            )

        except Exception:
            exit_stack.close()
            raise

    def close(self) -> None:
        self._exit_stack.close()

    @property
    def synchronous(self) -> Interactive[Synchronous]:
        if TYPE_CHECKING:
            synchronous: Interactive[Synchronous]
        else:
            synchronous = self
        return replace(synchronous, calling=Calling.synchronous)

    @property
    def asynchronous(self) -> Interactive[Asynchronous]:
        if TYPE_CHECKING:
            asynchronous: Interactive[Asynchronous]
        else:
            asynchronous = self
        return replace(asynchronous, calling=Calling.asynchronous)

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
        if self.calling is Calling.asynchronous:
            return self._dual_interactive.asynchronous_evaluate(expression)
        else:
            return self._dual_interactive.synchronous_evaluate(expression)


@dataclass(frozen=True)
class _DualInteractive:
    synchronous: zmq.Socket
    asynchronous: zmq.asyncio.Socket
    process: Popen[str]
    lock: Lock = field(default_factory=Lock)

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
    omc: Path,
) -> Generator[
    tuple[Popen[str], Port, zmq.Socket, zmq.asyncio.Socket], None, None
]:
    with ExitStack() as stack:
        suffix = str(uuid.uuid4())

        command = [
            omc.__fspath__(),
            "--interactive=zmq",
            "--locale=C",
            f"-z={suffix}",
        ]

        process = Popen(command, stdout=PIPE, stderr=DEVNULL, encoding="utf-8")
        logger.info(f"(pid={process.pid}) Start omc :: {' '.join(command)}")

        stack.callback(lambda: logger.info(f"(pid={process.pid}) Stop omc"))
        stack.enter_context(_terminating(process))

        assert process.stdout is not None
        first_line = process.stdout.readline()
        logger.debug(f"(pid={process.pid}) >>> {first_line}")

        with _unlinking(
            _find_openmodelica_zmq_port_filepath(suffix)
        ) as port_filepath:
            logger.info(
                f"(pid={process.pid}) Find zmq port file at {port_filepath}"
            )
            port = Port(port_filepath.read_text())
        logger.info(
            f"(pid={process.pid}) Remove zmq port file at {port_filepath}"
        )

        socket, asyncio_socket = (
            stack.enter_context(_open_zmq_socket(port, False)),
            stack.enter_context(_open_zmq_socket(port, True)),
        )
        logger.info(f"(pid={process.pid}) Connect zmq sokcet via {port}")
        stack.callback(
            lambda: logger.info(f"(pid={process.pid}) Close zmq sokcet")
        )

        yield process, port, socket, asyncio_socket


def _resolve_omc(
    omc: str | PathLike[str] | None,
) -> Path:
    if isinstance(omc, PathLike):
        omc = omc.__fspath__()
    elif omc is None:
        omc = "omc"

    resolved = shutil.which(omc)
    if resolved is None and platform.system() == "Windows":
        resolved = max(
            glob("C:\\Program Files\\OpenModelica*\\bin\\omc.exe"),
            key=_search_openmodelica_version,
            default=None,
        )

    if resolved is None:
        raise FileNotFoundError(f"Can't find executable of {omc}")
    return Path(resolved)


def _search_openmodelica_version(s: str | None) -> tuple[int, int, int]:
    major, minor, patch = -1, -1, -1

    if s is not None:
        matched = re.search(
            "OpenModelica"
            r"(?P<major>\d+)(\.(?P<minor>\d+)(\.(?P<patch>\d+))?)?",
            s,
        )
        if matched is not None:
            major = int(matched.group("major"))
            with suppress(TypeError):
                minor = int(matched.group("minor"))
            with suppress(TypeError):
                patch = int(matched.group("patch"))

    return major, minor, patch


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


@overload
@contextmanager
def _open_zmq_socket(
    port: Port, asyncio: Literal[False]
) -> Generator[zmq.Socket, None, None]:
    ...


@overload
@contextmanager
def _open_zmq_socket(
    port: Port, asyncio: Literal[True]
) -> Generator[zmq.asyncio.Socket, None, None]:
    ...


@contextmanager
def _open_zmq_socket(
    port: Port, asyncio: bool
) -> Generator[zmq.Socket | zmq.asyncio.Socket, None, None]:
    context: zmq.Context | zmq.asyncio.Context
    if asyncio:
        context = zmq.asyncio.Context()
    else:
        context = zmq.Context()
    with context.socket(zmq.REQ) as socket:
        socket.connect(port)
        yield socket


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
