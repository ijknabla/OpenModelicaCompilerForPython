from typing import Any

import pytest

from omc4py.classes import TypeName
from omc4py.parser import parse_OMCValue


@pytest.mark.parametrize(
    "literal, expected",
    [
        ("+1.0", +1.0),
        ("-1.0", -1.0),
        ("+1", +1),
        ("-1", -1),
        ("true", True),
        ("false", False),
        ("A.$a", TypeName("A.$a")),
    ],
)
def test_parse_primitives(literal: str, expected: Any) -> None:
    assert parse_OMCValue(literal) == expected
