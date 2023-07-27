from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass
from itertools import product
from typing import Any, List, NamedTuple, Sequence, TypeVar, Union

import pytest
from typing_extensions import Annotated, Literal

from neo import TypeName, VariableName
from neo.modelica import alias, enumeration, external, record
from neo.openmodelica import Component
from neo.parser import cast, parse


@external(".OneTwo")
class OneTwo(enumeration):
    One = 1
    Two = 2


@external(".ScalarRecord")
@dataclass
class ScalarRecord(record):
    real: float
    integer: int
    boolean: bool
    string: str
    variable: VariableName
    type_: TypeName
    enumeration_: OneTwo


@external(".SequenceRecord")
@dataclass
class SequenceRecord(record):
    real: Sequence[float]
    integer: Sequence[int]
    boolean: Sequence[bool]
    string: Sequence[str]
    variable: Sequence[VariableName]
    type_: Sequence[TypeName]
    enumeration_: Sequence[OneTwo]
    record_: Sequence[ScalarRecord]


class ScalarNamedTuple(NamedTuple):
    real: float
    integer: int
    boolean: bool
    string: str
    variable: VariableName
    type_: TypeName
    enumeration_: OneTwo
    record_: ScalarRecord


class ListNamedTuple(NamedTuple):
    real: List[float]
    integer: List[int]
    boolean: List[bool]
    string: List[str]
    variable: List[VariableName]
    type_: List[TypeName]
    enumeration_: List[OneTwo]
    record_: List[SequenceRecord]


_T_name = TypeVar("_T_name", VariableName, TypeName)


def _iter_namelike_values(
    name_type: type[_T_name],
    literals: Iterable[str],
) -> Iterable[tuple[Any, _T_name | str, _T_name]]:
    for literal, val_is_str, use_union in product(
        literals, [False, True], [False, True]
    ):
        typ: Any
        if use_union:
            typ = Union[name_type, str]
        else:
            typ = name_type

        val: _T_name | str
        if val_is_str:
            val = literal
        else:
            val = name_type(literal)

        yield typ, val, name_type(literal)


def _iter_enumeration_values(
    enum: type[enumeration],
) -> Iterable[tuple[Any, enumeration | int | str, enumeration]]:
    literal: Any = Literal[
        tuple(e.value for e in enum) + tuple(e.name for e in enum)
    ]

    e: enumeration
    for e, val_type, use_union in product(
        enum, [enum, int, str], [False, True]
    ):
        typ: Any
        if use_union:
            typ = Union[enum, literal]
        else:
            typ = enum

        val: enumeration | int | str
        if val_type is enum:
            val = e
        elif val_type is int:
            val = e.value  # type: ignore
        elif val_type is str:
            val = e.name
        else:
            raise NotImplementedError(val)

        yield typ, val, e


@pytest.mark.parametrize(
    "typ, val, expected",
    [
        (Annotated[str, alias[Literal["from"]]], "from", "from"),
        *_iter_namelike_values(
            TypeName,
            [
                ".OpenModelica",
                ".OpenModelica.$Code",
                ".OpenModelica.$Code.TypeName",
            ],
        ),
        *_iter_namelike_values(
            VariableName,
            [
                "OpenModelica",
                "$Code",
                "VariableName",
            ],
        ),
        *_iter_enumeration_values(OneTwo),
    ],
)
def test_cast(typ: Any, val: Any, expected: Any) -> None:
    assert cast(typ, val) == expected


@pytest.mark.parametrize(
    "typ, literal, expected",
    [
        (None, "", None),
        (type(None), "", None),
        (float, "1", 1),
        (float, "+2", +2),
        (float, "-3", -3),
        (float, "4.1", 4.1),
        (float, "4.2e1", 42),
        (float, "4.3e+1", 43),
        (float, "4.4e-1", 0.44),
        (List[float], "{}", []),
        (List[float], "{1}", [1]),
        (List[List[float]], "{{}}", [[]]),
        (List[List[float]], "{{1}}", [[1]]),
        (int, "1", 1),
        (int, "+2", +2),
        (int, "-3", -3),
        (List[int], "{}", []),
        (List[int], "{1}", [1]),
        (List[List[int]], "{{}}", [[]]),
        (List[List[int]], "{{1}}", [[1]]),
        (bool, "true", True),
        (bool, "false", False),
        (List[bool], "{}", []),
        (List[bool], "{true}", [True]),
        (List[bool], "{false}", [False]),
        (List[List[bool]], "{{}}", [[]]),
        (List[List[bool]], "{{true}}", [[True]]),
        (List[List[bool]], "{{false}}", [[False]]),
        (str, '""', ""),
        (str, '"a"', "a"),
        (List[str], "{}", []),
        (List[str], '{"a"}', ["a"]),
        (List[List[str]], "{{}}", [[]]),
        (List[List[str]], '{{"a"}}', [["a"]]),
        (VariableName, "$", VariableName("$")),
        (VariableName, "x", VariableName("x")),
        (List[VariableName], "{}", []),
        (List[VariableName], "{x}", [VariableName("x")]),
        (List[List[VariableName]], "{{}}", [[]]),
        (List[List[VariableName]], "{{x}}", [[VariableName("x")]]),
        (TypeName, "$", TypeName("$")),
        (TypeName, ".x.$", TypeName(".x.$")),
        (List[TypeName], "{}", []),
        (List[TypeName], "{x.y}", [TypeName("x.y")]),
        (List[List[TypeName]], "{{}}", [[]]),
        (List[List[TypeName]], "{{.x.y}}", [[TypeName(".x.y")]]),
        (
            List[Component],
            '{{x,y,"","public",true,false,false,false,"constant","inner","input",{}}}',  # noqa: E501
            [
                Component(
                    className=TypeName("x"),
                    name=VariableName("y"),
                    comment="",
                    protected="public",
                    isFinal=True,
                    isFlow=False,
                    isStream=False,
                    isReplaceable=False,
                    variability="constant",
                    innerOuter="inner",
                    inputOutput="input",
                    dimensions=[],
                ),
            ],
        ),
        (
            List[Component],
            '{{x.y,z,"","protected",false,true,false,false,"parameter","outer","output",{}}}',  # noqa: E501
            [
                Component(
                    className=TypeName("x.y"),
                    name=VariableName("z"),
                    comment="",
                    protected="protected",
                    isFinal=False,
                    isFlow=True,
                    isStream=False,
                    isReplaceable=False,
                    variability="parameter",
                    innerOuter="outer",
                    inputOutput="output",
                    dimensions=[],
                ),
            ],
        ),
        (
            List[Component],
            '{{$,$,"","public",false,false,true,false,"discrete","none","unspecified",{}}}',  # noqa: E501
            [
                Component(
                    className=TypeName("$"),
                    name=VariableName("$"),
                    comment="",
                    protected="public",
                    isFinal=False,
                    isFlow=False,
                    isStream=True,
                    isReplaceable=False,
                    variability="discrete",
                    innerOuter="none",
                    inputOutput="unspecified",
                    dimensions=[],
                ),
            ],
        ),
        (
            List[Component],
            (
                '{{.$,$,"","protected",false,false,false,true,"unspecified","none","unspecified",{}}}'  # noqa: E501
            ),
            [
                Component(
                    className=TypeName(".$"),
                    name=VariableName("$"),
                    comment="",
                    protected="protected",
                    isFinal=False,
                    isFlow=False,
                    isStream=False,
                    isReplaceable=True,
                    variability="unspecified",
                    innerOuter="none",
                    inputOutput="unspecified",
                    dimensions=[],
                ),
            ],
        ),
        (
            ScalarNamedTuple,
            (
                """
(
    1,1,true,"1",One,One,OneTwo.One,
    record ScalarRecord
        real=1,integer=1,boolean=true,string="1",
        variable=One,type_=One,enumeration_=OneTwo.One
    end ScalarRecord;
)
                """
            ),
            ScalarNamedTuple(
                1.0,
                1,
                True,
                "1",
                VariableName("One"),
                TypeName("One"),
                OneTwo.One,
                ScalarRecord(
                    1.0,
                    1,
                    True,
                    "1",
                    VariableName("One"),
                    TypeName("One"),
                    OneTwo.One,
                ),
            ),
        ),
        (
            ListNamedTuple,
            "({},{},{},{},{},{},{},{})",
            ListNamedTuple([], [], [], [], [], [], [], []),
        ),
        (
            ListNamedTuple,
            "({1},{},{},{},{},{},{},{})",
            ListNamedTuple([1.0], [], [], [], [], [], [], []),
        ),
        (
            ListNamedTuple,
            "({},{1},{},{},{},{},{},{})",
            ListNamedTuple([], [1], [], [], [], [], [], []),
        ),
        (
            ListNamedTuple,
            "({},{},{true},{},{},{},{},{})",
            ListNamedTuple([], [], [True], [], [], [], [], []),
        ),
        (
            ListNamedTuple,
            '({},{},{},{"1"},{},{},{},{})',
            ListNamedTuple([], [], [], ["1"], [], [], [], []),
        ),
        (
            ListNamedTuple,
            "({},{},{},{},{One},{},{},{})",
            ListNamedTuple(
                [],
                [],
                [],
                [],
                [VariableName("One")],
                [],
                [],
                [],
            ),
        ),
        (
            ListNamedTuple,
            "({},{},{},{},{},{One},{},{})",
            ListNamedTuple(
                [],
                [],
                [],
                [],
                [],
                [TypeName("One")],
                [],
                [],
            ),
        ),
        (
            ListNamedTuple,
            "({},{},{},{},{},{},{OneTwo.One},{})",
            ListNamedTuple(
                [],
                [],
                [],
                [],
                [],
                [],
                [OneTwo.One],
                [],
            ),
        ),
        (
            ListNamedTuple,
            """
(
    {},{},{},{},{},{},{},
    {
        record SequenceRecord
            real={},integer={},boolean={},string={},
            variable={},type_={},enumeration_={},record_={}
        end SequenceRecord;
    }
)
            """,
            ListNamedTuple(
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                [
                    SequenceRecord(
                        [],
                        [],
                        [],
                        [],
                        [],
                        [],
                        [],
                        [],
                    )
                ],
            ),
        ),
    ],
)
def test_parse(typ: Any, literal: str, expected: Any) -> None:
    assert parse(typ, literal) == expected