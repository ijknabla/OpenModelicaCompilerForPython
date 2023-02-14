from typing import Any

import pytest
from numpy import array

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
        ('"text"', "text"),
        ("A.$a", TypeName("A.$a")),
        ("()", ()),
        ("(0, 1)", (0, 1)),
    ],
)
def test_parse_primitives(literal: str, expected: Any) -> None:
    assert parse_OMCValue(literal) == expected


@pytest.mark.parametrize(
    "literal, expected",
    [
        ("{}", []),
        ("{0, 1}", [0, 1]),
        ("{{0, 1}, {2, 3}}", [[0, 1], [2, 3]]),
    ],
)
def test_parse_arrays(literal: str, expected: Any) -> None:
    assert (parse_OMCValue(literal) == array(expected)).all()
