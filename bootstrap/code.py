from __future__ import annotations

import sys

if sys.version_info < (3, 10):
    raise ImportError(
        f"python=={sys.version_info.major}.{sys.version_info.minor}"
        " not supported!"
    )

import ast
import enum
import os

# import re
from asyncio import create_subprocess_exec, gather
from collections.abc import Generator
from contextlib import AsyncExitStack
from dataclasses import dataclass, field
from itertools import chain
from operator import attrgetter
from pathlib import Path
from typing import Literal

from omc4py import TypeName, VariableName

from .interface import (
    Entities,
    Entity,
    EnumerationEntity,
    InputOutput,
    Interface,
    PackageEntity,
)
from .parser import get_enumerators
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
    for typename, entity in entities.items():
        if isinstance(entity, PackageEntity):
            factories[typename] = PackageFactory(typename=typename)
        elif isinstance(entity, EnumerationEntity):
            factories[typename] = EnumerationFactory(
                typename=typename, entity=entity
            )

    root = PackageFactory(typename=TypeName())
    factories[root.typename] = root

    for typename, child in factories.items():
        for parent in (
            factories.get(i) for i in typename.parents if i != typename
        ):
            if isinstance(parent, PackageFactory):
                parent.children[typename] = child
                break

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

    @property
    def is_root(self) -> bool:
        return self.typename == TypeName()

    @property
    def name(self) -> str:
        return f"{self.typename.last_identifier}"


@dataclass
class PackageFactory(HasTypeName):
    children: dict[TypeName, Factory] = field(default_factory=dict)

    @property
    def name(self) -> str:
        if self.is_root:
            return "GenericSession"
        else:
            return super().name

    async def save_module(self, directory: Path) -> None:
        path = Path(directory, *self.typename.parts, "__init__.py")
        os.makedirs(path.parent, exist_ok=True)
        with path.open("w", encoding="utf-8") as o:
            print(ast.unparse(self._get_module()), file=o)

        await self._lint_python_code(path)

    def _get_module(self) -> ast.Module:
        return ast.Module(
            body=[
                *map(attrgetter("stmt"), self._iter_module_imports()),
                *self._iter_module_stmts(),
            ],
            type_ignores=[],
        )

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

    def _iter_module_imports(self) -> Generator[ImportFrom, None, None]:
        yield ImportFrom(module="__future__", name="annotations", asname="_")

        imports = set(
            chain.from_iterable(
                child.iter_imports() for child in self.children.values()
            )
        )
        if self.is_root:
            imports.update(
                ImportFrom(module="omc4py.protocol", name=typevar)
                for typevar in ["Asynchronous", "Synchronous"]
            )
            imports.add(
                ImportFrom(module="omc4py.openmodelica2", name="BasicSession")
            )
        for child in self.children.values():
            if isinstance(child, PackageFactory) and child.children:
                imports.add(
                    ImportFrom(
                        name=child.name,
                        asname=_to_camel_case(child.name),
                        level=1,
                    )
                )

        yield from imports

    def iter_imports(self) -> Generator[ImportFrom, None, None]:
        yield ImportFrom(module="omc4py.modelica2", name="package")
        yield ImportFrom(module="omc4py.openmodelica", name="TypeName")
        yield ImportFrom(module="omc4py.protocol", name="T_Calling")

    def _iter_module_stmts(self) -> Generator[ast.stmt, None, None]:
        for child in self.children.values():
            yield from child.iter_stmts()

        if self.is_root:
            yield from self.iter_stmts()
            for name, typevar in [
                ("Session", "Synchronous"),
                ("AsyncSession", "Asynchronous"),
            ]:
                yield ast.Assign(
                    targets=[ast.Name(id=name, ctx=ast.Store())],
                    value=ast.Subscript(
                        value=ast.Name(id="GenericSession", ctx=ast.Load()),
                        slice=ast.Name(id=typevar, ctx=ast.Load()),
                        ctx=ast.Load(),
                    ),
                    lineno=None,
                )

    def iter_stmts(self) -> Generator[ast.stmt, None, None]:
        yield self._class_def

    @property
    def _class_def(self) -> ast.ClassDef:
        return ast.ClassDef(
            name=self.name,
            bases=[
                ast.Subscript(
                    value=ast.Name(
                        id="BasicSession" if self.is_root else "package",
                        ctx=ast.Load(),
                    ),
                    slice=ast.Name(id="T_Calling", ctx=ast.Load()),
                    ctx=ast.Load(),
                )
            ],
            keywords=[],
            body=[*self._iter_class_def_body()],
            decorator_list=[],
        )

    def _iter_class_def_body(self) -> Generator[ast.stmt, None, None]:
        if not self.is_root:
            yield ast.Assign(
                targets=[ast.Name(id="__omc_class__", ctx=ast.Store())],
                value=ast.Call(
                    func=ast.Name(id="TypeName", ctx=ast.Load()),
                    args=[
                        ast.Constant(value=f"{self.typename.as_absolute()}")
                    ],
                    keywords=[],
                ),
                lineno=None,
            )

        for child in self.children.values():
            if self.is_root:
                parts = [child.name]
            else:
                parts = [_to_camel_case(self.name), child.name]

            reference: ast.expr
            reference = ast.Name(id=parts[0], ctx=ast.Load())
            for part in parts[1:]:
                reference = ast.Attribute(
                    value=reference,
                    attr=part,
                    ctx=ast.Load(),
                )

            if isinstance(child, PackageFactory):
                yield ast.FunctionDef(
                    name=child.name,
                    args=ast.arguments(
                        posonlyargs=[],
                        args=[ast.arg(arg="self")],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        ast.Return(
                            value=ast.Call(
                                func=reference,
                                args=[
                                    ast.Attribute(
                                        value=ast.Name(
                                            id="self", ctx=ast.Load()
                                        ),
                                        attr="__omc_interactive__",
                                        ctx=ast.Load(),
                                    )
                                ],
                                keywords=[],
                            )
                        )
                    ],
                    decorator_list=[ast.Name(id="property", ctx=ast.Load())],
                    returns=ast.Subscript(
                        value=reference,
                        slice=ast.Name(id="T_Calling", ctx=ast.Load()),
                        ctx=ast.Load(),
                    ),
                    lineno=None,
                )
            else:
                yield ast.Assign(
                    targets=[ast.Name(id=child.name, ctx=ast.Store())],
                    value=reference,
                    lineno=None,
                )


@dataclass
class EnumerationFactory(HasTypeName):
    entity: EnumerationEntity

    def iter_imports(self) -> Generator[ImportFrom, None, None]:
        yield ImportFrom(module="omc4py.modelica", name="enumeration")
        yield ImportFrom(module="omc4py.openmodelica", name="TypeName")

    def iter_stmts(self) -> Generator[ast.stmt, None, None]:
        yield ast.ClassDef(
            name=self.name,
            bases=[ast.Name(id="enumeration", ctx=ast.Load())],
            keywords=[],
            body=[*self._iter_class_def_body()],
            decorator_list=[],
        )

    def _iter_class_def_body(self) -> Generator[ast.stmt, None, None]:
        yield ast.Expr(value=ast.Constant(value=_to_doc(self.entity.code)))
        yield ast.Assign(
            targets=[ast.Name(id="__omc_class__", ctx=ast.Store())],
            value=ast.Call(
                func=ast.Name(id="TypeName", ctx=ast.Load()),
                args=[ast.Constant(value=f"{self.typename.as_absolute()}")],
                keywords=[],
            ),
            lineno=None,
        )
        for value, (name, comment) in enumerate(
            get_enumerators(self.entity.code), start=1
        ):
            yield ast.Assign(
                targets=[ast.Name(id=f"{name}", ctx=ast.Store())],
                value=ast.Constant(value=value),
                lineno=None,
            )
            if comment is not None:
                yield ast.Expr(value=ast.Constant(value=comment))


Factory = PackageFactory | EnumerationFactory


@dataclass(frozen=True)
class ImportFrom:
    name: str
    module: str | None = None
    asname: str | None = None
    level: Literal[0, 1] = 0

    @property
    def stmt(self) -> ast.ImportFrom:
        return ast.ImportFrom(
            module=self.module,
            names=[ast.alias(name=self.name, asname=self.asname)],
            level=self.level,
        )


class TypeKind(enum.Enum):
    real = enum.auto()
    integer = enum.auto()
    boolean = enum.auto()
    string = enum.auto()
    # path = enum.auto()
    typename = enum.auto()
    variablename = enum.auto()

    @classmethod
    def resolve(
        cls,
        variablename: VariableName,
        typename: TypeName,
        entity: Entity | None,
    ) -> TypeKind:
        # path_pattern = re.compile(
        #     r"(file|header|dir|directory|(?<!modelica)path)(name|names)?$",
        #     re.IGNORECASE,
        # )
        match f"{typename}", entity:
            case "Real", None:
                return TypeKind.real
            case "Integer", None:
                return TypeKind.integer
            case "Boolean", None:
                return TypeKind.boolean
            case "String", None:
                return TypeKind.string
                # if path_pattern.search(f"{variablename}") is None:
                #     return TypeKind.string
                # else:
                #     return TypeKind.path
            case (
                "OpenModelica.$Code.TypeName" | "OpenModelica.$Code.TypeNames"
            ), None:
                return TypeKind.typename
            case (
                "OpenModelica.$Code.VariableName"
                | "OpenModelica.$Code.VariableNames"
            ), None:
                return TypeKind.variablename

        raise ValueError(typename, entity)


@dataclass
class BuiltinTypeHint:
    kind: TypeKind
    input_output: InputOutput

    def iter_imports(self) -> Generator[ImportFrom, None, None]:
        match self.kind, self.input_output:
            # case (TypeKind.path, "input"):
            #     yield ImportFrom(module="typing", name="Union")
            #     yield ImportFrom(module="omc4py.protocol", name="PathLike")
            case (TypeKind.typename, _):
                yield ImportFrom(module="omc4py.openmodelica", name="TypeName")
                if self.input_output == "input":
                    ImportFrom(module="typing", name="Union")
            case (TypeKind.variablename, _):
                yield ImportFrom(
                    module="omc4py.openmodelica", name="VariableName"
                )
                if self.input_output == "input":
                    ImportFrom(module="typing", name="Union")

    @property
    def annotation(self) -> ast.expr:
        match self.kind, self.input_output:
            case (TypeKind.real, _):
                return ast.Name(id="float", ctx=ast.Load())
            case (TypeKind.integer, _):
                return ast.Name(id="int", ctx=ast.Load())
            case (TypeKind.boolean, _):
                return ast.Name(id="bool", ctx=ast.Load())
            case (
                (TypeKind.string, _)
                # | (
                #     TypeKind.path,
                #     "output" | "unspecified",
                # )
            ):
                return ast.Name(id="str", ctx=ast.Load())
            # case (TypeKind.path, "input"):
            #     return ast.Subscript(
            #         value=ast.Name(id="Union", ctx=ast.Load()),
            #         slice=ast.Tuple(
            #             elts=[
            #                 ast.Name(id="PathLike", ctx=ast.Load()),
            #                 ast.Name(id="str", ctx=ast.Load()),
            #             ],
            #             ctx=ast.Load(),
            #         ),
            #         ctx=ast.Load(),
            #     )
            case (TypeKind.typename, "input"):
                return ast.Subscript(
                    value=ast.Name(id="Union", ctx=ast.Load()),
                    slice=ast.Tuple(
                        elts=[
                            ast.Name(id="TypeName", ctx=ast.Load()),
                            ast.Name(id="str", ctx=ast.Load()),
                        ],
                        ctx=ast.Load(),
                    ),
                    ctx=ast.Load(),
                )
            case (TypeKind.typename, _):
                return ast.Name(id="TypeName", ctx=ast.Load())
            case (TypeKind.variablename, "input"):
                return ast.Subscript(
                    value=ast.Name(id="Union", ctx=ast.Load()),
                    slice=ast.Tuple(
                        elts=[
                            ast.Name(id="VariableName", ctx=ast.Load()),
                            ast.Name(id="str", ctx=ast.Load()),
                        ],
                        ctx=ast.Load(),
                    ),
                    ctx=ast.Load(),
                )
            case (TypeKind.variablename, _):
                return ast.Name(id="VariableName", ctx=ast.Load())

        raise NotImplementedError(self)


@dataclass
class EnumerationTypeHint(HasTypeName):
    input_output: InputOutput
    entity: EnumerationEntity

    def iter_imports(self) -> Generator[ImportFrom, None, None]:
        match self.input_output:
            case "input":
                yield ImportFrom(module="typing", name="Literal")
                yield ImportFrom(module="typing", name="Union")

    @property
    def annotation(self) -> ast.expr:
        match self.input_output:
            case "input":
                return ast.Subscript(
                    value=ast.Name(id="Union", ctx=ast.Load()),
                    slice=ast.Tuple(
                        elts=[
                            ast.Name(
                                id=self.name,
                                ctx=ast.Load(),
                            ),
                            ast.Subscript(
                                value=ast.Name(id="Literal", ctx=ast.Load()),
                                slice=ast.Tuple(
                                    elts=[
                                        ast.Constant(value=f"{value}")
                                        for value, _ in get_enumerators(
                                            self.entity.code
                                        )
                                    ],
                                    ctx=ast.Load(),
                                ),
                                ctx=ast.Load(),
                            ),
                        ],
                        ctx=ast.Load(),
                    ),
                    ctx=ast.Load(),
                )
            case _:
                return ast.Name(id=self.name, ctx=ast.Load())


@dataclass
class AliasTypeHint(HasTypeName):
    input_output: InputOutput

    def iter_imports(self) -> Generator[ImportFrom, None, None]:
        yield from []

    @property
    def annotation(self) -> ast.expr:
        return ast.Name(id=self.name, ctx=ast.Load())


TypeHint = BuiltinTypeHint | EnumerationTypeHint | AliasTypeHint


def _to_camel_case(s: str) -> str:
    return s[:1].lower() + s[1:]


def _to_doc(code: str) -> str:
    return "\n".join(
        [
            "",
            ".. code-block:: modelica",
            "",
            *(f"    {line}" for line in code.splitlines(keepends=False)),
        ]
    )
