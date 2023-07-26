from __future__ import annotations

from asyncio import AbstractEventLoop, get_event_loop
from collections.abc import AsyncGenerator

import pytest
import pytest_asyncio
from pkg_resources import resource_filename

from omc4py.compiler import AsyncOMCInteractive

from .aio import EmptySession, NestedSession, OneSession


@pytest.fixture(scope="session")
def event_loop() -> AbstractEventLoop:
    return get_event_loop()


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
