import asyncio
import logging
from contextlib import suppress
from subprocess import CalledProcessError, run

from omc4py import AsyncSession, open_session


async def main() -> None:
    with open_session(asyncio=True) as session:
        assert await ensure_package(session, "Modelica", "3.2.2")
        assert await session.loadModel("Modelica")


async def ensure_package(
    session: AsyncSession,
    pkg: str,
    version: str,
) -> bool:
    with suppress(CalledProcessError):
        run(["sudo", "apt", "update"], check=True)
        run(
            [
                "sudo",
                "apt",
                "install",
                "-qy",
                f"omlib-{pkg.lower()}-{version}",
            ],
            check=True,
        )
        return True

    return await session.installPackage(
        pkg=pkg, version=version, exactMatch=True
    )


if __name__ == "__main__":
    logging.root.setLevel(logging.DEBUG)
    logging.getLogger("omc4py").addHandler(logging.StreamHandler())

    asyncio.run(main())
