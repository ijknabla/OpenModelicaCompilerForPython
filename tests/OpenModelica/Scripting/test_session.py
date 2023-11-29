from __future__ import annotations

from pathlib import Path

import pytest

from omc4py import TypeName
from tests import OpenSession


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

    added, fileNames = zip(*paths)

    assert set(await s.getClassNames()) == class_names

    class_names.update(added)
    assert await s.loadFiles(fileNames=fileNames)

    assert set(await s.getClassNames()) == class_names
