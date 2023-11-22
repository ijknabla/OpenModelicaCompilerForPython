from __future__ import annotations

from collections.abc import AsyncGenerator
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import Never

import pytest_asyncio
from pkg_resources import resource_filename

from omc4py.interactive import Interactive
from omc4py.protocol import asynchronous

from . import AsyncEmptySession, AsyncNestedSession, AsyncOneSession


@pytest_asyncio.fixture(scope="session")
async def empty_session(
    _function_coverage: Never,
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
    _function_coverage: Never,
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
    _function_coverage: Never,
) -> AsyncGenerator[AsyncNestedSession, None]:
    interactive = Interactive.open("omc", asynchronous)
    with AsyncNestedSession(interactive) as session:
        assert await session.loadFile(
            resource_filename(__name__, "src/Nested.mo")
        )
        yield session
        await session.__check__()
