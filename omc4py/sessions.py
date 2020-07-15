
import typing
import sys
import uuid
import shutil
import tempfile
from getpass import getuser
from pathlib import Path
import asyncio
import zmq
import zmq.asyncio


class OMCSessionBase:
    pass


class AsyncOMCSessionBase(
    OMCSessionBase,
):
    pass


def find_omc_executable() -> Path:
    omc_executable_ = shutil.which("omc")
    if omc_executable_ is not None:
        return Path(omc_executable_)
    else:
        raise RuntimeError(
            "Can't find executable 'omc'"
        )


async def find_omc_zmq_port_file(
    tmp_dir: Path,
    suffix: str,
    timeout: float,
) -> Path:
    if timeout <= 0.0:
        raise ValueError(
            f"timeout must be positive, got {timeout}"
        )

    name: str
    if sys.platform == "win32":
        name = f"openmodelica.port.{suffix}"
    else:
        username = getuser()
        name = f"openmodelica.{username}.port.{suffix}"

    async def task() -> Path:
        path = (tmp_dir / name).resolve()
        while True:
            if path.exists():
                return path

    return await asyncio.wait_for(
        task(),
        timeout
    )


def random_string() -> str:
    return uuid.uuid4().hex


async def read_omc_port_file(
    tmp_dir: Path,
    suffix: str,
    timeout: float
) -> str:
    omc_port_file_path = await find_omc_zmq_port_file(
        tmp_dir, suffix, timeout
    )
    return omc_port_file_path.read_text()


class AsyncOMCSessionZMQ(
    AsyncOMCSessionBase,
):
    process: asyncio.subprocess.Process
    socket: zmq.asyncio.Socket

    @classmethod
    def create(
        cls
    ):
        return cls()

    async def hello_world(self):
        print("hello_world!")

    async def __aenter__(self):
        omc_executable = find_omc_executable()
        suffix = random_string()
        self.process = await asyncio.create_subprocess_exec(
            str(omc_executable),
            "--interactive=zmq",
            f"--zeroMQFileSuffix={suffix}",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )

        context = zmq.asyncio.Context()
        self.socket = context.socket(zmq.REQ)
        self.socket.setsockopt(zmq.LINGER, 0)  # Dismisses pending messages if closed

        url = await read_omc_port_file(
            Path(tempfile.gettempdir()),
            suffix,
            1.0
        )
        self.socket.connect(url)

        return self

    async def evaluate(
        self,
        expression: str,
        timeout: typing.Optional[float] = None,
    ) -> typing.List[str]:
        if not expression.endswith("\n"):
            expression += "\n"
        await self.socket.send(expression.encode("utf-8"))
        msgs = await asyncio.wait_for(
            self.socket.recv_multipart(),
            timeout=timeout,
        )
        return [
            msg.decode("utf-8")
            for msg in msgs
        ]

    async def __aexit__(
        self,
        exception_type,
        exception,
        traceback,
    ):
        await self.evaluate("quit()")
        await self.process.wait()
        if self.process.returncode is None:
            # process still running
            self.process.terminate()
            returncode = await self.process.wait()  # drop returncode
            print(f"process terminated {returncode}")
