from __future__ import annotations

import atexit
import logging
import platform
import re
import shutil
import sys
import tempfile
import uuid
from asyncio import Lock
from collections.abc import Coroutine, Generator
from contextlib import ExitStack, closing, contextmanager, suppress
from dataclasses import dataclass, field, replace
from glob import glob
from os import PathLike
from pathlib import Path
from subprocess import DEVNULL, PIPE, Popen
from typing import TYPE_CHECKING, Any, Generic, NewType, overload

import zmq.asyncio

from .protocol import Asynchronous, Calling, Synchronous, T_Calling

if TYPE_CHECKING:
    from typing_extensions import Self

    Process = Popen[str]
else:
    Process = ...

Port = NewType("Port", str)

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class Interactive(Generic[T_Calling]):
    calling: T_Calling
    exit_stack: ExitStack
    process: Process
    port: Port
    socket: zmq.Socket
    asyncio_socket: zmq.asyncio.Socket
    lock: Lock = field(default_factory=Lock)

    @classmethod
    def open(
        cls,
        omc: str | PathLike[str] | None,
        calling: T_Calling,
        user: str | None = None,
    ) -> Self:
        exit_stack = ExitStack()
        atexit.register(exit_stack.close)

        try:
            return cls(
                calling,
                exit_stack,
                *exit_stack.enter_context(
                    _open_process_and_socket(_resolve_omc(omc), user=user)
                ),
            )
        except Exception:
            exit_stack.close()
            raise

    def __enter__(self) -> Self:
        return closing(self).__enter__()

    def __exit__(self, *exc_info: Any) -> None:
        return closing(self).__exit__(*exc_info)

    def close(self) -> None:
        self.exit_stack.close()

    @property
    def synchronous(self) -> Interactive[Synchronous]:
        if TYPE_CHECKING:
            _self: Interactive[Synchronous]
        else:
            _self = self
        return replace(
            _self,
            calling=Calling.synchronous,
        )

    @property
    def asynchronous(self) -> Interactive[Asynchronous]:
        if TYPE_CHECKING:
            _self: Interactive[Asynchronous]
        else:
            _self = self
        return replace(
            _self,
            calling=Calling.asynchronous,
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
        if self.calling is Calling.synchronous:
            return self.__synchronous_evaluate(expression)
        else:
            return self.__asynchronous_evaluate(expression)

    def __synchronous_evaluate(self, expression: str) -> str:
        socket = self.socket
        logger.debug(f"(pid={self.process.pid}) >>> {expression}")
        socket.send_string(expression)
        result = socket.recv_string()
        logger.debug(f"(pid={self.process.pid}) {result}")
        return result

    async def __asynchronous_evaluate(self, expression: str) -> str:
        socket = self.asyncio_socket
        async with self.lock:
            logger.debug(f"(pid={self.process.pid}) >>> {expression}")
            await socket.send_string(expression)
            result = await socket.recv_string()
            logger.debug(f"(pid={self.process.pid}) {result}")
        return result


def _resolve_omc(
    omc: str | PathLike[str] | None,
) -> str:
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
    return resolved


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


@contextmanager
def _open_process_and_socket(
    omc: str,
    user: str | None = None,
) -> Generator[
    tuple[Process, Port, zmq.Socket, zmq.asyncio.Socket], None, None
]:
    with ExitStack() as stack:
        suffix = str(uuid.uuid4())

        command = [
            omc,
            "--interactive=zmq",
            "--locale=C",
            f"-z={suffix}",
        ]
        if user is not None and sys.version_info < (3, 9):
            process = _popen("sudo", "-u", user, *command)
        else:
            process = _popen(*command, user=user)

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

        stack.callback(
            lambda: logger.info(f"(pid={process.pid}) Close zmq sokcet")
        )
        socket, asyncio_socket = (
            stack.enter_context(_open_socket(zmq.Context(), port)),
            stack.enter_context(_open_socket(zmq.asyncio.Context(), port)),
        )

        yield process, port, socket, asyncio_socket


def _popen(*command: str, user: str | None = None) -> Process:
    if user is None:
        return Popen(command, stdout=PIPE, stderr=DEVNULL, encoding="utf-8")
    else:
        return Popen(
            command, stdout=PIPE, stderr=DEVNULL, encoding="utf-8", user=user
        )


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
def _open_socket(
    context: zmq.Context, port: Port
) -> Generator[zmq.Socket, None, None]:
    ...


@overload
@contextmanager
def _open_socket(
    context: zmq.asyncio.Context, port: Port
) -> Generator[zmq.asyncio.Socket, None, None]:
    ...


@contextmanager
def _open_socket(
    context: zmq.Context | zmq.asyncio.Context, port: Port
) -> Generator[zmq.Socket | zmq.asyncio.Socket, None, None]:
    with context.socket(zmq.REQ) as socket:
        socket.connect(port)
        yield socket


@contextmanager
def _terminating(
    process: Process,
) -> Generator[Process, None, None]:
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
