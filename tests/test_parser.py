from typing import Any

import pytest

from omc4py.parser import parse_OMCValue


@pytest.mark.parametrize(
    "literal, expected",
    [
        ("+1.0", +1.0),
        ("-1.0", -1.0),
        ("+1", +1),
        ("-1", -1),
    ],
)
def test_parse_primitives(literal: str, expected: Any) -> None:
    assert parse_OMCValue(literal) == expected
