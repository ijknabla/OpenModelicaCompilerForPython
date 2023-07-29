from __future__ import annotations

from asyncio import AbstractEventLoop, get_event_loop
from collections.abc import AsyncGenerator, Generator

import pytest
import pytest_asyncio
from pkg_resources import resource_filename

import omc4py.session
import omc4py.session.aio
from omc4py.interactive import open_interactives

from .session.aio import EmptySession, NestedSession, OneSession


@pytest.fixture(scope="session")
def event_loop() -> AbstractEventLoop:
    return get_event_loop()


@pytest.fixture(scope="session")
def session() -> Generator[omc4py.session.Session, None, None]:
    interactive, _ = open_interactives("omc")
    with omc4py.session.Session(interactive) as session:
        yield session


@pytest.fixture(scope="session")
def async_session() -> Generator[omc4py.session.aio.Session, None, None]:
    _, interactive = open_interactives("omc")
    with omc4py.session.aio.Session(interactive) as session:
        yield session


@pytest_asyncio.fixture(scope="session")
async def empty_session() -> AsyncGenerator[EmptySession, None]:
    _, interactive = open_interactives("omc")
    with EmptySession(interactive) as session:
        assert await session.loadFile(
            resource_filename(__name__, "src/empty.mo")
        )
        yield session


@pytest_asyncio.fixture(scope="session")
async def one_session() -> AsyncGenerator[OneSession, None]:
    _, interactive = open_interactives("omc")
    with OneSession(interactive) as session:
        assert await session.loadFile(
            resource_filename(__name__, "src/one.mo")
        )
        yield session


@pytest_asyncio.fixture(scope="session")
async def nested_session() -> AsyncGenerator[NestedSession, None]:
    _, interactive = open_interactives("omc")
    with NestedSession(interactive) as session:
        assert await session.loadFile(
            resource_filename(__name__, "src/Nested.mo")
        )
        yield session
