import sys

if sys.version_info < (3, 10):
    raise ImportError(
        f"python=={sys.version_info.major}.{sys.version_info.minor}"
        " not supported!"
    )

import ast
import os
from asyncio import create_subprocess_exec, gather
from contextlib import AsyncExitStack
from dataclasses import dataclass
from pathlib import Path

from omc4py import TypeName

from .interface import Entities, Interface
from .util import ensure_terminate


async def save_code(
    directory: Path,
    interface: Interface,
) -> None:
    await gather(
        *(
            _save_code(
                directory / f"v_{version.major}_{version.minor}", entities
            )
            for version, entities in interface.items()
        )
    )


async def _save_code(directory: Path, entities: Entities) -> None:
    factories = dict[TypeName, Factory]()

    root = PackageFactory(typename=TypeName())
    factories[root.typename] = root

    await gather(
        *(
            factory.save_module(directory)
            for factory in factories.values()
            if isinstance(factory, PackageFactory)
        )
    )


@dataclass
class HasTypeName:
    typename: TypeName


@dataclass
class PackageFactory(HasTypeName):
    async def save_module(self, directory: Path) -> None:
        path = Path(directory, *self.typename.parts, "__init__.py")
        os.makedirs(path.parent, exist_ok=True)
        with path.open("w", encoding="utf-8") as o:
            print(ast.unparse(self._get_module()), file=o)

        await self._lint_python_code(path)

    def _get_module(self) -> ast.Module:
        return ast.Module(body=[], type_ignores=[])

    @staticmethod
    async def _lint_python_code(path: Path) -> None:
        async with AsyncExitStack() as stack:
            isort = await stack.enter_async_context(
                ensure_terminate(
                    await create_subprocess_exec("isort", f"{path}")
                )
            )
            await isort.wait()

            black = await stack.enter_async_context(
                ensure_terminate(
                    await create_subprocess_exec("black", f"{path}")
                )
            )
            await black.wait()


Factory = PackageFactory
