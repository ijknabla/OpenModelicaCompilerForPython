import sys

if sys.version_info < (3, 10):
    raise ImportError(
        f"python=={sys.version_info.major}.{sys.version_info.minor}"
        " not supported!"
    )

from pathlib import Path

from .interface import Interface


async def save_code(
    directory: Path,
    interface: Interface,
) -> None:
    return
