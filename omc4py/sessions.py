
import shutil
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


class AsyncOMCSessionZMQ(
    AsyncOMCSessionBase,
):
    process: asyncio.subprocess.Process

    @classmethod
    def create(
        cls
    ):
        return cls()

    async def hello_world(self):
        print("hello_world!")

    async def __aenter__(self):
        omc_executable = find_omc_executable()
        self.process = await asyncio.create_subprocess_exec(
            str(omc_executable),
            "--interactive=zmq",
        )
        context = zmq.asyncio.Context()
        socket = context.socket(zmq.REQ)
        socket.setsockopt(zmq.LINGER, 0)  # Dismisses pending messages if closed
        print(socket)
        print(omc_executable)
        return self

    async def __aexit__(
        self,
        exception_type,
        exception,
        traceback,
    ):
        if self.process.returncode is None:
            # process still running
            self.process.terminate()
            returncode = await self.process.wait()  # drop returncode
            print(f"process terminated {returncode}")
