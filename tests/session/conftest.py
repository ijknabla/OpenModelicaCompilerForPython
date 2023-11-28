from __future__ import annotations

from collections.abc import AsyncGenerator
from typing import TYPE_CHECKING

import importlib_resources as resources

if TYPE_CHECKING:
    from typing_extensions import Never

from contextlib import ExitStack

import pytest_asyncio

from omc4py.interactive import Interactive
from omc4py.protocol import asynchronous

from . import AsyncEmptySession, AsyncNestedSession, AsyncOneSession


@pytest_asyncio.fixture(scope="session")
async def empty_session(
    _function_coverage: Never,
) -> AsyncGenerator[AsyncEmptySession, None]:
    interactive = Interactive.open("omc", asynchronous)
    with ExitStack() as stack:
        enter = stack.enter_context
        session = enter(AsyncEmptySession(interactive))
        ref = resources.files("tests.session") / "src/empty.mo"
        assert await session.loadFile(enter(resources.as_file(ref)))
        yield session
        await session.__check__()


@pytest_asyncio.fixture(scope="session")
async def one_session(
    _function_coverage: Never,
) -> AsyncGenerator[AsyncOneSession, None]:
    interactive = Interactive.open("omc", asynchronous)
    with ExitStack() as stack:
        enter = stack.enter_context
        session = enter(AsyncOneSession(interactive))
        ref = resources.files("tests.session") / "src/one.mo"
        assert await session.loadFile(enter(resources.as_file(ref)))
        yield session
        await session.__check__()


@pytest_asyncio.fixture(scope="session")
async def nested_session(
    _function_coverage: Never,
) -> AsyncGenerator[AsyncNestedSession, None]:
    interactive = Interactive.open("omc", asynchronous)
    with ExitStack() as stack:
        enter = stack.enter_context
        session = enter(AsyncNestedSession(interactive))
        ref = resources.files("tests.session") / "src/Nested.mo"
        assert await session.loadFile(enter(resources.as_file(ref)))
        yield session
        await session.__check__()
