from __future__ import annotations

import argparse
import asyncio
import logging
from collections.abc import Iterable
from contextlib import suppress
from subprocess import CalledProcessError, run

from omc4py import AsyncSession, open_session
from omc4py.interactive import Interactive
from omc4py.protocol import Calling


async def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--user", type=str, default=None)

    args = parser.parse_args()

    user: str | None = args.user

    with open_session(
        Interactive.open(omc=None, calling=Calling.asynchronous, user=user)
    ) as session:
        assert await ensure_package(
            session, "Modelica", ("4.0.0", "3.2.3", "3.2.2")
        )
        assert await session.loadModel("Modelica")


async def ensure_package(
    session: AsyncSession,
    pkg: str,
    versions: Iterable[str],
) -> bool:
    if hasattr(session, "installPackage") and await session.installPackage(
        pkg
    ):
        return True

    run(["apt", "update"], check=True)
    for version in versions:
        with suppress(CalledProcessError):
            run(
                [
                    "apt",
                    "install",
                    "-qy",
                    f"omlib-{pkg.lower()}-{version}",
                ],
                check=True,
            )
            return True

    return False


if __name__ == "__main__":
    logging.root.setLevel(logging.DEBUG)
    logging.getLogger("omc4py").addHandler(logging.StreamHandler())

    asyncio.run(main())
