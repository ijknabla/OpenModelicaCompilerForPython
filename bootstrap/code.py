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
import re
from asyncio import create_subprocess_exec, gather
from collections.abc import Generator, Iterable
from contextlib import AsyncExitStack
from dataclasses import dataclass, field
from itertools import chain
from keyword import iskeyword
from operator import attrgetter
from pathlib import Path
from typing import TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from typing_extensions import Self

from omc4py import TypeName, VariableName

from .interface import (
    Entities,
    Entity,
    EnumerationEntity,
    FunctionEntity,
    InputOutput,
    Interface,
    PackageEntity,
    RecordEntity,
    Version,
)
from .parser import get_enumerators, get_optionals
from .util import ensure_terminate


async def save_code(
    directory: Path,
    interface: Interface,
) -> None:
    interface = patch(interface)
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
        elif isinstance(entity, RecordEntity):
            components = dict(Component.iter_from_entity(entity, entities))
            factories[typename] = RecordFactory(
                typename=typename, code=entity.code, components=components
            )
        elif isinstance(entity, FunctionEntity):
            try:
                components = dict(Component.iter_from_entity(entity, entities))
            except Exception:
                continue
            factories[typename] = FunctionFactory(
                typename=typename, code=entity.code, components=components
            )
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
            if isinstance(parent, (PackageFactory, RecordFactory)):
                parent.children[typename] = child
                break

        match typename.parts:
            case "OpenModelica", "Scripting", _ if isinstance(
                child, FunctionFactory
            ):
                root.children[typename] = AliasFactory(typename)

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
        return re.sub(r"^__", "_", f"{self.typename.last_identifier}")


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
            print(
                ast.unparse(self._get_module()).replace(
                    "__RETURN_TYPE_IGNORE__", "return ... # type: ignore"
                ),
                file=o,
            )

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
            imports.add(ImportFrom(module="typing", name="TYPE_CHECKING"))
            imports.update(
                ImportFrom(module="omc4py.protocol", name=typevar)
                for typevar in ["Asynchronous", "Synchronous"]
            )
            imports.add(
                ImportFrom(module="omc4py.session", name="BasicSession")
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
        yield ImportFrom(module="omc4py.modelica", name="package")
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
        body = list[ast.stmt]()
        if self.is_root:
            body.append(
                ast.If(
                    test=ast.Name(id="TYPE_CHECKING", ctx=ast.Load()),
                    body=[
                        ast.FunctionDef(
                            name=name,
                            args=ast.arguments(
                                posonlyargs=[],
                                args=[ast.arg(arg="self")],
                                kwonlyargs=[],
                                kw_defaults=[],
                                defaults=[],
                            ),
                            body=[
                                ast.Expr(
                                    value=ast.Name(
                                        id="__RETURN_TYPE_IGNORE__",
                                        ctx=ast.Load(),
                                    )
                                )
                            ],
                            decorator_list=[
                                ast.Name(id="property", ctx=ast.Load())
                            ],
                            returns=ast.Subscript(
                                value=ast.Name(
                                    id="GenericSession", ctx=ast.Load()
                                ),
                                slice=ast.Name(
                                    id=name.capitalize(), ctx=ast.Load()
                                ),
                                ctx=ast.Load(),
                            ),
                            lineno=None,
                        )
                        for name in ["synchronous", "asynchronous"]
                    ],
                    orelse=[],
                )
            )

        body += self._iter_class_def_body()

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
            body=body,
            decorator_list=[],
        )

    def _iter_class_def_body(self) -> Generator[ast.stmt, None, None]:
        if not self.is_root:
            yield ast.Assign(
                targets=[ast.Name(id="__omc_class__", ctx=ast.Store())],
                value=ast.Call(
                    func=ast.Name(id="TypeName", ctx=ast.Load()),
                    args=[
                        ast.Constant(value=f"{self.typename}")
                    ],
                    keywords=[],
                ),
                lineno=None,
            )

        for child in self.children.values():
            if isinstance(child, AliasFactory):
                i = len(self.typename.parts)
                parts = [
                    *map(_to_camel_case, child.typename.parts[i:-1]),
                    child.typename.parts[-1],
                ]
            else:
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
class RecordFactory(HasTypeName):
    code: str
    components: dict[VariableName, Component]
    children: dict[TypeName, Factory] = field(default_factory=dict, init=False)

    def iter_imports(self) -> Generator[ImportFrom, None, None]:
        yield ImportFrom(module="omc4py.modelica", name="record")
        yield ImportFrom(module="dataclasses", name="dataclass")

        for component in self.components.values():
            yield from component.iter_imports()

    def iter_stmts(self) -> Generator[ast.stmt, None, None]:
        yield ast.ClassDef(
            name=self.name,
            bases=[ast.Name(id="record", ctx=ast.Load())],
            keywords=[],
            body=[*self._iter_class_def_body()],
            decorator_list=[
                ast.Call(
                    func=ast.Name(id="dataclass", ctx=ast.Load()),
                    args=[],
                    keywords=[
                        ast.keyword(
                            arg="frozen", value=ast.Constant(value=True)
                        )
                    ],
                )
            ],
        )

    def _iter_class_def_body(self) -> Generator[ast.stmt, None, None]:
        yield ast.Expr(value=ast.Constant(value=_to_doc(self.code)))
        yield ast.Assign(
            targets=[ast.Name(id="__omc_class__", ctx=ast.Store())],
            value=ast.Call(
                func=ast.Name(id="TypeName", ctx=ast.Load()),
                args=[ast.Constant(value=f"{self.typename}")],
                keywords=[],
            ),
            lineno=None,
        )

        for variablename, component in self.components.items():
            yield ast.AnnAssign(
                target=ast.Name(id=f"{variablename}", ctx=ast.Store()),
                annotation=component.annotation,
                simple=1,
            )


@dataclass
class FunctionFactory(HasTypeName):
    code: str | None
    components: dict[VariableName, Component]

    @property
    def required_inputs(self) -> list[VariableName]:
        return [
            variablename
            for variablename, component in self.components.items()
            if component.input_output == "input" and not component.is_optional
        ]

    @property
    def optional_inputs(self) -> list[VariableName]:
        return [
            variablename
            for variablename, component in self.components.items()
            if component.input_output == "input" and component.is_optional
        ]

    @property
    def outputs(self) -> dict[VariableName, Component]:
        return {
            variablename: component
            for variablename, component in self.components.items()
            if component.input_output == "output"
        }

    def iter_imports(self) -> Generator[ImportFrom, None, None]:
        yield ImportFrom(module="omc4py.modelica", name="external")
        yield ImportFrom(module="omc4py.protocol", name="Asynchronous")
        yield ImportFrom(module="omc4py.protocol", name="Synchronous")
        yield ImportFrom(
            module="omc4py.protocol", name="SupportsInteractiveProperty"
        )
        match len(self.outputs):
            case 0 | 1:
                pass
            case _:
                yield ImportFrom(module="typing", name="NamedTuple")
        yield ImportFrom(module="typing", name="Coroutine")
        yield ImportFrom(module="typing", name="Union")
        yield ImportFrom(module="typing", name="overload")
        for component in self.components.values():
            yield from component.iter_imports()

    def iter_stmts(self) -> Generator[ast.stmt, None, None]:
        py_modelica = dict[str, str]()

        args = list[ast.arg]()
        for variablename in self.required_inputs + self.optional_inputs:
            component = self.components[variablename]
            modelica = f"{variablename}"
            py = _avoid_keyword(modelica)
            if py != modelica:
                py_modelica[py] = modelica
            match component.input_output:
                case "input":
                    args.append(
                        ast.arg(
                            arg=py,
                            annotation=component.annotation,
                        )
                    )

        basic_returns: ast.expr
        match len(self.outputs):
            case 0:
                basic_returns = ast.Constant(value=None)
            case 1:
                (component,) = self.outputs.values()
                basic_returns = component.annotation
            case _:
                yield ast.ClassDef(
                    name=self.name.capitalize(),
                    bases=[ast.Name(id="NamedTuple", ctx=ast.Load())],
                    keywords=[],
                    body=[
                        ast.AnnAssign(
                            target=ast.Name(
                                id=f"{variablename}", ctx=ast.Store()
                            ),
                            annotation=component.annotation,
                            simple=1,
                        )
                        for variablename, component in self.outputs.items()
                    ],
                    decorator_list=[],
                )
                basic_returns = ast.Name(
                    id=self.name.capitalize(), ctx=ast.Load()
                )

        defaults = [ast.Constant(value=None)] * len(self.optional_inputs)

        for mode in ("sync_overload", "async_overload", "impl"):
            function_def_type: (
                type[ast.FunctionDef] | type[ast.AsyncFunctionDef]
            )
            match mode:
                case "async_overload":
                    function_def_type = ast.AsyncFunctionDef
                case _:
                    function_def_type = ast.FunctionDef

            decorator_list: list[ast.expr]
            match mode:
                case "impl":
                    match self.typename.parts:
                        case "OpenModelica", "Scripting", name:
                            funcname = name
                        case _:
                            funcname = f"{self.typename.as_absolute()}"

                    decorator_list = [
                        ast.Call(
                            func=ast.Name(id="external", ctx=ast.Load()),
                            args=[ast.Constant(value=funcname)],
                            keywords=[],
                        )
                    ]
                case _:
                    decorator_list = [ast.Name(id="overload", ctx=ast.Load())]

            synchronous_self_annotation = ast.Subscript(
                value=ast.Name(
                    id="SupportsInteractiveProperty", ctx=ast.Load()
                ),
                slice=ast.Name(id="Synchronous", ctx=ast.Load()),
                ctx=ast.Load(),
            )
            asynchronous_self_annotation = ast.Subscript(
                value=ast.Name(
                    id="SupportsInteractiveProperty", ctx=ast.Load()
                ),
                slice=ast.Name(id="Asynchronous", ctx=ast.Load()),
                ctx=ast.Load(),
            )

            self_annotation: ast.expr
            match mode:
                case "sync_overload":
                    self_annotation = synchronous_self_annotation
                case "async_overload":
                    self_annotation = asynchronous_self_annotation
                case "impl":
                    self_annotation = ast.Subscript(
                        value=ast.Name(id="Union", ctx=ast.Load()),
                        slice=ast.Tuple(
                            elts=[
                                synchronous_self_annotation,
                                asynchronous_self_annotation,
                            ],
                            ctx=ast.Load(),
                        ),
                        ctx=ast.Load(),
                    )

            returns: ast.expr
            match mode:
                case "impl":
                    returns = ast.Subscript(
                        value=ast.Name(id="Union", ctx=ast.Load()),
                        slice=ast.Tuple(
                            elts=[
                                basic_returns,
                                ast.Subscript(
                                    value=ast.Name(
                                        id="Coroutine", ctx=ast.Load()
                                    ),
                                    slice=ast.Tuple(
                                        elts=[
                                            ast.Constant(value=None),
                                            ast.Constant(value=None),
                                            basic_returns,
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
                    returns = basic_returns

            body = list[ast.stmt]()
            match mode, self.code:
                case "impl", code if isinstance(code, str):
                    body.append(
                        ast.Expr(value=ast.Constant(value=_to_doc(code)))
                    )

            match mode, len(self.outputs):
                case "impl", 0:
                    pass
                case "impl", _:
                    body.append(
                        ast.Expr(
                            value=ast.Name(
                                id="__RETURN_TYPE_IGNORE__", ctx=ast.Load()
                            )
                        )
                    )

            if not body:
                body.append(ast.Expr(value=ast.Constant(value=Ellipsis)))

            yield function_def_type(
                name=self.name,
                args=ast.arguments(
                    posonlyargs=[],
                    args=[
                        ast.arg(
                            arg="self",
                            annotation=self_annotation,
                        ),
                        *args,
                    ],
                    kwonlyargs=[],
                    kw_defaults=[],
                    defaults=defaults,
                ),
                body=body,
                decorator_list=decorator_list,
                returns=returns,
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
                args=[ast.Constant(value=f"{self.typename}")],
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


class AliasFactory(HasTypeName):
    def iter_imports(self) -> Generator[ImportFrom, None, None]:
        yield from []

    def iter_stmts(self) -> Generator[ast.stmt, None, None]:
        yield from []


Factory = (
    PackageFactory
    | RecordFactory
    | FunctionFactory
    | EnumerationFactory
    | AliasFactory
)


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


@dataclass
class Component:
    type_hint: TypeHint
    ndim: int
    is_optional: bool

    @classmethod
    def iter_from_entity(
        cls,
        entity: RecordEntity | FunctionEntity,
        entities: Entities,
    ) -> Generator[tuple[VariableName, Self], None, None]:
        if entity.code is None:
            optionals = set[VariableName]()
        else:
            optionals = set(
                map(VariableName, get_optionals(entity.code))
            )  # TODO:

        for variablename, component in entity.components.items():
            typename = component.className
            component_entity = entities.get(typename)

            type_hint: TypeHint
            if isinstance(component_entity, EnumerationEntity):
                type_hint = EnumerationTypeHint(
                    typename, component.inputOutput, component_entity
                )
            elif isinstance(component_entity, RecordEntity):
                type_hint = AliasTypeHint(typename, component.inputOutput)
            else:
                type_hint = BuiltinTypeHint(
                    TypeKind.resolve(variablename, typename, component_entity),
                    component.inputOutput,
                )

            ndim = len(component.dimensions)
            if f"{typename}" in {
                "OpenModelica.$Code.TypeNames",
                "OpenModelica.$Code.VariableNames",
            }:
                ndim += 1

            yield variablename, cls(
                type_hint=type_hint,
                ndim=ndim,
                is_optional=variablename in optionals,
            )

    @property
    def input_output(self) -> InputOutput:
        return self.type_hint.input_output

    @property
    def sequence_type(self) -> str:
        match self.input_output:
            case "input":
                return "Sequence"
            case _:
                return "List"

    def iter_imports(self) -> Generator[ImportFrom, None, None]:
        yield from self.type_hint.iter_imports()
        if 0 < self.ndim:
            yield ImportFrom(module="typing", name=self.sequence_type)
        if self.is_optional:
            yield ImportFrom(module="typing", name="Union")

    @property
    def annotation(self) -> ast.expr:
        annotation = self.type_hint.annotation

        for _ in range(self.ndim):
            annotation = ast.Subscript(
                value=ast.Name(id=self.sequence_type, ctx=ast.Load()),
                slice=annotation,
                ctx=ast.Load(),
            )

        if self.is_optional:
            if (
                isinstance(annotation, ast.Subscript)
                and isinstance(annotation.value, ast.Name)
                and annotation.value.id == "Union"
                and isinstance(annotation.slice, ast.Tuple)
            ):
                annotation.slice.elts.append(ast.Constant(value=None))
            else:
                annotation = ast.Subscript(
                    value=ast.Name(id="Union", ctx=ast.Load()),
                    slice=ast.Tuple(
                        elts=[
                            annotation,
                            ast.Constant(value=None),
                        ],
                        ctx=ast.Load(),
                    ),
                    ctx=ast.Load(),
                )

        return annotation


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


def _avoid_keyword(s: str) -> str:
    while iskeyword(s):
        s = f"{s}_"
    return s


# Patches

EntitiesItems = Iterable[tuple[TypeName, Entity]]


def patch(interface: Interface) -> Interface:
    return {
        version: dict(_patch(version, entities.items()))
        for version, entities in interface.items()
    }


def _patch(version: Version, entities: EntitiesItems) -> EntitiesItems:
    yield from _patch_check_settings(version, entities)


def _patch_check_settings(
    version: Version, entities: EntitiesItems
) -> EntitiesItems:
    for typename, entity in entities:
        if typename == TypeName(
            "OpenModelica.Scripting.CheckSettingsResult"
        ) and isinstance(entity, RecordEntity):
            REMOVED = VariableName("SENDDATALIBS")
            ADDED = VariableName("RTLIBS")

            code = re.sub(
                rf"(\s+)(.*?){REMOVED}(.*)",
                (rf"\1// \2{REMOVED}\3" rf"\1   \2{ADDED}\3"),
                entity.code,
            )
            components = {
                {REMOVED: ADDED}.get(k, k): v
                for k, v in entity.components.items()
            }
            yield typename, entity.model_copy(
                update={"code": code, "components": components}
            )
        else:
            yield typename, entity
