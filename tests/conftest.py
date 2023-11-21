from __future__ import annotations

from asyncio import AbstractEventLoop, get_event_loop
from collections.abc import AsyncGenerator, Callable, Generator
from functools import wraps
from typing import TYPE_CHECKING, TypeVar

import pytest
import pytest_asyncio
from pkg_resources import resource_filename

import omc4py.modelica
from omc4py import open_session
from omc4py.interactive import Interactive
from omc4py.protocol import asynchronous
from omc4py.v_1_22 import AsyncSession, Session  # NOTE: update to latest

from .session import AsyncEmptySession, AsyncNestedSession, AsyncOneSession

if TYPE_CHECKING:
    from typing_extensions import Concatenate, Never, ParamSpec

    from omc4py.modelica import MethodType, ReturnType, SelfType

    P = ParamSpec("P")
    T = TypeVar("T")

    Call = Callable[
        Concatenate[MethodType[P, T], str, dict[str, str], SelfType, P],
        ReturnType[T],
    ]


@pytest.fixture(scope="session")
def event_loop() -> AbstractEventLoop:
    return get_event_loop()


@pytest.fixture(scope="session")
def function_coverage() -> Generator[None, None, None]:
    with pytest.MonkeyPatch().context() as _monkeypatch:
        _monkeypatch.setattr(
            omc4py.modelica, "_call", wrap_call(omc4py.modelica._call)
        )
        yield


def wrap_call(call: Call[P, T]) -> Call[P, T]:
    @wraps(call)
    def wrapped(
        f: MethodType[P, T],
        funcname: str,
        rename: dict[str, str],
        self: SelfType,
        /,
        *args: P.args,
        **kwargs: P.kwargs,
    ) -> ReturnType[T]:
        f(self, *args, **kwargs)
        return call(f, funcname, rename, self, *args, **kwargs)

    return wrapped


@pytest.fixture(scope="session")
def session(
    function_coverage: Never,
) -> Generator[Session, None, None]:
    with open_session() as session:
        yield session
        session.__check__()


@pytest_asyncio.fixture(scope="session")
async def async_session(
    function_coverage: Never,
) -> AsyncGenerator[AsyncSession, None]:
    with open_session(asyncio=True) as session:
        yield session
        await session.__check__()


@pytest_asyncio.fixture(scope="session")
async def empty_session(
    function_coverage: Never,
) -> AsyncGenerator[AsyncEmptySession, None]:
    interactive = Interactive.open("omc", asynchronous)
    with AsyncEmptySession(interactive) as session:
        assert await session.loadFile(
            resource_filename(__name__, "src/empty.mo")
        )
        yield session
        await session.__check__()


@pytest_asyncio.fixture(scope="session")
async def one_session(
    function_coverage: Never,
) -> AsyncGenerator[AsyncOneSession, None]:
    interactive = Interactive.open("omc", asynchronous)
    with AsyncOneSession(interactive) as session:
        assert await session.loadFile(
            resource_filename(__name__, "src/one.mo")
        )
        yield session
        await session.__check__()


@pytest_asyncio.fixture(scope="session")
async def nested_session(
    function_coverage: Never,
) -> AsyncGenerator[AsyncNestedSession, None]:
    interactive = Interactive.open("omc", asynchronous)
    with AsyncNestedSession(interactive) as session:
        assert await session.loadFile(
            resource_filename(__name__, "src/Nested.mo")
        )
        yield session
        await session.__check__()
