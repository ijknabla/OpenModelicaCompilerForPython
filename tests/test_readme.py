from __future__ import annotations

import re
from collections.abc import Generator, Iterable
from pathlib import Path

import importlib_resources as resources
import pytest


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
    [
        """
```python3
#!/usr/bin/env python3
import omc4py

with omc4py.open_session() as session:
    print(session.getVersion())
```
        """,
        """
```python3
import omc4py

with omc4py.open_session(
    "C:/OpenModelica1.13.0-64bit/bin/omc.exe"
) as session:
    print(session.getVersion())
```
        """,
        """
```python3
import omc4py

with \
    omc4py.open_session(
        "C:/OpenModelica1.13.0-64bit/bin/omc.exe"
    ) as session_13, \
    omc4py.open_session(
        "C:/Program Files/OpenModelica1.14.0-64bit/bin/omc.exe"
    ) as session_14:

    print("v1.13.0:", session_13.getVersion())
    print("v1.14.0:", session_14.getVersion())
```
        """,
        '''
```python3
>>> from omc4py import *
>>> session = open_session()
>>> session.loadString("""
... package A
...     package B
...             package C
...             end C;
...     end B;
... end A;
... """)
True
>>> list(session.getClassNames("A", recursive=True))
[TypeName('A'), TypeName('A.B'), TypeName('A.B.C')]
>>>
>>>
>>> exit()  # session will be closed internally
```
        ''',
        """
```python3
>>> from omc4py import *
>>> session = open_session()
>>> session.__close__()
>>>
>>> exit()
```
        """,
        """
```python3
# Example for "timerTick" and "timerTock"
# in "OpenModelica.Scripting.Internal.Time"
from omc4py import open_session
from time import sleep

timer_index: int = 1

with open_session() as session:
    session.OpenModelica.Scripting.Internal.Time.timerTick(timer_index)

    sleep(0.1)

    # show elapsed time from last timerTick
    print(session.OpenModelica.Scripting.Internal.Time.timerTock(timer_index))
```
        """,
        """
```python3
import omc4py

with omc4py.open_session() as session:
    assert(session.loadModel("Modelica"))  # load MSL
```
        """,
        """
```python3
import omc4py

with omc4py.open_session() as session:
    assert(session.loadModel("Modelica", ["3.2.3"]))  # load MSL 3.2.3
```
        """,
        """
```python3
import omc4py

with omc4py.open_session() as session:
    assert(session.loadModel("Modelica"))
    for className in session.getClassNames("Modelica"):
        print(className)
```
        """,
        """
```python3
import omc4py

with omc4py.open_session() as session:
    assert(session.loadModel("Modelica"))
    for className in session.getClassNames("Modelica", recursive=True):
        print(className)  # many class names will be printed
```
        """,
        """
```python3
import omc4py

with omc4py.open_session() as session:
    assert(session.loadModel("Modelica", ["3.2.3"]))
    for component in session.getComponents("Modelica.Constants"):
        print(
            f"{component.className.last_identifier!s:<20}"
            f"{component.name!s:<15}"
            f"{component.comment!r}"
        )
```
        """,
        """
```python3
from omc4py import open_session

def doubtful_task(session):
    # session.doubtful_API1(...)
    # session.doubtful_API2(...)
    # session.doubtful_API3(...)
    session.__check__()

with open_session() as session:
    doubtful_task(session)
```
        """,
    ],
)
def test_readme(
    modelica_version: str,
    source: str,
) -> None:
    def _replace_modelica_version(s: str, /) -> str:
        return s.replace('"3.2.3"', f'"{modelica_version}"')

    for f in [
        _unquote,
        _replace_omc_to_none,
        _remove_prompt,
        _replace_modelica_version,
    ]:
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
