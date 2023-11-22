from __future__ import annotations

import pytest

from . import AsyncEmptySession, AsyncNestedSession, AsyncOneSession, Enum, One


@pytest.mark.asyncio
async def test_empty_session(empty_session: AsyncEmptySession) -> None:
    s = empty_session
    await s.empty()


@pytest.mark.asyncio
async def test_one(one_session: AsyncOneSession) -> None:
    s = one_session
    result = await s.one()
    assert isinstance(result, One)
    assert result == (1.0, 1, True, "1", Enum.One)
    assert result == One(
        real=1.0, integer=1, boolean=True, string="1", enum=Enum.One
    )


@pytest.mark.asyncio
async def test_nested(nested_session: AsyncNestedSession) -> None:
    s = nested_session
    assert 1 == await s.Nested.level()
    assert 2 == await s.Nested.Nested.level()
    assert 3 == await s.Nested.Nested.Nested.level()
