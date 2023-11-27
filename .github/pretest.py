import logging
from asyncio import run

from omc4py import open_session


async def main() -> None:
    with open_session(asyncio=True) as session:
        if not await session.loadModel("Modelica"):
            if hasattr(session, "installPackage"):
                await session.installPackage("Modelica")


if __name__ == "__main__":
    logging.root.setLevel(logging.DEBUG)
    logging.getLogger("omc4py").addHandler(logging.StreamHandler())

    run(main())
