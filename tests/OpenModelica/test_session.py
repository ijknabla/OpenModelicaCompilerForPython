import pytest

from omc4py import AsyncSession, TypeName
from tests import OpenSession


@pytest.mark.asyncio
async def test_load_string(open_session: OpenSession) -> None:
    s = open_session().asynchronous

    assert await get_class_names(s) == set()
    assert await s.loadString("model A end A;")
    assert await get_class_names(s) == {"A"}


async def get_class_names(
    session: AsyncSession, class_: TypeName | str | None = None
) -> set[str]:
    return set(map(str, await session.getClassNames(class_)))
