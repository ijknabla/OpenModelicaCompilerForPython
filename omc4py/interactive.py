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
from dataclasses import dataclass, field
from glob import glob
from os import PathLike
from pathlib import Path
from subprocess import DEVNULL, PIPE, Popen
from typing import TYPE_CHECKING, Any, Generic, NewType, TypeVar, overload

import zmq.asyncio

from .protocol import (
    Asynchronous,
    Synchronous,
    T_Calling,
    asynchronous,
    synchronous,
)

if TYPE_CHECKING:
    from typing_extensions import ParamSpec, Self

    P = ParamSpec("P")
    T = TypeVar("T")

    Process = Popen[str]
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
            return cls(
                exit_stack,
                exit_stack.enter_context(_DualInteractive.open(omc)),
                calling,
            )

        except Exception:
            exit_stack.close()
            raise

    def __enter__(self) -> Self:
        return closing(self).__enter__()

    def __exit__(self, *exc_info: Any) -> None:
        return closing(self).__exit__(*exc_info)

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
    process: Process
    lock: Lock = field(default_factory=Lock)

    @classmethod
    @contextmanager
    def open(cls, omc: Path) -> Generator[Self, None, None]:
        with ExitStack() as stack:
            enter = stack.enter_context

            process, port = enter(_create_omc_interactive(omc))

            yield cls(
                *enter(cls.__open_socket(process=process, port=port)),
                process,
                Lock(),
            )

    @staticmethod
    @contextmanager
    def __open_socket(
        process: Process, port: str
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
    omc: Path,
    user: str | None = None,
) -> Generator[tuple[Process, Port], None, None]:
    with ExitStack() as stack:
        suffix = str(uuid.uuid4())

        command = [
            omc.__fspath__(),
            "--interactive=zmq",
            "--locale=C",
            f"-z={suffix}",
        ]
        if user is not None and sys.version_info <= (3, 8):
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

        yield process, port


def _popen(*command: str, user: str | None = None) -> Process:
    if user is None:
        return Popen(command, stdout=PIPE, stderr=DEVNULL, encoding="utf-8")
    else:
        return Popen(
            command, stdout=PIPE, stderr=DEVNULL, encoding="utf-8", user=user
        )


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
