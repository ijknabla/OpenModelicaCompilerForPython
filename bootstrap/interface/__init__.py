from __future__ import annotations

import re
from asyncio import (
    FIRST_COMPLETED,
    CancelledError,
    Event,
    Queue,
    create_task,
    gather,
    wait,
)
from collections.abc import AsyncGenerator, AsyncIterator, Sequence
from contextlib import ExitStack, suppress
from dataclasses import dataclass, field
from functools import reduce
from typing import Generic, Mapping, NamedTuple, NewType, TypeVar, overload

from typing_extensions import Literal, NotRequired, Self, TypedDict

from neo import TypeName, VariableName
from omc4py import exception

from .. import open_session
from ..session import Session

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


async def create_interface(n: int) -> Interface:
    with ExitStack() as stack:
        sessions = [stack.enter_context(open_session()) for _ in range(n)]

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
