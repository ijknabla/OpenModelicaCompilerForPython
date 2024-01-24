from __future__ import annotations

from asyncio import gather
from pathlib import Path
from tempfile import TemporaryDirectory

import pytest

from omc4py import Session, TypeName
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
async def test_load_files(
    open_session: OpenSession, paths: list[tuple[TypeName, Path]]
) -> None:
    s = open_session().asynchronous

    class_names: set[TypeName] = set()

    assert set(await s.getClassNames()) == class_names

    name: tuple[TypeName, ...]
    path: tuple[Path, ...]
    name, path = zip(*paths)

    class_names.update(name)
    assert await s.loadFiles(fileNames=path)

    assert set(await s.getClassNames()) == class_names


@pytest.mark.asyncio
async def test_reload_class(open_session: OpenSession) -> None:
    """
    omc4py/v_1_22/OpenModelica/Scripting/__init__.py:323
    """
    session = open_session().asynchronous

    assert not await session.reloadClass("Modelica")
    with pytest.raises(OMCError):
        await session.__check__()

    assert await session.loadModel("Modelica")
    assert await session.reloadClass("Modelica")


@pytest.mark.asyncio
async def test_load_string(
    open_session: OpenSession, strings: list[tuple[TypeName, str]]
) -> None:
    """
    omc4py/v_1_22/OpenModelica/Scripting/__init__.py:365
    """
    s = open_session().asynchronous

    class_names: set[TypeName] = set()

    assert set(await s.getClassNames()) == class_names
    for name, string in strings:
        class_names.add(name)
        assert await s.loadString(data=string)
        assert set(await s.getClassNames()) == class_names


# # TOOD: EncryptedPackage features
# File not Found: /usr/bin/omc-semla/packagetool.
# Compile OpenModelica with Encryption support.
# - parseEncryptedPackage
# - loadEncryptedPackage
# - buildEncryptedPackage


@pytest.mark.asyncio
async def test_directory_exists(session: Session) -> None:
    """
    omc4py/v_1_22/OpenModelica/Scripting/__init__.py:2516
    """
    s = session.asynchronous

    with TemporaryDirectory() as temp:
        paths = [Path(temp, name) for name in "ABCD"]

        async def check() -> None:
            assert (
                await gather(
                    *(s.directoryExists(dirName=path) for path in paths)
                )
            ) == [path.exists() for path in paths]

        await check()

        for path in paths:
            path.mkdir()
            await check()
