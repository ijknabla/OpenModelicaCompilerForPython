import sys

if sys.version_info < (3, 10):
    raise ImportError(
        f"python=={sys.version_info.major}.{sys.version_info.minor}"
        " not supported!"
    )

from ast import Module
from asyncio import FIRST_COMPLETED, get_running_loop, wait
from collections.abc import AsyncGenerator
from concurrent.futures import ProcessPoolExecutor
from pathlib import PurePath

from .interface import Entities, Interface, VersionString


async def create_code(
    interface: Interface,
) -> AsyncGenerator[tuple[PurePath, Module], None]:
    loop = get_running_loop()
    with ProcessPoolExecutor() as executor:
        pending = set(
            loop.run_in_executor(executor, _create_interface, v, e)
            for v, e in interface.items()
        )
        while pending:
            done, pending = await wait(pending, return_when=FIRST_COMPLETED)
            for future in done:
                for item in future.result():
                    yield item


def _create_interface(
    version: VersionString, entities: Entities
) -> list[tuple[PurePath, Module]]:
    return []
