from __future__ import annotations

from asyncio import AbstractEventLoop, get_event_loop
from collections.abc import AsyncGenerator, Generator

import pytest
import pytest_asyncio
from pkg_resources import resource_filename

from omc4py import latest, open_session
from omc4py.interactive import open_interactives

from .session.aio import EmptySession, NestedSession, OneSession


@pytest.fixture(scope="session")
def event_loop() -> AbstractEventLoop:
    return get_event_loop()


@pytest.fixture(scope="session")
def session() -> Generator[latest.Session, None, None]:
    with open_session() as session:
        yield session
        session.__check__()


@pytest_asyncio.fixture(scope="session")
async def async_session() -> Generator[latest.aio.Session, None, None]:
    with open_session(asyncio=True) as session:
        yield session
        await session.__check__()


@pytest_asyncio.fixture(scope="session")
async def empty_session() -> AsyncGenerator[EmptySession, None]:
    _, interactive = open_interactives("omc")
    with EmptySession(interactive) as session:
        assert await session.loadFile(
            resource_filename(__name__, "src/empty.mo")
        )
        yield session
        await session.__check__()


@pytest_asyncio.fixture(scope="session")
async def one_session() -> AsyncGenerator[OneSession, None]:
    _, interactive = open_interactives("omc")
    with OneSession(interactive) as session:
        assert await session.loadFile(
            resource_filename(__name__, "src/one.mo")
        )
        yield session
        await session.__check__()


@pytest_asyncio.fixture(scope="session")
async def nested_session() -> AsyncGenerator[NestedSession, None]:
    _, interactive = open_interactives("omc")
    with NestedSession(interactive) as session:
        assert await session.loadFile(
            resource_filename(__name__, "src/Nested.mo")
        )
        yield session
        await session.__check__()
