import sys

if sys.version_info < (3, 10):
    raise ImportError(
        f"python=={sys.version_info.major}.{sys.version_info.minor}"
        " not supported!"
    )

from ast import (
    AnnAssign,
    Assign,
    AsyncFunctionDef,
    Attribute,
    Call,
    ClassDef,
    Constant,
    Expr,
    FunctionDef,
    If,
    ImportFrom,
    Load,
    Module,
    Name,
    Raise,
    Store,
    Subscript,
    Tuple,
    alias,
    arg,
    arguments,
    expr,
    stmt,
)
from asyncio import FIRST_COMPLETED, get_running_loop, wait
from collections.abc import (
    AsyncGenerator,
    Generator,
    Iterable,
    Mapping,
    Sequence,
)
from concurrent.futures import ProcessPoolExecutor
from functools import lru_cache
from keyword import iskeyword
from pathlib import PurePath
from typing import DefaultDict, NamedTuple

from omc4py import TypeName

from .interface import (
    ComponentDict,
    EntitiesDict,
    EntityDict,
    InterfaceDict,
    TypeNameString,
    VariableNameString,
    Version,
    VersionString,
)
from .parser import get_enumerators, get_optionals


async def create_code(
    interface: InterfaceDict,
) -> AsyncGenerator[tuple[PurePath, Module], None]:
    path, module, enum_names, enum_refs = _create_enumeration_module(interface)
    yield path, module

    loop = get_running_loop()
    with ProcessPoolExecutor() as executor:
        pending = set(
            loop.run_in_executor(
                executor,
                _create_interface,
                v,
                enum_names[v],
                enum_refs[v],
                interface[v],
            )
            for v in interface
        )
        while pending:
            done, pending = await wait(pending, return_when=FIRST_COMPLETED)
            for future in done:
                for path, module in future.result():
                    yield path, module


ComponentsDict = dict[VariableNameString, ComponentDict]


class Reference(NamedTuple):
    input: expr
    output: expr


References = dict[TypeNameString, Reference]


def _create_enumeration_module(
    interface: InterfaceDict,
) -> tuple[
    PurePath,
    Module,
    Mapping[VersionString, list[str]],
    Mapping[VersionString, References],
]:
    categories = _categorize_enumerations(interface)

    names = DefaultDict[VersionString, list[str]](list)
    references = DefaultDict[VersionString, References](dict)

    module = Module(
        body=[
            ImportFrom(
                module="modelica",
                names=[alias(name="enumeration"), alias(name="external")],
                level=1,
            ),
        ],
        type_ignores=[],
    )
    for full_name, es_vs in categories.items():
        for enumerators, vs in es_vs.items():
            *_, part = _parts(full_name)
            minimal_version = min(vs, key=Version.parse)
            name = f"{part}__{_format_version(minimal_version)}"

            literals = []
            for i, enumerator in enumerate(enumerators, start=1):
                literals.append(Constant(value=enumerator))
                literals.append(Constant(value=i))

            reference = Reference(
                _subscript(
                    "Union",
                    [
                        _reference(name),
                        _subscript("Literal", literals),
                    ],
                ),
                _reference(name),
            )

            for v in vs:
                names[v].append(name)
                references[v][full_name] = reference

            module.body.append(
                ClassDef(
                    name=name,
                    bases=[Name(id="enumeration", ctx=Load())],
                    keywords=[],
                    body=[
                        *_code2doc(
                            interface[minimal_version][full_name]["code"]
                        ),
                        *[
                            Assign(
                                targets=[
                                    Name(id=f"{enumerator!s}", ctx=Store())
                                ],
                                value=Constant(value=i),
                                lineno=None,
                            )
                            for i, enumerator in enumerate(
                                enumerators, start=1
                            )
                        ],
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id="external", ctx=Load()),
                            args=[Constant(value=_as_absolute(full_name))],
                            keywords=[],
                        )
                    ],
                )
            )

    return PurePath("enumeration.py"), module, names, references


def _categorize_enumerations(
    interface: InterfaceDict,
) -> Mapping[
    TypeNameString,
    Mapping[tuple[VariableNameString, ...], list[VersionString]],
]:
    enumerations = list[
        tuple[TypeNameString, VersionString, tuple[VariableNameString, ...]]
    ]()

    for version, entities in interface.items():
        for name, entity in entities.items():
            if entity.get("isEnumeration", False):
                enumerators = tuple(
                    name for name, _ in get_enumerators(entity["code"])
                )
                enumerations.append((name, version, enumerators))
    enumerations.sort(
        key=lambda item: (TypeName(item[0]).parts, Version.parse(item[1]))
    )

    names = set(n for n, *_ in enumerations)
    assert len(names) == len({TypeName(n).last_identifier for n in names})

    Compatibilities = DefaultDict[
        tuple[VariableNameString, ...], list[VersionString]
    ]

    categories = DefaultDict[TypeNameString, Compatibilities](
        lambda: Compatibilities(list)
    )
    for n, v, es in enumerations:
        categories[n][es].append(v)

    return categories


def _code2doc(code: str | None) -> list[Expr]:
    if code is None:
        return []
    else:

        def doc_lines() -> Generator[str, None, None]:
            yield "```modelica"
            yield from code.splitlines(keepends=False)
            yield "```"
            yield ""

        return [Expr(value=Constant(value="\n".join(doc_lines())))]


def _create_interface(
    version: VersionString,
    enumeration_names: list[str],
    enumeration_references: References,
    entities: EntitiesDict,
) -> list[tuple[PurePath, Module]]:
    references = (
        _builtin_references()
        | enumeration_references
        | dict(_record_references(entities))
    )

    functions = set(
        name
        for name, entity in entities.items()
        if entity.get("isFunction")
        if set(c["className"] for c in entity["components"].values())
        <= references.keys()
    )

    packages = set(
        name for name, entity in entities.items() if entity.get("isPackage")
    ) & set(
        parent
        for name in references.keys() | functions
        for parent in _parents(name)
    )

    package_dir = PurePath(_format_version(version))

    result = []
    for aio in [False, True]:
        exports = list(enumeration_names)
        module_body = list[stmt]()
        package_bodies = dict[tuple[str, ...], list[stmt]]({(): []})
        root_packages = list[TypeNameString]()
        scripting_functions = list[tuple[str, expr]]()

        for name, entity in entities.items():
            statement: stmt
            if entity.get("isEnumeration"):
                statement = _create_enumeration(name, references)

            elif entity.get("isRecord"):
                statement = _create_record(name, entity, references)
                if not _in_package(entities, name):
                    exports.append(_parts(name)[-1])

            elif entity.get("isPackage") and name in packages:
                statement = _create_package(name)
                if len(_parts(name)) <= 1:
                    exports.append(name)
                    root_packages.append(name)

            elif entity.get("isFunction") and name in functions:
                components = entity["components"]
                code = entity.get("code")
                inputs, outputs = _inputs_outputs(code, components)
                annotations = dict(_get_annotations(references, components))

                if 1 < len(outputs):
                    module_body.append(
                        _create_return_tuple(name, outputs, annotations)
                    )
                    exports.append(_parts(name)[-1])

                statement = _create_function(
                    name, code, inputs, outputs, annotations, aio
                )

                if _parts(name)[:-1] == ("OpenModelica", "Scripting"):
                    scripting_functions.append(
                        (_parts(name)[-1], _reference(*_parts(name)))
                    )

            else:
                continue

            if hasattr(statement, "body"):
                package_bodies[_parts(name)] = statement.body

            if _in_package(entities, name):
                parent_body = package_bodies[_parts(name)[:-1]]
            else:
                parent_body = module_body

            parent_body.append(statement)

        interface = Module(
            body=[
                *_iter_headers(enumeration_names, sorted(exports), aio),
                *module_body,
                *package_bodies[()],
            ],
            type_ignores=[],
        )

        session = ClassDef(
            name="Session",
            bases=[_reference("BasicSession")],
            keywords=[],
            body=[],
            decorator_list=[],
        )
        exports.append("Session")

        session.body.extend(
            (
                _create_assign(
                    _parts(package)[-1], _reference(*_parts(package))
                )
                for package in root_packages
            )
        )

        if aio:
            session.body.extend(
                [
                    _create_assign(
                        name,
                        Call(
                            func=_reference("staticmethod"),
                            args=[value],
                            keywords=[],
                        ),
                    )
                    for name, value in scripting_functions
                ]
            )
        else:
            session.body.append(
                If(
                    test=_reference("TYPE_CHECKING"),
                    body=[
                        _create_assign(
                            name,
                            Call(
                                func=_reference("staticmethod"),
                                args=[value],
                                keywords=[],
                            ),
                        )
                        for name, value in scripting_functions
                    ],
                    orelse=[
                        _create_assign(name, value)
                        for name, value in scripting_functions
                    ],
                )
            )

        interface.body.append(session)

        if aio:
            result.append((package_dir / "aio.pyi", interface))
        else:
            result.append((package_dir / "_interface.py", interface))

        if aio:
            _all_ = exports
            imports = [
                ImportFrom(
                    module="_interface",
                    names=[alias(name=name) for name in exports],
                    level=1,
                ),
            ]
        else:
            _all_ = exports + ["aio"]
            imports = [
                ImportFrom(names=[alias(name="aio")], level=1),
                ImportFrom(
                    module="_interface",
                    names=[alias(name=name) for name in exports],
                    level=1,
                ),
            ]

        module = Module(
            body=[
                Assign(
                    targets=[Name(id="__all__", ctx=Store())],
                    value=Tuple(
                        elts=[Constant(value=item) for item in _all_],
                        ctx=Load(),
                    ),
                    lineno=None,
                ),
                *imports,
            ],
            type_ignores=[],
        )

        package_dir = PurePath(_format_version(version))
        if aio:
            result.append((package_dir / "aio.py", module))
        else:
            result.append((package_dir / "__init__.py", module))

    return result


def _iter_headers(
    enumeration_names: Iterable[str],
    exports: Iterable[str],
    aio: bool,
) -> Generator[ImportFrom | Assign, None, None]:
    yield ImportFrom(
        module="__future__",
        names=[alias(name="annotations")],
        level=0,
    )
    yield Assign(
        targets=[Name(id="__all__", ctx=Store())],
        value=Tuple(
            elts=[Constant(value=value) for value in exports], ctx=Load()
        ),
        lineno=None,
    )
    yield ImportFrom(
        module="dataclasses",
        names=[alias(name="dataclass")],
        level=0,
    )
    yield ImportFrom(
        module="typing",
        names=[
            alias(name=name)
            for name in ([] if aio else ["TYPE_CHECKING"])
            + ["List", "Literal", "Sequence", "Union"]
        ],
        level=0,
    )
    yield ImportFrom(
        module="typing_extensions",
        names=[alias(name="Annotated")],
        level=0,
    )
    yield ImportFrom(
        module="enumeration",
        names=[alias(name=name) for name in enumeration_names],
        level=2,
    )
    yield ImportFrom(
        module="modelica",
        names=[
            alias(name="alias"),
            alias(name="external"),
            alias(name="package"),
            alias(name="record"),
        ],
        level=2,
    )
    yield ImportFrom(
        module="openmodelica",
        names=[
            alias(name="TypeName"),
            alias(name="VariableName"),
        ],
        level=2,
    )
    if aio:
        yield ImportFrom(
            module="session.aio",
            names=[alias(name="Session", asname="BasicSession")],
            level=2,
        )
    else:
        yield ImportFrom(
            module="session",
            names=[alias(name="Session", asname="BasicSession")],
            level=2,
        )


@lru_cache(1)
def _builtin_references() -> dict[TypeNameString, Reference]:
    return (
        {
            TypeNameString(n): Reference(i, i)
            for n, i in [
                ("Real", _reference("float")),
                ("Integer", _reference("int")),
                ("Boolean", _reference("bool")),
                ("String", _reference("str")),
            ]
        }
        | {
            TypeNameString(f"OpenModelica.$Code.{n}"): Reference(
                _subscript("Union", [_reference(n), _reference("str")]),
                _reference(n),
            )
            for n in ["TypeName", "VariableName"]
        }
        | {
            TypeNameString("OpenModelica.$Code.VariableNames"): Reference(
                _subscript(
                    "Sequence",
                    _subscript(
                        "Union",
                        [_reference("VariableName"), _reference("str")],
                    ),
                ),
                _subscript("List", _reference("VariableName")),
            )
        }
    )


def _record_references(
    entities: EntitiesDict,
) -> Generator[tuple[TypeNameString, Reference], None, None]:
    for name, entity in entities.items():
        if entity.get("isRecord"):
            parts = _parts(name)
            expr = (
                _reference(*parts)
                if _in_package(entities, name)
                else _reference(parts[-1])
            )
            yield name, Reference(expr, expr)


def _create_package(name: TypeNameString) -> ClassDef:
    parts = _parts(name)
    return ClassDef(
        name=parts[-1],
        bases=[_reference("package")],
        keywords=[],
        body=[],
        decorator_list=[_external_decorator(name)],
    )


def _create_enumeration(
    name: TypeNameString, references: References
) -> Assign:
    return Assign(
        targets=[Name(id=_parts(name)[-1], ctx=Store())],
        value=references[name].output,
        lineno=None,
    )


def _create_return_tuple(
    name: TypeNameString,
    outputs: list[VariableNameString],
    annotations: dict[VariableNameString, expr],
) -> ClassDef:
    return ClassDef(
        name=_parts(name)[-1],
        bases=[],
        keywords=[],
        body=[
            AnnAssign(
                target=Name(id=output, ctx=Store()),
                annotation=annotations[output],
                simple=1,
            )
            for output in outputs
        ],
        decorator_list=[],
    )


def _create_function(
    name: TypeNameString,
    code: str | None,
    inputs: dict[VariableNameString, bool],
    outputs: list[VariableNameString],
    annotations: dict[VariableNameString, expr],
    aio: bool,
) -> FunctionDef | AsyncFunctionDef:
    parts = _parts(name)

    returns: expr
    if len(outputs) == 0:
        returns = Constant(value=None)
    elif len(outputs) == 1:
        (output,) = outputs
        returns = annotations[output]
    else:
        returns = _reference(parts[-1])

    function_type: type[AsyncFunctionDef] | type[FunctionDef]
    function_type = AsyncFunctionDef if aio else FunctionDef

    return function_type(
        name=parts[-1],
        args=arguments(
            posonlyargs=[],
            args=[
                arg(arg="_"),
                *(
                    arg(
                        arg=_avoid_keyword(input),
                        annotation=annotations[input],
                    )
                    for input in inputs
                ),
            ],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[Constant(value=Ellipsis)] * sum(inputs.values()),
        ),
        body=[
            *_code2doc(code),
            Raise(
                exc=Call(
                    func=Name(id="NotImplementedError", ctx=Load()),
                    args=[],
                    keywords=[],
                )
            ),
        ],
        decorator_list=[
            _external_decorator(name),
            _reference("classmethod"),
        ],
        returns=returns,
        lineno=None,
    )


def _create_function_assign(name: TypeNameString) -> Assign:
    return Assign(
        targets=[Name(id=_parts(name)[-1], ctx=Store())],
        value=_reference(*_parts(name)),
        lineno=None,
    )


def _create_record(
    name: TypeNameString, entity: EntityDict, references: References
) -> ClassDef:
    code = entity["code"]
    annotations = dict(_get_annotations(references, entity["components"]))
    return ClassDef(
        name=_parts(name)[-1],
        bases=[_reference("record")],
        keywords=[],
        body=[
            *_code2doc(code),
            *(
                AnnAssign(
                    target=Name(id=name, ctx=Store()),
                    annotation=annotation,
                    simple=1,
                )
                for name, annotation in annotations.items()
            ),
        ],
        decorator_list=[
            _external_decorator(name),
            _reference("dataclass"),
        ],
    )


def _create_assign(target: str, value: expr) -> Assign:
    return Assign(
        targets=[Name(id=target, ctx=Store())],
        value=value,
        lineno=None,
    )


def _external_decorator(name: TypeNameString) -> Call:
    return Call(
        func=_reference("external"),
        args=[Constant(value=f"{TypeName(name).as_absolute()}")],
        keywords=[],
    )


def _as_absolute(name: TypeNameString) -> TypeNameString:
    return TypeNameString(f"{TypeName(name).as_absolute()}")


@lru_cache(1)
def _parts(name: TypeNameString) -> tuple[str, ...]:
    return TypeName(name).parts


def _parents(name: TypeNameString) -> Generator[TypeNameString, None, None]:
    for parent in TypeName(name).parents:
        if parent == TypeName():
            return
        yield TypeNameString(f"{parent}")


def _in_package(entities: EntitiesDict, name: TypeNameString) -> bool:
    return all(entities[parent].get("isPackage") for parent in _parents(name))


def _inputs_outputs(
    code: str | None, components: ComponentsDict
) -> tuple[dict[VariableNameString, bool], list[VariableNameString]]:
    if code is not None:
        optionals = get_optionals(code)
    else:
        optionals = ()

    inputs, outputs = {}, []
    for name, component in components.items():
        if component["inputOutput"] == "input":
            inputs[name] = name in optionals
        else:
            outputs.append(name)

    inputs = dict(sorted(inputs.items(), key=lambda item: item[-1]))

    return inputs, outputs


def _get_annotations(
    references: dict[TypeNameString, Reference], components: ComponentsDict
) -> Generator[tuple[VariableNameString, expr], None, None]:
    for name, component in components.items():
        io = component.get("inputOutput", "output")
        reference = getattr(references[component["className"]], io)
        sequence_type = "Sequence" if io == "input" else "List"
        for _ in component.get("dimensions", []):
            reference = _subscript(sequence_type, reference)

        if iskeyword(name):
            reference = _mark_alias(reference, name)

        yield name, reference


def _mark_alias(reference: expr, alias: VariableNameString) -> Subscript:
    return _subscript(
        "Annotated",
        [
            reference,
            _subscript(
                "alias",
                _subscript("Literal", Constant(value=alias)),
            ),
        ],
    )


def _reference(part: str, *parts: str) -> Name | Attribute:
    if not parts:
        return Name(id=part, ctx=Load())
    else:
        *body, tail = part, *parts
        return Attribute(value=_reference(*body), attr=tail, ctx=Load())


def _subscript(value: str, slice: expr | Sequence[expr]) -> Subscript:
    slice = Tuple(elts=slice, ctx=Load()) if isinstance(slice, list) else slice
    return Subscript(value=_reference(value), slice=slice, ctx=Load())


def _format_version(version: VersionString) -> str:
    v = Version.parse(version)
    return f"v_{v.major}_{v.minor}"


def _avoid_keyword(s: str) -> str:
    while iskeyword(s):
        s += "_"
    return s
