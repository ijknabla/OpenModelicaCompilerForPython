from __future__ import annotations

import collections.abc
import os
import types
import typing
from collections.abc import Generator, Iterable
from contextlib import suppress
from dataclasses import dataclass
from itertools import product
from typing import Any, List, Literal, NamedTuple, Sequence, TypeVar, Union

import pytest

import omc4py.protocol
from omc4py import TypeName, VariableName
from omc4py.modelica import enumeration, record
from omc4py.openmodelica import Component
from omc4py.parser import (
    _get_ndim,
    _get_type,
    _is_component,
    _is_coroutine,
    _is_defined,
    _is_literal,
    _is_named_tuple,
    _is_none,
    _is_path_like,
    _is_primitive,
    _is_sequence,
    _is_union,
    _ScalarType,
    parse,
    unparse,
)
from omc4py.v_1_22.OpenModelica.Scripting import (  # NOTE: update to latest
    ErrorKind,
    ErrorLevel,
    ErrorMessage,
    SourceInfo,
)


class OneTwo(enumeration):
    __omc_class__ = TypeName("OneTwo")

    One = 1
    Two = 2


@dataclass
class SingleRecord(record):
    __omc_class__ = TypeName("SingleRecord")

    a: int


@dataclass
class ScalarRecord(record):
    __omc_class__ = TypeName("ScalarRecord")

    real: float
    integer: int
    boolean: bool
    string: str
    variable: VariableName
    type_: TypeName
    enumeration_: OneTwo


@dataclass
class SequenceRecord(record):
    __omc_class__ = TypeName("SequenceRecord")

    real: Sequence[float]
    integer: Sequence[int]
    boolean: Sequence[bool]
    string: Sequence[str]
    variable: Sequence[VariableName]
    type_: Sequence[TypeName]
    enumeration_: Sequence[OneTwo]
    record_: Sequence[ScalarRecord]


class TwoInt(NamedTuple):
    i: int
    j: int


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


@dataclass(frozen=True)
class Example:
    annotation: Any
    type: _ScalarType
    ndim: int = 0
    is_none: bool = False
    is_literal: bool = False
    is_union: bool = False
    is_path_like: bool = False
    is_component: bool = False
    is_primitive: bool = False
    is_named_tuple: bool = False
    is_defined: bool = False
    is_sequence: bool = False
    is_coroutine: bool = False


def _iter_examples() -> Generator[Example, None, None]:
    # NoneType
    yield Example(
        annotation=None,
        type=None,
        is_none=True,
    )
    yield Example(
        annotation=type(None),
        type=None,
        is_none=True,
    )
    with suppress(AttributeError):
        yield Example(
            annotation=types.NoneType,
            type=None,
            is_none=True,
        )

    # Literal
    yield Example(
        annotation=Literal["a"],
        type=str,
        is_literal=True,
    )

    yield Example(
        annotation=Literal["a", "b"],
        type=str,
        is_literal=True,
    )

    # Union
    yield Example(
        annotation=Union[int, None],
        type=int,
        is_union=True,
    )
    with suppress(TypeError):
        yield Example(
            annotation=int | None,
            type=int,
            is_union=True,
        )
    yield Example(
        annotation=Union[typing.Sequence[int], None],
        type=int,
        ndim=1,
        is_union=True,
    )

    # PathLike
    yield Example(
        annotation=omc4py.protocol.PathLike,
        type=str,
        is_path_like=True,
    )
    yield Example(
        annotation=omc4py.protocol.PathLike[str],
        type=str,
        is_path_like=True,
    )
    yield Example(
        annotation=os.PathLike,
        type=str,
        is_path_like=True,
    )
    with suppress(TypeError):
        yield Example(
            annotation=os.PathLike[str],
            type=str,
            is_path_like=True,
        )

    # Component
    yield Example(
        annotation=Component,
        type=Component,
        is_component=True,
        is_primitive=True,
    )

    # float, int
    yield Example(
        annotation=float,
        type=float,
        is_primitive=True,
    )
    yield Example(
        annotation=int,
        type=int,
        is_primitive=True,
    )

    # TypeName
    yield Example(
        annotation=TypeName,
        type=TypeName,
        is_primitive=True,
    )
    yield Example(
        annotation=Union[TypeName, str],
        type=TypeName,
        is_union=True,
    )
    with suppress(TypeError):
        yield Example(
            annotation=TypeName | str,
            type=TypeName,
            is_union=True,
        )

    # VariableName
    yield Example(
        annotation=VariableName,
        type=VariableName,
        is_primitive=True,
    )
    yield Example(
        annotation=Union[VariableName, str],
        type=VariableName,
        is_union=True,
    )
    with suppress(TypeError):
        yield Example(
            annotation=VariableName | str,
            type=VariableName,
            is_union=True,
        )

    # NamedTuple
    yield Example(
        ScalarNamedTuple,
        type=ScalarNamedTuple,
        is_named_tuple=True,
        is_defined=True,
    )

    # record, enumeration
    yield Example(
        ScalarRecord,
        type=ScalarRecord,
        is_defined=True,
    )

    yield Example(
        OneTwo,
        type=OneTwo,
        is_defined=True,
    )

    # Sequence
    yield Example(
        annotation=typing.List[int],
        type=int,
        ndim=1,
        is_sequence=True,
    )
    yield Example(
        annotation=typing.List[typing.List[int]],
        type=int,
        ndim=2,
        is_sequence=True,
    )
    yield Example(
        annotation=typing.Sequence[int],
        type=int,
        ndim=1,
        is_sequence=True,
    )
    yield Example(
        annotation=typing.Sequence[typing.Sequence[int]],
        type=int,
        ndim=2,
        is_sequence=True,
    )
    with suppress(TypeError):
        yield Example(
            annotation=list[int],
            type=int,
            ndim=1,
            is_sequence=True,
        )
        yield Example(
            annotation=list[list[int]],
            type=int,
            ndim=2,
            is_sequence=True,
        )
    with suppress(TypeError):
        yield Example(
            annotation=collections.abc.Sequence[int],
            type=int,
            ndim=1,
            is_sequence=True,
        )
        yield Example(
            annotation=collections.abc.Sequence[collections.abc.Sequence[int]],
            type=int,
            ndim=2,
            is_sequence=True,
        )

    # Coroutine
    yield Example(
        annotation=typing.Coroutine[None, None, int],
        type=int,
        is_coroutine=True,
    )
    yield Example(
        annotation=Union[int, typing.Coroutine[None, None, int]],
        type=int,
        is_union=True,
    )
    with suppress(TypeError):
        yield Example(
            annotation=collections.abc.Coroutine[None, None, int],
            type=int,
            is_coroutine=True,
        )
    with suppress(TypeError):
        yield Example(
            annotation=int | collections.abc.Coroutine[None, None, int],
            type=int,
            is_union=True,
        )


@pytest.mark.parametrize("example", _iter_examples())
def test_annotation_checker(example: Example) -> None:
    x = example
    assert _is_none(x.annotation) == x.is_none
    assert _is_literal(x.annotation) == x.is_literal
    assert _is_union(x.annotation) == x.is_union
    assert _is_path_like(x.annotation) == x.is_path_like
    assert _is_component(x.annotation) == x.is_component
    assert _is_primitive(x.annotation) == x.is_primitive
    assert _is_named_tuple(x.annotation) == x.is_named_tuple
    assert _is_defined(x.annotation) == x.is_defined
    assert _is_sequence(x.annotation) == x.is_sequence
    assert _is_coroutine(x.annotation) == x.is_coroutine


@pytest.mark.parametrize("example", _iter_examples())
def test_type_and_ndim(example: Example) -> None:
    x = example
    assert _get_type(x.annotation) is x.type
    assert _get_ndim(x.annotation) == x.ndim


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
    literal: Any = Literal.__getitem__(
        tuple(e.value for e in enum) + tuple(e.name for e in enum)
    )

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
    assert parse(typ, unparse(typ, val)) == expected


@pytest.mark.parametrize(
    "annotation," "literal," "expected,",
    [
        (None, "", None),
        (type(None), "", None),
        (float, "0.0", 0.0),
        (float, "1", 1),
        (float, "+1.0", +1.0),
        (float, "-1.0", -1.0),
        (float, "+2", +2),
        (float, "-3", -3),
        (float, "4.1", 4.1),
        (float, "4.2e1", 42),
        (float, "4.3e+1", 43),
        (float, "4.4e-1", 0.44),
        (List[float], "{}", []),
        (List[float], "{1}", [1]),
        (List[float], "{0.0, 1.0}", [0.0, 1.0]),
        (List[List[float]], "{{}}", [[]]),
        (List[List[float]], "{{1}}", [[1]]),
        (List[List[float]], "{{0.0}, {1.0}}", [[0.0], [1.0]]),
        (int, "0", 0),
        (int, "1", 1),
        (int, "+1", +1),
        (int, "-1", -1),
        (int, "+2", +2),
        (int, "-3", -3),
        (List[int], "{}", []),
        (List[int], "{1}", [1]),
        (List[int], "{0, 1}", [0, 1]),
        (List[List[int]], "{{}}", [[]]),
        (List[List[int]], "{{1}}", [[1]]),
        (List[List[int]], "{{0}, {1}}", [[0], [1]]),
        (List[List[int]], "{{0, 1}, {2, 3}}", [[0, 1], [2, 3]]),
        (bool, "true", True),
        (bool, "false", False),
        (List[bool], "{}", []),
        (List[bool], "{true}", [True]),
        (List[bool], "{false}", [False]),
        (List[bool], "{false, true}", [False, True]),
        (List[List[bool]], "{{}}", [[]]),
        (List[List[bool]], "{{true}}", [[True]]),
        (List[List[bool]], "{{false}}", [[False]]),
        (List[List[bool]], "{{false}, {true}}", [[False], [True]]),
        (str, '""', ""),
        (str, '"a"', "a"),
        (str, '"text"', "text"),
        (List[str], "{}", []),
        (List[str], '{"a"}', ["a"]),
        (List[str], '{"a", "b"}', ["a", "b"]),
        (List[List[str]], "{{}}", [[]]),
        (List[List[str]], '{{"a"}}', [["a"]]),
        (List[List[str]], '{{"a"}, {"b"}}', [["a"], ["b"]]),
        (VariableName, "$", VariableName("$")),
        (VariableName, "a", VariableName("a")),
        (VariableName, "x", VariableName("x")),
        (List[VariableName], "{}", []),
        (List[VariableName], "{x}", [VariableName("x")]),
        (List[List[VariableName]], "{{}}", [[]]),
        (List[List[VariableName]], "{{x}}", [[VariableName("x")]]),
        (TypeName, "$", TypeName("$")),
        (TypeName, ".x.$", TypeName(".x.$")),
        (TypeName, ".A.$A", TypeName(".A.$A")),
        (TypeName, "A.$a", TypeName("A.$a")),
        (List[TypeName], "{}", []),
        (List[TypeName], "{x.y}", [TypeName("x.y")]),
        (List[List[TypeName]], "{{}}", [[]]),
        (List[List[TypeName]], "{{.x.y}}", [[TypeName(".x.y")]]),
        (List[Component], "{}", []),
        (
            List[Component],
            """
{{.A,a,"","public",false,false,false,false,"unspecified","none","unspecified",{:,:}}}
            """,
            [
                Component(
                    className=TypeName(".A"),
                    name=VariableName("a"),
                    comment="",
                    protected="public",
                    isFinal=False,
                    isFlow=False,
                    isStream=False,
                    isReplaceable=False,
                    variability="unspecified",
                    innerOuter="none",
                    inputOutput="unspecified",
                    dimensions=[":", ":"],
                )
            ],
        ),
        (
            List[Component],
            """\
{
    {
        className,
        name,
        "comment",
        "protected",
        true, true, true, true,
        "parameter",
        "inner",
        "input",
        {:}
    }
}""",
            [
                Component(
                    className=TypeName("className"),
                    name=VariableName("name"),
                    comment="comment",
                    protected="protected",
                    isFinal=True,
                    isFlow=True,
                    isStream=True,
                    isReplaceable=True,
                    variability="parameter",
                    innerOuter="inner",
                    inputOutput="input",
                    dimensions=[":"],
                )
            ],
        ),
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
            SingleRecord,
            "record SingleRecord a = 0 end SingleRecord;",
            SingleRecord(a=0),
        ),
        (
            ScalarRecord,
            """
record ScalarRecord
  real=1.0,
  integer=1,
  boolean=true,
  string="one",
  variable=one,
  type_=One,
  enumeration_=OneTwo.One
end ScalarRecord;
            """,
            ScalarRecord(
                real=1.0,
                integer=1,
                boolean=True,
                string="one",
                variable=VariableName("one"),
                type_=TypeName("One"),
                enumeration_=OneTwo.One,
            ),
        ),
        (
            ScalarRecord,  # Check reversed order
            """
record ScalarRecord
  enumeration_=OneTwo.One,
  type_=One,
  variable=one,
  string="one",
  boolean=true,
  integer=1,
  real=1.0
end ScalarRecord;
            """,
            ScalarRecord(
                real=1.0,
                integer=1,
                boolean=True,
                string="one",
                variable=VariableName("one"),
                type_=TypeName("One"),
                enumeration_=OneTwo.One,
            ),
        ),
        (TwoInt, "(0, 1)", (0, 1)),
        (
            ScalarNamedTuple,
            (
                """
(
    1,1,true,"1",One,One,OneTwo.One,
    record ScalarRecord
        real=1,integer=1,boolean=true,string="1",variable=One,type_=One,enumeration_=OneTwo.One
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
        (
            SourceInfo,
            """\
record OpenModelica.Scripting.SourceInfo
    filename = "filename",
    readonly=false,
    lineStart=1,
    columnStart=2,
    lineEnd=3,
    columnEnd=4
end OpenModelica.Scripting.SourceInfo;
""",
            SourceInfo(
                fileName="filename",
                readonly=False,
                lineStart=1,
                columnStart=2,
                lineEnd=3,
                columnEnd=4,
            ),
        ),
        (
            SourceInfo,
            """\
record OpenModelica.Scripting.SourceInfo
    fileName="fileName",
    readonly=false,
    lineStart=1,
    columnStart=2,
    lineEnd=3,
    columnEnd=4
end OpenModelica.Scripting.SourceInfo;
""",
            SourceInfo(
                fileName="fileName",
                readonly=False,
                lineStart=1,
                columnStart=2,
                lineEnd=3,
                columnEnd=4,
            ),
        ),
        (
            List[ErrorMessage],
            """
{
  record OpenModelica.Scripting.ErrorMessage
    info =
      record OpenModelica.Scripting.SourceInfo
        filename = "",
        readonly = false,
        lineStart = 0,
        columnStart = 0,
        lineEnd = 0,
        columnEnd = 0
      end OpenModelica.Scripting.SourceInfo;,
    message = "",
    kind = .OpenModelica.Scripting.ErrorKind.syntax,
    level = .OpenModelica.Scripting.ErrorLevel.internal,
    id = 0
  end OpenModelica.Scripting.ErrorMessage;
}
            """,
            [
                ErrorMessage(
                    info=SourceInfo(
                        fileName="",
                        readonly=False,
                        lineStart=0,
                        columnStart=0,
                        lineEnd=0,
                        columnEnd=0,
                    ),
                    message="",
                    kind=ErrorKind.syntax,
                    level=ErrorLevel.internal,
                    id=0,
                )
            ],
        ),
    ],
)
def test_parse(annotation: Any, literal: str, expected: Any) -> None:
    assert parse(annotation, literal) == expected
    assert parse(annotation, unparse(annotation, expected)) == expected
