from __future__ import annotations

from collections.abc import Generator
from pathlib import Path
from tempfile import TemporaryDirectory

import pytest

from omc4py import TypeName


@pytest.fixture
def strings() -> list[tuple[TypeName, str]]:
    return [
        (TypeName(name), f"class {name} end {name};")
        for name in ["A", "B", "C"]
    ]


@pytest.fixture
def paths(
    strings: list[tuple[TypeName, str]]
) -> Generator[list[tuple[TypeName, Path]], None, None]:
    with TemporaryDirectory() as _directory:
        directory = Path(_directory)
        result: list[tuple[TypeName, Path]] = []
        for name, string in strings:
            path = directory / f"{name}.mo"
            path.write_text(string)
            result.append((name, path))

        yield result
