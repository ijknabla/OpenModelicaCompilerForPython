import pytest

from . import Enum, one
from .aio import EmptySession, NestedSession, OneSession


@pytest.mark.asyncio
async def test_empty_session(empty_session: EmptySession) -> None:
    s = empty_session
    assert await s.empty() is None  # type: ignore


@pytest.mark.asyncio
async def test_one(one_session: OneSession) -> None:
    s = one_session
    result = await s.one()
    assert isinstance(result, one)
    assert result == (1.0, 1, True, "1", Enum.One)
    assert result == one(
        real=1.0, integer=1, boolean=True, string="1", enum=Enum.One
    )


@pytest.mark.asyncio
async def test_nested(nested_session: NestedSession) -> None:
    s = nested_session
    assert await s.level_1() == await s.Nested.level()
    assert await s.level_2() == await s.Nested.Nested.level()
    assert await s.level_3() == await s.Nested.Nested.Nested.level()
