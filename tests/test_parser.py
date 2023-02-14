import pytest

from omc4py.parser import parse_OMCValue


@pytest.mark.parametrize("literal", ["+1.0", "-1.0", "+1", "-1"])
def test_parse_primitives(literal: str) -> None:
    assert eval(literal) == parse_OMCValue(literal)
