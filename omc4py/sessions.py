
import shutil
from pathlib import Path


class OMCSessionBase:
    pass


class AsyncOMCSessionBase(
    OMCSessionBase,
):
    pass


def find_omc_executable() -> Path:
    omc_executable_ = shutil.which("omc")
    if omc_executable_ is not None:
        return Path(shutil.which("omc"))
    else:
        raise RuntimeError(
            "Can't find executable 'omc'"
        )


class AsyncOMCSessionZMQ(
    AsyncOMCSessionBase,
):
    pass

    @classmethod
    def create(
        cls
    ):
        return cls()

    async def hello_world(self):
        print("hello_world!")

    async def __aenter__(self):
        omc_executable = find_omc_executable()
        print(omc_executable)
        return self

    async def __aexit__(
        self,
        exception_type,
        exception,
        traceback,
    ):
        pass
