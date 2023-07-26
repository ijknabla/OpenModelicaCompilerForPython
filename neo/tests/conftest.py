from __future__ import annotations

from asyncio import AbstractEventLoop, get_event_loop
from collections.abc import AsyncGenerator, Generator

import pytest
import pytest_asyncio
from pkg_resources import resource_filename

import neo.session
import neo.session.aio
from omc4py.compiler import AsyncOMCInteractive, OMCInteractive

from .aio import EmptySession, NestedSession, OneSession


@pytest.fixture(scope="session")
def event_loop() -> AbstractEventLoop:
    return get_event_loop()


@pytest.fixture(scope="session")
def session() -> Generator[neo.session.Session, None, None]:
    with neo.session.Session(OMCInteractive.open()) as session:
        yield session


@pytest.fixture(scope="session")
def async_session() -> Generator[neo.session.aio.Session, None, None]:
    with neo.session.aio.Session(AsyncOMCInteractive.open()) as session:
        yield session


@pytest_asyncio.fixture(scope="session")
async def empty_session() -> AsyncGenerator[EmptySession, None]:
    with EmptySession(AsyncOMCInteractive.open()) as session:
        assert await session.loadFile(
            resource_filename(__name__, "src/empty.mo")
        )
        yield session


@pytest_asyncio.fixture(scope="session")
async def one_session() -> AsyncGenerator[OneSession, None]:
    with OneSession(AsyncOMCInteractive.open()) as session:
        assert await session.loadFile(
            resource_filename(__name__, "src/one.mo")
        )
        yield session


@pytest_asyncio.fixture(scope="session")
async def nested_session() -> AsyncGenerator[NestedSession, None]:
    with NestedSession(AsyncOMCInteractive.open()) as session:
        assert await session.loadFile(
            resource_filename(__name__, "src/Nested.mo")
        )
        yield session
