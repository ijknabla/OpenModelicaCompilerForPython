import re
from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "source,",
    [],
)
def test_readme(source: str) -> None:
    for f in [_unquote, _replace_omc_to_none, _remove_prompt]:
        source = f(source)

    exec(source, {"exit": lambda: None})


def _unquote(s: str, /) -> str:
    return re.sub(r"(^\s+```python3?|```\s+$)", "", s)


def _replace_omc_to_none(s: str, /) -> str:
    missing_omc_exe = set(
        s
        for s in map(
            lambda m: m.group(0),
            re.finditer(
                r"C:/(Program Files/)?"
                r"OpenModelica\d+\.\d+\.\d+-64bit/bin/omc.exe",
                s,
            ),
        )
        if not Path(s).exists()
    )
    if not missing_omc_exe:
        return s
    else:
        pattern = "(" + "|".join(map(re.escape, sorted(missing_omc_exe))) + ")"
        return re.sub("|".join(q + pattern + q for q in ['"', "'"]), "None", s)


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
