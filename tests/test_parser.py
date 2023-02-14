from typing import Any

import pytest
from numpy import array

from omc4py.classes import TypeName, VariableName
from omc4py.parser import parse_components
from omc4py.parser import parse_OMCValue__v_1_13 as parse_OMCValue
from omc4py.parser.visitor import ComponentTuple


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
        ("record A a = 0 end A;", {"a": 0}),
        ("record A a = 0, b = 1 end A;", {"a": 0, "b": 1}),
        (
            """\
record OpenModelica.Scripting.SourceInfo
    filename = "filename"
end OpenModelica.Scripting.SourceInfo;
""",
            {"fileName": "filename"},
        ),
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


@pytest.mark.parametrize(
    "literal, expected",
    [
        ("{}", []),
        (
            """\
{
    {
        className,
        name,
        "comment",
        "protected",
        true, true, true, true,
        "variability",
        "innerOuter",
        "inputOutput",
        {:}
    }
}""",
            [
                ComponentTuple(
                    className=TypeName("className"),
                    name=VariableName("name"),
                    comment="comment",
                    protected="protected",
                    isFinal=True,
                    isFlow=True,
                    isStream=True,
                    isReplaceable=True,
                    variability="variability",
                    innerOuter="innerOuter",
                    inputOutput="inputOutput",
                    dimensions=(":",),
                )
            ],
        ),
    ],
)
def test_parse_omc_component_array(literal: str, expected: Any) -> None:
    assert parse_components(literal) == expected
