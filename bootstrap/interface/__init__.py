from __future__ import annotations

import re
from asyncio import create_subprocess_exec, create_task, gather
from asyncio.subprocess import PIPE
from collections import ChainMap
from collections.abc import AsyncGenerator, AsyncIterable, Iterable
from contextlib import AsyncExitStack, suppress
from pathlib import Path, PurePosixPath
from subprocess import CalledProcessError
from typing import (
    Any,
    Dict,
    Literal,
    Mapping,
    NamedTuple,
    NewType,
    Sequence,
    Tuple,
    TypeVar,
    Union,
    cast,
    get_args,
    overload,
)

from frozendict import frozendict
from pydantic import (
    BaseModel,
    PlainSerializer,
    PlainValidator,
    RootModel,
    model_serializer,
)
from typing_extensions import Annotated, NotRequired, Self, TypedDict

from bootstrap.util import (
    QueueingIteration,
    ensure_cancel,
    ensure_terminate,
    get_root,
)
from omc4py import (
    AsyncSession,
    TypeName,
    VariableName,
    exception,
    open_session,
)

_T = TypeVar("_T")
_T_key = TypeVar("_T_key")
_T_value = TypeVar("_T_value")

InputOutput = Literal["input", "output", "unspecified"]
TypeNameString = NewType("TypeNameString", str)
VariableNameString = NewType("VariableNameString", str)
VersionString = NewType("VersionString", str)


@PlainValidator
def _typename_validator(typename: str | TypeName) -> TypeName:
    return TypeName(typename)


@PlainSerializer
def _typename_serializer(typename: TypeName) -> str:
    return f"{typename}"


AnnotatedTypeName = Annotated[
    TypeName, _typename_validator, _typename_serializer
]


@PlainValidator
def _variablename_validator(variablename: str | VariableName) -> VariableName:
    return VariableName(variablename)


@PlainSerializer
def _variablename_serializer(variablename: VariableName) -> str:
    return f"{variablename}"


AnnotatedVariableName = Annotated[
    VariableName, _variablename_validator, _variablename_serializer
]


class Version(NamedTuple):
    major: int
    minor: int

    @classmethod
    def parse(cls, s: str) -> Self:
        major, minor = map(int, s.split("."))
        return cls(major=major, minor=minor)

    def unparse(self) -> str:
        return f"{self.major}.{self.minor}"


@PlainValidator
def _version_validator(version: str | Version) -> Version:
    if isinstance(version, str):
        return Version.parse(version)
    elif isinstance(version, Version):
        return version
    raise ValueError(version)


@PlainSerializer
def _version_serializer(version: Version) -> str:
    return version.unparse()


AnnotatedVersion = Annotated[Version, _version_validator, _version_serializer]


class Component(BaseModel, frozen=True):
    className: AnnotatedTypeName
    inputOutput: InputOutput = "unspecified"
    dimensions: Tuple[str, ...] = ()

    @model_serializer
    def __serialize(self) -> Any:
        result = _Component(className=TypeNameString(f"{self.className}"))
        if self.inputOutput != "unspecified":
            result["inputOutput"] = self.inputOutput
        if self.dimensions:
            result["dimensions"] = self.dimensions

        return result


class _Component(TypedDict):
    className: TypeNameString
    inputOutput: NotRequired[Literal["input", "output"]]
    dimensions: NotRequired[Sequence[str]]


@PlainValidator
def _components_validator(
    components: Mapping[Any, Any],
) -> frozendict[VariableName, Component]:
    return frozendict(
        (VariableName(k), Component.model_validate(v))
        for k, v in components.items()
    )


Components = Annotated[
    Mapping[AnnotatedVariableName, Component], _components_validator
]


class TypeEntity(BaseModel, frozen=True):
    restriction: str
    isType: Literal[True]
    isPackage: Literal[False] = False
    isRecord: Literal[False] = False
    isFunction: Literal[False] = False
    isEnumeration: Literal[False] = False

    @model_serializer
    def __serialize(self) -> Any:
        return _entity_serializer(self)


class PackageEntity(BaseModel, frozen=True):
    restriction: str
    isType: Literal[False] = False
    isPackage: Literal[True]
    isRecord: Literal[False] = False
    isFunction: Literal[False] = False
    isEnumeration: Literal[False] = False

    @model_serializer
    def __serialize(self) -> Any:
        return _entity_serializer(self)


class RecordEntity(BaseModel, frozen=True):
    restriction: str
    isType: Literal[False] = False
    isPackage: Literal[False] = False
    isRecord: Literal[True]
    isFunction: Literal[False] = False
    isEnumeration: Literal[False] = False
    code: str
    components: Components

    @model_serializer
    def __serialize(self) -> Any:
        return _entity_serializer(self)


class FunctionEntity(BaseModel, frozen=True):
    restriction: str
    isType: Literal[False] = False
    isPackage: Literal[False] = False
    isRecord: Literal[False] = False
    isFunction: Literal[True]
    isEnumeration: Literal[False] = False
    code: Union[str, None] = None
    components: Components

    @model_serializer
    def __serialize(self) -> Any:
        return _entity_serializer(self)


class EnumerationEntity(BaseModel, frozen=True):
    restriction: str
    isType: Literal[True]
    isPackage: Literal[False] = False
    isRecord: Literal[False] = False
    isFunction: Literal[False] = False
    isEnumeration: Literal[True]
    code: str

    @model_serializer
    def __serialize(self) -> Any:
        return _entity_serializer(self)


class _Entity(TypedDict):
    restriction: str
    isType: NotRequired[Literal[True]]
    isPackage: NotRequired[Literal[True]]
    isRecord: NotRequired[Literal[True]]
    isFunction: NotRequired[Literal[True]]
    isEnumeration: NotRequired[Literal[True]]
    code: NotRequired[str]
    components: NotRequired[Dict[VariableNameString, _Component]]


def _entity_serializer(entity: Entity) -> _Entity:
    result = _Entity(restriction=entity.restriction)

    IsAttribute = Literal[
        "isType", "isPackage", "isRecord", "isFunction", "isEnumeration"
    ]
    is_attribute: IsAttribute
    for is_attribute in get_args(IsAttribute):
        value = getattr(entity, is_attribute, False)
        if value:
            result[is_attribute] = value

    code: str | None = None
    if not isinstance(entity, (TypeEntity, PackageEntity)):
        code = entity.code
    if code is not None:
        result["code"] = code

    if not isinstance(entity, (TypeEntity, PackageEntity, EnumerationEntity)):
        result["components"] = {
            VariableNameString(f"{k}"): cast(_Component, v.model_dump())
            for k, v in entity.components.items()
        }

    return result


Entity = Union[
    TypeEntity, PackageEntity, RecordEntity, FunctionEntity, EnumerationEntity
]

Entities = Mapping[AnnotatedTypeName, Entity]

Interface = Mapping[AnnotatedVersion, Entities]


class InterfaceRoot(RootModel[Interface]):
    pass


async def create_interface(n: int, exe: str | None) -> InterfaceRoot:
    async with AsyncExitStack() as stack:
        sessions = [
            cast(
                AsyncSession,
                stack.enter_context(open_session(exe, asyncio=True)),
            )
            for _ in range(n)
        ]

        version = await _get_version(sessions[0])

        typenames_iterator = QueueingIteration[TypeName]()

        put_task = await stack.enter_async_context(
            ensure_cancel(
                create_task(_put_recursive(sessions[0], typenames_iterator))
            )
        )

        entities: Mapping[TypeName, Entity]
        entities = ChainMap(
            *await gather(
                *(
                    _get_entities(
                        session,
                        typenames_iterator,
                    )
                    for session in sessions
                )
            )
        )

        await put_task
        typename_order = put_task.result()

        entities = {
            typename: entities[typename]
            for typename in typename_order
            if typename in entities
        }

    return InterfaceRoot(root={version: entities})


async def create_interface_by_docker(
    image: Iterable[str],
    n: int,
    output_dir: Path,
    pip_cache_dir: Path | None,
) -> None:
    async with AsyncExitStack() as stack:
        process = await stack.enter_async_context(
            ensure_terminate(
                await create_subprocess_exec(
                    "poetry",
                    "export",
                    "--only=main,bootstrap",
                    "--without-hashes",
                    cwd=get_root(),
                    stdout=PIPE,
                )
            )
        )
        requirements: list[str] = []
        assert process.stdout is not None
        async for line in process.stdout:
            if line.startswith(b"poetry-version-plugin:"):
                continue
            requirement, *_ = line.split(b";")
            requirements.append(requirement.strip().decode("utf-8"))

    await gather(
        *(
            _create_interface_by_docker(
                i, n, output_dir, pip_cache_dir, requirements
            )
            for i in image
        )
    )


async def _create_interface_by_docker(
    image: str,
    n: int,
    output_dir: Path,
    pip_cache_dir: Path | None,
    requirements: Iterable[str],
) -> None:
    py_version_match = re.search(r"python\d+\.\d+", image)
    assert py_version_match is not None

    PYTHON = py_version_match.group(0)

    omc_version_match = re.search(
        r"(\d+)\.(\d+)\.\d+",
        await _docker_run(
            image,
            [],
            ["omc", "--version"],
            pipe=True,
        ),
    )
    assert omc_version_match is not None
    omc_major, omc_minor = map(int, omc_version_match.groups())

    omc4py_s = get_root()
    omc4py_t = PurePosixPath("/omc4py")
    output_s = output_dir.resolve()
    output_t = PurePosixPath("/output") / f"v_{omc_major}_{omc_minor}.yaml"

    docker_args = [
        "--mount",
        f"type=bind,source={omc4py_s},target={omc4py_t}",
        "--mount",
        f"type=bind,source={output_s},target={output_t.parent}",
        "--user=1000:1000",
    ]

    if pip_cache_dir is not None:
        pip_cache_s = pip_cache_dir.resolve()
        pip_cache_t = PurePosixPath("/pip-cache")

        docker_args.extend(
            [
                "--mount",
                f"type=bind,source={pip_cache_s},target={pip_cache_t}",
            ]
        )
        PYTHON = f"env PIP_CACHE_DIR={pip_cache_t} {PYTHON}"

    await _docker_run(
        image,
        docker_args,
        [
            "bash",
            "-c",
            " && ".join(
                [
                    f"cd {omc4py_t}",
                    f"{PYTHON} -m pip install -U pip",
                    f"{PYTHON} -m pip install " + " ".join(requirements),
                    f"{PYTHON} -m bootstrap interface -n {n} -o {output_t}",
                ]
            ),
        ],
        pipe=False,
    )


@overload
async def _docker_run(
    image: str,
    docker_args: Iterable[str],
    args: Iterable[str],
    pipe: Literal[False],
) -> None: ...


@overload
async def _docker_run(
    image: str,
    docker_args: Iterable[str],
    args: Iterable[str],
    pipe: Literal[True],
) -> str: ...


async def _docker_run(
    image: str,
    docker_args: Iterable[str],
    args: Iterable[str],
    pipe: Literal[False, True],
) -> str | None:
    cmd = [
        "docker",
        "run",
        *docker_args,
        image,
        *args,
    ]
    async with ensure_terminate(
        await create_subprocess_exec(
            *cmd,
            stdout=PIPE if pipe else None,
        )
    ) as process:
        o, _ = await process.communicate()
        if pipe:
            return o.decode("utf-8")
        if process.returncode:
            raise CalledProcessError(process.returncode, cmd)

    return None


async def _get_version(session: AsyncSession) -> Version:
    matched = re.search(r"(\d+\.\d+)\.\d+", await session.getVersion())
    assert matched is not None
    return Version.parse(matched.group(1))


async def _put_recursive(
    session: AsyncSession, iterator: QueueingIteration[TypeName]
) -> list[TypeName]:
    result: list[TypeName] = []

    async for typename in _iter_recursive(session, TypeName("OpenModelica")):
        await iterator.put(typename)
        result.append(typename)
    iterator.put_done()

    return result


async def _iter_recursive(
    session: AsyncSession, name: TypeName
) -> AsyncGenerator[TypeName, None]:
    yield name
    try:
        children = await session.getClassNames(
            name, builtin=True, showProtected=True
        )
    except exception.OMCError:
        return
    for child in children:
        async for child_item in _iter_recursive(session, name / child):
            yield child_item


async def _get_entities(
    session: AsyncSession, typenames: AsyncIterable[TypeName]
) -> dict[TypeName, Entity]:
    return {
        typename: entity
        async for typename in typenames
        for entity in [await _get_entity(session, typename)]
        if entity is not None
    }


async def _get_entity(
    session: AsyncSession,
    name: TypeName,
) -> Entity | None:
    try:
        restriction = await session.getClassRestriction(name)
    except exception.OMCError:
        return None

    code = await session.list(name, interfaceOnly=False)
    code_kwargs = {"code": code} if code else {}

    interface_only_code = await session.list(name, interfaceOnly=True)
    interface_only_code_kwargs = (
        {"code": interface_only_code} if interface_only_code else {}
    )

    components: Components = {
        k: v async for k, v in _iter_components(session, name)
    }

    isType, isPackage, isRecord, isFunction, isEnumeration = await gather(
        session.isType(name),
        session.isPackage(name),
        session.isRecord(name),
        session.isFunction(name),
        session.isEnumeration(name),
    )

    if (
        True
        and isType
        and not isPackage
        and not isRecord
        and not isFunction
        and not isEnumeration
    ):
        return TypeEntity(
            restriction=restriction,
            isType=isType,
            isPackage=isPackage,
            isRecord=isRecord,
            isFunction=isFunction,
            isEnumeration=isEnumeration,
        )
    if (
        True
        and not isType
        and isPackage
        and not isRecord
        and not isFunction
        and not isEnumeration
    ):
        return PackageEntity(
            restriction=restriction,
            isType=isType,
            isPackage=isPackage,
            isRecord=isRecord,
            isFunction=isFunction,
            isEnumeration=isEnumeration,
        )
    if (
        True
        and not isType
        and not isPackage
        and isRecord
        and not isFunction
        and not isEnumeration
    ):
        return RecordEntity(
            restriction=restriction,
            **code_kwargs,
            components=components,
            isType=isType,
            isPackage=isPackage,
            isRecord=isRecord,
            isFunction=isFunction,
            isEnumeration=isEnumeration,
        )
    if (
        True
        and not isType
        and not isPackage
        and not isRecord
        and isFunction
        and not isEnumeration
    ):
        return FunctionEntity(
            restriction=restriction,
            **interface_only_code_kwargs,
            components=components,
            isType=isType,
            isPackage=isPackage,
            isRecord=isRecord,
            isFunction=isFunction,
            isEnumeration=isEnumeration,
        )
    if (
        True
        and isType
        and not isPackage
        and not isRecord
        and not isFunction
        and isEnumeration
    ):
        return EnumerationEntity(
            restriction=restriction,
            **code_kwargs,
            isType=isType,
            isPackage=isPackage,
            isRecord=isRecord,
            isFunction=isFunction,
            isEnumeration=isEnumeration,
        )

    return None


async def _iter_components(
    session: AsyncSession, typename: TypeName
) -> AsyncGenerator[tuple[VariableName, Component], None]:
    with suppress(exception.OMCError):
        for component_tuple in await session.getComponents(typename):
            if component_tuple.protected == "public":
                yield (
                    component_tuple.name,
                    Component(
                        className=component_tuple.className,
                        inputOutput=component_tuple.inputOutput,
                        dimensions=tuple(component_tuple.dimensions),
                    ),
                )
