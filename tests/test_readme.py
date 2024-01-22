from __future__ import annotations

import logging
import re
from collections.abc import Callable, Generator, Iterable
from functools import reduce
from pathlib import Path

import importlib_resources as resources
import pytest

logger = logging.getLogger()


def _iter_readme_lines() -> Generator[str, None, None]:
    with resources.files("tests").joinpath("../README.md").open(
        "r", encoding="utf-8"
    ) as f:
        yield from f


def _split_code_block(
    xs: Iterable[str],
) -> Generator[Generator[str, None, None], None, None]:
    iterator = iter(xs)

    begin = re.compile(r"^\s*```python\d*\s*$")
    end = re.compile(r"^\s*```\s*$")

    def _iter_code_block() -> Generator[str, None, None]:
        for line in iterator:
            if end.match(line) is not None:
                return
            yield line

    for line in iterator:
        if begin.match(line) is not None:
            yield _iter_code_block()


@pytest.mark.parametrize(
    "source,",
    map("".join, _split_code_block(_iter_readme_lines())),
)
def test_readme(
    modelica_version: str,
    source: str,
) -> None:
    logger.info(f"'''\n{source}'''")

    fs: list[Callable[[str], str]]
    fs = [
        _remove_prompt,
        lambda s: re.sub(
            r'"(?P<path>C:/(Program Files/)?'
            r'OpenModelica\d+\.\d+\.\d+-64bit/bin/omc.exe")',
            lambda m: m.group(0)
            if Path(str(m.group("path"))).exists()
            else "None",
            s,
        ),
        lambda s: re.sub(r'"3.2.3"', f'"{modelica_version}"', s),
    ]

    exec(reduce(lambda s, f: f(s), fs, source), {"exit": lambda: None})


def _remove_prompt(s: str, /) -> str:
    lines = list(
        map(
            lambda m: m.group("line"),
            re.finditer(r"^(>>>|\.\.\.) (?P<line>.*\n)", s, re.MULTILINE),
        )
    )
    if not lines:
        return s
    else:
        return "".join(lines)
