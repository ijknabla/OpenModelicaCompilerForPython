from __future__ import annotations

from contextlib import ExitStack
from pathlib import Path
from tempfile import TemporaryDirectory

import pytest

from omc4py import AsyncSession, Session, TypeName
from omc4py.exception import OMCError
from tests import OpenSession


@pytest.mark.skip
@pytest.mark.asyncio
async def test_check_settings(session: Session) -> None:
    s = session.asynchronous
    await s.checkSettings()


@pytest.mark.asyncio
async def test_load_file(
    open_session: OpenSession, paths: list[tuple[TypeName, Path]]
) -> None:
    s = open_session().asynchronous

    class_names: set[TypeName] = set()

    assert set(await s.getClassNames()) == class_names
    for name, path in paths:
        class_names.add(name)
        assert await s.loadFile(fileName=path)
        assert set(await s.getClassNames()) == class_names


@pytest.mark.asyncio
async def test_load_files(open_session: OpenSession) -> None:
    s = open_session().asynchronous

    assert await get_class_names(s) == set()

    with ExitStack() as stack:
        mos: list[str] = []
        for name in "ABC":
            mo = Path(stack.enter_context(TemporaryDirectory())) / "{name}.mo"
            mo.write_text(f"model {name} end {name};")
            mos.append(f"{mo}")
        assert await s.loadFiles(mos)

    assert await get_class_names(s) == {"A", "B", "C"}


@pytest.mark.asyncio
async def test_load_string(open_session: OpenSession) -> None:
    s = open_session().asynchronous

    assert await get_class_names(s) == set()

    assert await s.loadString("model A end A;")

    assert await get_class_names(s) == {"A"}


# # TOOD: EncryptedPackage features
# File not Found: /usr/bin/omc-semla/packagetool.
# Compile OpenModelica with Encryption support.
# - parseEncryptedPackage
# - loadEncryptedPackage
# - buildEncryptedPackage


@pytest.mark.asyncio
async def test_reload_model(open_session: OpenSession) -> None:
    session = open_session().asynchronous

    assert not await session.reloadClass("Modelica")
    with pytest.raises(OMCError):
        await session.__check__()

    assert await session.loadModel("Modelica")
    assert await session.reloadClass("Modelica")


async def get_class_names(
    session: AsyncSession, class_: TypeName | str | None = None
) -> set[str]:
    return set(map(str, await session.getClassNames(class_)))
