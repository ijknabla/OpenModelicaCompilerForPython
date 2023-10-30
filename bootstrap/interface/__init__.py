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
from collections.abc import AsyncGenerator, AsyncIterator, Iterable, Sequence
from contextlib import ExitStack, suppress
from dataclasses import dataclass, field
from functools import reduce
from pathlib import Path, PurePosixPath
from subprocess import CalledProcessError
from typing import Generic, Mapping, NamedTuple, NewType, TypeVar, overload

from pkg_resources import resource_filename
from typing_extensions import Literal, NotRequired, Self, TypedDict

from omc4py import TypeName, VariableName, exception, open_session
from omc4py.latest.aio import Session

from ..util import aterminating

_T = TypeVar("_T")
_T_key = TypeVar("_T_key")
_T_value = TypeVar("_T_value")

InputOutput = Literal["input", "output"]
TypeNameString = NewType("TypeNameString", str)
VariableNameString = NewType("VariableNameString", str)
VersionString = NewType("VersionString", str)


class Version(NamedTuple):
    major: int
    minor: int

    @classmethod
    def parse(cls, s: VersionString) -> Self:
        major, minor = map(int, s.split("."))
        return cls(major=major, minor=minor)


class Component(TypedDict):
    className: TypeNameString
    inputOutput: NotRequired[InputOutput]
    dimensions: NotRequired[Sequence[str]]


Components = Mapping[VariableNameString, Component]


class Entity(TypedDict):
    restriction: str
    isType: NotRequired[Literal[True]]
    isPackage: NotRequired[Literal[True]]
    isRecord: NotRequired[Literal[True]]
    isFunction: NotRequired[Literal[True]]
    isEnumeration: NotRequired[Literal[True]]
    code: NotRequired[str]
    components: NotRequired[Components]


Entities = Mapping[TypeNameString, Entity]


Interface = Mapping[VersionString, Entities]


async def create_interface(n: int, exe: str | None) -> Interface:
    with ExitStack() as stack:
        sessions = [
            stack.enter_context(open_session(exe, asyncio=True))
            for _ in range(n)
        ]

        version = await _get_version(sessions[0])

        iterator = QueueingIteration[TypeName]()

        entities: dict[TypeName, Entity | None] = reduce(
            _union,
            await gather(
                *(
                    _get_entities(
                        session, iterator, put=session is sessions[0]
                    )
                    for session in sessions
                )
            ),
        )

    return {
        version: {
            _dump_key(n): e for n, e in entities.items() if e is not None
        }
    }


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


def _union(
    mapping_a: Mapping[_T_key, _T_value], mapping_b: Mapping[_T_key, _T_value]
) -> dict[_T_key, _T_value]:
    result = dict(mapping_a)
    for k, v in mapping_b.items():
        result[k] = v
    return result


async def _get_version(session: Session) -> VersionString:
    matched = re.search(r"(\d+\.\d+)\.\d+", await session.getVersion())
    assert matched is not None
    return VersionString(matched.group(1))


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
    session: Session, iterator: QueueingIteration[TypeName], put: bool
) -> dict[TypeName, Entity | None]:
    result: dict[TypeName, Entity | None] = {}
    if put:
        async for name in _iter_recursive(session, TypeName("OpenModelica")):
            result[name] = None
            await iterator.put(name)
        iterator.put_done()

    async for name in iterator:
        try:
            restriction = await session.getClassRestriction(name)
        except exception.OMCError:
            continue

        entity = Entity(
            restriction=restriction,
        )

        if await session.isType(name):
            entity["isType"] = True
        if await session.isPackage(name):
            entity["isPackage"] = True
        if await session.isRecord(name):
            entity["isRecord"] = True
        if await session.isFunction(name):
            entity["isFunction"] = True
        if await session.isEnumeration(name):
            entity["isEnumeration"] = True

        code: str | None = None
        if entity.keys() & {"isRecord", "isEnumeration"}:
            code = await session.list(name, interfaceOnly=False)
        elif entity.keys() & {"isFunction"}:
            code = await session.list(name, interfaceOnly=True)

        if code:
            entity["code"] = code

        if entity.keys() & {"isRecord", "isFunction"}:
            component_tuples = []
            with suppress(exception.OMCError):
                component_tuples = await session.getComponents(name)

            components: dict[VariableNameString, Component] = {}
            for component_tuple in component_tuples:
                if component_tuple.protected == "public":
                    component = Component(
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

            entity["components"] = components

        result[name] = entity

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
