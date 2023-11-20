from __future__ import annotations

from asyncio import AbstractEventLoop, get_event_loop
from collections.abc import AsyncGenerator, Generator

import pytest
import pytest_asyncio
from pkg_resources import resource_filename

from omc4py import open_session
from omc4py.interactive import Interactive
from omc4py.protocol import asynchronous
from omc4py.v_1_22 import AsyncSession, Session  # NOTE: update to latest

from .session import AsyncEmptySession, AsyncNestedSession, AsyncOneSession


@pytest.fixture(scope="session")
def event_loop() -> AbstractEventLoop:
    return get_event_loop()


@pytest.fixture(scope="session")
def session() -> Generator[Session, None, None]:
    with open_session() as session:
        yield session
        session.__check__()


@pytest_asyncio.fixture(scope="session")
async def async_session() -> AsyncGenerator[AsyncSession, None]:
    with open_session(asyncio=True) as session:
        yield session
        await session.__check__()


@pytest_asyncio.fixture(scope="session")
async def empty_session() -> AsyncGenerator[AsyncEmptySession, None]:
    interactive = Interactive.open("omc", asynchronous)
    with AsyncEmptySession(interactive) as session:
        assert await session.loadFile(
            resource_filename(__name__, "src/empty.mo")
        )
        yield session
        await session.__check__()


@pytest_asyncio.fixture(scope="session")
async def one_session() -> AsyncGenerator[AsyncOneSession, None]:
    interactive = Interactive.open("omc", asynchronous)
    with AsyncOneSession(interactive) as session:
        assert await session.loadFile(
            resource_filename(__name__, "src/one.mo")
        )
        yield session
        await session.__check__()


@pytest_asyncio.fixture(scope="session")
async def nested_session() -> AsyncGenerator[AsyncNestedSession, None]:
    interactive = Interactive.open("omc", asynchronous)
    with AsyncNestedSession(interactive) as session:
        assert await session.loadFile(
            resource_filename(__name__, "src/Nested.mo")
        )
        yield session
        await session.__check__()
