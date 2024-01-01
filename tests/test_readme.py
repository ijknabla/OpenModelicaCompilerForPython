import re

import pytest


@pytest.mark.parametrize(
    "source,",
    [],
)
def test_readme(source: str) -> None:
    for f in [_unquote]:
        source = f(source)

    exec(source)


def _unquote(s: str, /) -> str:
    return re.sub(r"(^\s+```python3?|```\s+$)", "", s)
