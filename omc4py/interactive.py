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
from contextlib import ExitStack, closing, contextmanager, suppress
from dataclasses import dataclass, replace
from glob import glob
from os import PathLike
from pathlib import Path
from subprocess import DEVNULL, PIPE, Popen
from typing import TYPE_CHECKING, Any, AnyStr, Generic, NewType, overload
from weakref import WeakKeyDictionary

import zmq.asyncio

from .protocol import Asynchronous, Calling, Synchronous, T_Calling

if TYPE_CHECKING:
    from typing_extensions import Self

Port = NewType("Port", str)

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class Interactive(Generic[T_Calling]):
    _exit_stack: ExitStack
    _resource: _Resource
    calling: T_Calling

    @classmethod
    def open(
        cls,
        omc: str | PathLike[str] | None,
        calling: T_Calling,
    ) -> Self:
        exit_stack = ExitStack()
        atexit.register(exit_stack.close)

        try:
            resource = exit_stack.enter_context(_Resource.open(omc))

            return cls(
                exit_stack,
                resource,
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
        if self.calling is Calling.synchronous:
            return self.__synchronous_evaluate(expression)
        else:
            return self.__asynchronous_evaluate(expression)

    def __synchronous_evaluate(self, expression: str) -> str:
        process = self._resource.process
        socket = self._resource.sockets.synchronous
        logger.debug(f"(pid={process.pid}) >>> {expression}")
        socket.send_string(expression)
        result = socket.recv_string()
        logger.debug(f"(pid={process.pid}) {result}")
        return result

    async def __asynchronous_evaluate(self, expression: str) -> str:
        process = self._resource.process
        socket = self._resource.sockets.asynchronous
        async with self._resource.lock:
            logger.debug(f"(pid={process.pid}) >>> {expression}")
            await socket.send_string(expression)
            result = await socket.recv_string()
            logger.debug(f"(pid={process.pid}) {result}")
        return result


_resource_locks: WeakKeyDictionary[_Resource, Lock] = WeakKeyDictionary()


@dataclass(frozen=True)
class _Resource:
    process: Popen[str]
    sockets: _Sockets

    @classmethod
    @contextmanager
    def open(
        cls,
        omc: str | PathLike[str] | None,
    ) -> Generator[Self, None, None]:
        with ExitStack() as stack:
            suffix = str(uuid.uuid4())

            command = [
                _resolve_omc(omc),
                "--interactive=zmq",
                "--locale=C",
                f"-z={suffix}",
            ]

            process = Popen(
                command, stdout=PIPE, stderr=DEVNULL, encoding="utf-8"
            )
            header = f"(pid={process.pid})"
            logger.info(f"{header} Start omc :: {' '.join(command)}")

            stack.callback(lambda: logger.info(f"{header} Stop omc"))
            stack.enter_context(_terminating(process))

            assert process.stdout is not None
            first_line = process.stdout.readline()
            logger.debug(f"{header} >>> {first_line}")

            with _unlinking(
                _find_openmodelica_zmq_port_filepath(suffix)
            ) as port_filepath:
                logger.info(f"{header} Find zmq port file at {port_filepath}")
                port = Port(port_filepath.read_text())
            logger.info(f"{header} Remove zmq port file at {port_filepath}")

            sockets = stack.enter_context(_Sockets.open(port))
            logger.info(f"{header} Connect zmq sokcet via {port}")
            stack.callback(lambda: logger.info(f"{header} Close zmq sokcet"))

            yield cls(process=process, sockets=sockets)

    @property
    def lock(self) -> Lock:
        if self not in _resource_locks:
            _resource_locks[self] = Lock()
        return _resource_locks[self]


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


@dataclass(frozen=True)
class _Sockets:
    synchronous: zmq.Socket
    asynchronous: zmq.asyncio.Socket

    @classmethod
    @contextmanager
    def open(cls, port: Port) -> Generator[Self, None, None]:
        synchronous = zmq.Context().socket(zmq.REQ)
        asynchronous = zmq.asyncio.Context().socket(zmq.REQ)
        with synchronous, asynchronous:
            synchronous.connect(port)
            asynchronous.connect(port)
            yield cls(synchronous=synchronous, asynchronous=asynchronous)


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
