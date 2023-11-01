from __future__ import annotations

import re
from asyncio import (
    FIRST_COMPLETED,
    CancelledError,
    Event,
    Queue,
    create_subprocess_exec,
    create_task,
    gather,
    wait,
)
from asyncio.subprocess import PIPE
from collections import ChainMap
from collections.abc import (
    AsyncGenerator,
    AsyncIterable,
    AsyncIterator,
    Iterable,
)
from contextlib import AsyncExitStack, suppress
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath
from subprocess import CalledProcessError
from typing import (
    Any,
    Dict,
    Generic,
    Literal,
    Mapping,
    NamedTuple,
    NewType,
    Sequence,
    TypeVar,
    Union,
    cast,
    get_args,
    overload,
)

from pkg_resources import resource_filename
from pydantic import (
    BaseModel,
    PlainSerializer,
    PlainValidator,
    RootModel,
    model_serializer,
)
from typing_extensions import Annotated, NotRequired, Self, TypedDict

from omc4py import TypeName, VariableName, exception, open_session
from omc4py.latest.aio import Session

from ..util import aterminating, ensure_cancel

_T = TypeVar("_T")
_T_key = TypeVar("_T_key")
_T_value = TypeVar("_T_value")

InputOutput = Literal["input", "output"]
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


class ComponentDict(TypedDict):
    className: TypeNameString
    inputOutput: NotRequired[InputOutput]
    dimensions: NotRequired[Sequence[str]]


class Component(BaseModel):
    className: AnnotatedTypeName
    inputOutput: Literal["input", "output", "unspecified"] = "unspecified"
    dimensions: Union[Sequence[str], None] = None

    @model_serializer
    def __serialize(self) -> Dict[str, Any]:
        result = ComponentDict(className=TypeNameString(f"{self.className}"))
        if self.inputOutput != "unspecified":
            result["inputOutput"] = self.inputOutput
        if self.dimensions is not None:
            result["dimensions"] = self.dimensions

        return result


ComponentsDict = Dict[VariableNameString, ComponentDict]

Components = RootModel[Dict[AnnotatedVariableName, Component]]


class EntityDict(TypedDict):
    restriction: str
    isType: NotRequired[Literal[True]]
    isPackage: NotRequired[Literal[True]]
    isRecord: NotRequired[Literal[True]]
    isFunction: NotRequired[Literal[True]]
    isEnumeration: NotRequired[Literal[True]]
    code: NotRequired[str]
    components: NotRequired[ComponentsDict]


class TypeEntity(BaseModel):
    restriction: str
    isType: Literal[True]
    isPackage: Literal[False] = False
    isRecord: Literal[False] = False
    isFunction: Literal[False] = False
    isEnumeration: Literal[False] = False

    @model_serializer
    def __serialize(self) -> Dict[str, Any]:
        return _entity_serializer(self)


class PackageEntity(BaseModel):
    restriction: str
    isType: Literal[False] = False
    isPackage: Literal[True]
    isRecord: Literal[False] = False
    isFunction: Literal[False] = False
    isEnumeration: Literal[False] = False

    @model_serializer
    def __serialize(self) -> Dict[str, Any]:
        return _entity_serializer(self)


class RecordEntity(BaseModel):
    restriction: str
    isType: Literal[False] = False
    isPackage: Literal[False] = False
    isRecord: Literal[True]
    isFunction: Literal[False] = False
    isEnumeration: Literal[False] = False
    code: str
    components: Components

    @model_serializer
    def __serialize(self) -> Dict[str, Any]:
        return _entity_serializer(self)


class FunctionEntity(BaseModel):
    restriction: str
    isType: Literal[False] = False
    isPackage: Literal[False] = False
    isRecord: Literal[False] = False
    isFunction: Literal[True]
    isEnumeration: Literal[False] = False
    code: Union[str, None] = None
    components: Components

    @model_serializer
    def __serialize(self) -> Dict[str, Any]:
        return _entity_serializer(self)


class EnumerationEntity(BaseModel):
    restriction: str
    isType: Literal[True]
    isPackage: Literal[False] = False
    isRecord: Literal[False] = False
    isFunction: Literal[False] = False
    isEnumeration: Literal[True]
    code: str

    @model_serializer
    def __serialize(self) -> Dict[str, Any]:
        return _entity_serializer(self)


def _entity_serializer(entity: Entity) -> EntityDict:
    result = EntityDict(restriction=entity.restriction)

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

    components: ComponentsDict | None = None
    if not isinstance(entity, (TypeEntity, PackageEntity, EnumerationEntity)):
        components = cast(ComponentsDict, entity.components.model_dump())
    if components is not None:
        result["components"] = components

    return result


Entity = Union[
    TypeEntity, PackageEntity, RecordEntity, FunctionEntity, EnumerationEntity
]


EntitiesDict = Dict[TypeNameString, EntityDict]

Entities = Mapping[AnnotatedTypeName, Entity]

InterfaceDict = Dict[VersionString, EntitiesDict]


class Interface(RootModel[Mapping[AnnotatedVersion, Entities]]):
    ...


async def create_interface(n: int, exe: str | None) -> Interface:
    async with AsyncExitStack() as stack:
        sessions = [
            stack.enter_context(open_session(exe, asyncio=True))
            for _ in range(min(1, n))
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

    return Interface(root={version: entities})


async def create_interface_by_docker(
    image: Iterable[str],
    n: int,
    output_dir: Path,
    pip_cache_dir: Path | None,
) -> None:
    requirements: list[str] = []

    async with aterminating(
        await create_subprocess_exec(
            "poetry",
            "export",
            "--only=main,bootstrap",
            "--without-hashes",
            cwd=Path(__file__).parent,
            stdout=PIPE,
        )
    ) as process:
        assert process.stdout is not None
        async for line in process.stdout:
            requirement, *_ = line.split(b";")
            requirements.append(requirement.decode("utf-8").strip())

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
    py_version_match = re.search(
        r"(\d+)\.(\d+)\.\d+",
        await _docker_run(
            image,
            [],
            ["python", "--version"],
            pipe=True,
        ),
    )
    assert py_version_match is not None
    py_major, py_minor = map(int, py_version_match.groups())
    if (py_major, py_minor) < (3, 8):
        requirements = [
            requirement.split("==")[0] for requirement in requirements
        ]

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

    omc4py_s = Path(resource_filename("bootstrap", "..")).resolve()
    omc4py_t = PurePosixPath("/omc4py")
    output_s = output_dir.resolve()
    output_t = PurePosixPath("/output") / f"v_{omc_major}_{omc_minor}.yaml"

    docker_args = [
        "--mount",
        f"type=bind,source={omc4py_s},target={omc4py_t}",
        "--mount",
        f"type=bind,source={output_s},target={output_t.parent}",
    ]

    PYTHON = "sudo -u user python"

    if pip_cache_dir is not None:
        pip_cache_s = pip_cache_dir.resolve()
        pip_cache_t = PurePosixPath("/pip-cache")

        docker_args.extend(
            [
                "--mount",
                f"type=bind,source={pip_cache_s},target={pip_cache_t}",
            ]
        )
        PYTHON = f"sudo -u user env PIP_CACHE_DIR={pip_cache_t} python"

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
) -> None:
    ...


@overload
async def _docker_run(
    image: str,
    docker_args: Iterable[str],
    args: Iterable[str],
    pipe: Literal[True],
) -> str:
    ...


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
    async with aterminating(
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


async def _get_version(session: Session) -> Version:
    matched = re.search(r"(\d+\.\d+)\.\d+", await session.getVersion())
    assert matched is not None
    return Version.parse(matched.group(1))


@overload
def _dump_key(key: TypeName) -> TypeNameString:
    ...


@overload
def _dump_key(key: VariableName) -> VariableNameString:
    ...


def _dump_key(
    key: TypeName | VariableName,
) -> TypeNameString | VariableNameString:
    return f"{key!s}"  # type: ignore


@dataclass(frozen=True)
class QueueingIteration(Generic[_T]):
    _queue: Queue[_T] = field(default_factory=Queue)
    _put_done: Event = field(default_factory=Event)

    async def put(self, item: _T) -> None:
        await self._queue.put(item)

    def put_done(self) -> None:
        self._put_done.set()

    async def __aiter__(self) -> AsyncIterator[_T]:
        stop_task = create_task(self.__wait_stop())

        while True:
            get_task = create_task(self._queue.get())
            done, pending = await wait(
                [get_task, stop_task], return_when=FIRST_COMPLETED
            )
            if get_task in done:
                try:
                    yield get_task.result()
                finally:
                    self._queue.task_done()
            else:
                for task in pending:
                    task.cancel()
                for task in pending:
                    with suppress(CancelledError):
                        await task
                break

    async def __wait_stop(self) -> None:
        await self._put_done.wait()
        await self._queue.join()


async def _get_entities(
    session: Session, typenames: AsyncIterable[TypeName]
) -> dict[TypeName, Entity]:
    return {
        typename: entity
        async for typename in typenames
        for entity in [await _get_entity(session, typename)]
        if entity is not None
    }


async def _get_entity(
    session: Session,
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

    component_tuples = []
    with suppress(exception.OMCError):
        component_tuples = await session.getComponents(name)

    components: dict[VariableNameString, ComponentDict] = {}
    for component_tuple in component_tuples:
        if component_tuple.protected == "public":
            component = ComponentDict(
                className=_dump_key(component_tuple.className),
            )

            if (
                component_tuple.inputOutput == "input"
                or component_tuple.inputOutput == "output"
            ):
                component["inputOutput"] = component_tuple.inputOutput

            if component_tuple.dimensions:
                component["dimensions"] = component_tuple.dimensions

            components[_dump_key(component_tuple.name)] = component

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
            components=Components.model_validate(components),
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
            components=Components.model_validate(components),
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


async def _put_recursive(
    session: Session, iterator: QueueingIteration[TypeName]
) -> list[TypeName]:
    result: list[TypeName] = []

    async for typename in _iter_recursive(session, TypeName("OpenModelica")):
        await iterator.put(typename)
        result.append(typename)
    iterator.put_done()

    return result


async def _iter_recursive(
    session: Session, name: TypeName
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
