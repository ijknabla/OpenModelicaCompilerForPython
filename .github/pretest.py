import asyncio
import logging
from subprocess import CalledProcessError, run

from omc4py import open_session


async def main() -> None:
    with open_session(asyncio=True) as session:
        if not await session.loadModel("Modelica"):
            if hasattr(session, "installPackage"):
                await session.installPackage("Modelica")
        if not await session.loadModel("Modelica"):
            run(["sudo", "apt", "update"], check=True)
            for version in ["4.0.0", "3.2.3", "3.2.2"]:
                try:
                    run(
                        [
                            "sudo",
                            "apt",
                            "install",
                            "-qy",
                            f"omlib-modelica-{version}",
                        ],
                        check=True,
                    )
                except CalledProcessError:
                    continue

        assert await session.loadModel("Modelica")


if __name__ == "__main__":
    logging.root.setLevel(logging.DEBUG)
    logging.getLogger("omc4py").addHandler(logging.StreamHandler())

    asyncio.run(main())
