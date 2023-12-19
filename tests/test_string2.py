from __future__ import annotations

import collections.abc
import os
import types
import typing
from collections.abc import Generator
from contextlib import suppress
from dataclasses import dataclass
from typing import Any, Literal, Union

import pytest

import omc4py.protocol
from omc4py import TypeName, VariableName
from omc4py.modelica import enumeration, record
from omc4py.openmodelica import Component
from omc4py.string2 import (
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
    _StringableType,
    parse,
)


class NamedTuple(typing.NamedTuple):
    real: float
    integer: int
    boolean: bool
    string: str


@dataclass
class Record(record):
    __omc_class__ = TypeName("Record")
    real: float
    integer: int
    boolean: bool
    string: str


class Enumeration(enumeration):
    __omc_class__ = TypeName("Enumeration")
    a = 1
    b = 2
    c = 3


@dataclass(frozen=True)
class TestCase:
    annotation: Any
    type: _StringableType
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


def _iter_test_cases() -> Generator[TestCase, None, None]:
    # NoneType
    yield TestCase(
        annotation=None,
        type=None,
        is_none=True,
    )
    yield TestCase(
        annotation=type(None),
        type=None,
        is_none=True,
    )
    with suppress(AttributeError):
        yield TestCase(
            annotation=types.NoneType,
            type=None,
            is_none=True,
        )

    # Literal
    yield TestCase(
        annotation=Literal["a"],
        type=str,
        is_literal=True,
    )

    yield TestCase(
        annotation=Literal["a", "b"],
        type=str,
        is_literal=True,
    )

    # Union
    yield TestCase(
        annotation=Union[int, None],
        type=int,
        is_union=True,
    )
    with suppress(TypeError):
        yield TestCase(
            annotation=int | None,
            type=int,
            is_union=True,
        )

    # PathLike
    yield TestCase(
        annotation=omc4py.protocol.PathLike,
        type=str,
        is_path_like=True,
    )
    yield TestCase(
        annotation=omc4py.protocol.PathLike[str],
        type=str,
        is_path_like=True,
    )
    yield TestCase(
        annotation=os.PathLike,
        type=str,
        is_path_like=True,
    )
    with suppress(TypeError):
        yield TestCase(
            annotation=os.PathLike[str],
            type=str,
            is_path_like=True,
        )

    # Component
    yield TestCase(
        annotation=Component,
        type=Component,
        is_component=True,
        is_primitive=True,
    )

    # float, int
    yield TestCase(
        annotation=float,
        type=float,
        is_primitive=True,
    )
    yield TestCase(
        annotation=int,
        type=int,
        is_primitive=True,
    )

    # TypeName
    yield TestCase(
        annotation=TypeName,
        type=TypeName,
        is_primitive=True,
    )
    yield TestCase(
        annotation=Union[TypeName, str],
        type=TypeName,
        is_union=True,
    )
    with suppress(TypeError):
        yield TestCase(
            annotation=TypeName | str,
            type=TypeName,
            is_union=True,
        )

    # VariableName
    yield TestCase(
        annotation=VariableName,
        type=VariableName,
        is_primitive=True,
    )
    yield TestCase(
        annotation=Union[VariableName, str],
        type=VariableName,
        is_union=True,
    )
    with suppress(TypeError):
        yield TestCase(
            annotation=VariableName | str,
            type=VariableName,
            is_union=True,
        )

    # NamedTuple
    yield TestCase(
        NamedTuple,
        type=NamedTuple,
        is_named_tuple=True,
        is_defined=True,
    )

    # record, enumeration
    yield TestCase(
        Record,
        type=Record,
        is_defined=True,
    )

    yield TestCase(
        Enumeration,
        type=Enumeration,
        is_defined=True,
    )

    # Sequence
    yield TestCase(
        annotation=typing.List[int],
        type=int,
        ndim=1,
        is_sequence=True,
    )
    yield TestCase(
        annotation=typing.List[typing.List[int]],
        type=int,
        ndim=2,
        is_sequence=True,
    )
    yield TestCase(
        annotation=typing.Sequence[int],
        type=int,
        ndim=1,
        is_sequence=True,
    )
    yield TestCase(
        annotation=typing.Sequence[typing.Sequence[int]],
        type=int,
        ndim=2,
        is_sequence=True,
    )
    with suppress(TypeError):
        yield TestCase(
            annotation=list[int],
            type=int,
            ndim=1,
            is_sequence=True,
        )
        yield TestCase(
            annotation=list[list[int]],
            type=int,
            ndim=2,
            is_sequence=True,
        )
    with suppress(TypeError):
        yield TestCase(
            annotation=collections.abc.Sequence[int],
            type=int,
            ndim=1,
            is_sequence=True,
        )
        yield TestCase(
            annotation=collections.abc.Sequence[collections.abc.Sequence[int]],
            type=int,
            ndim=2,
            is_sequence=True,
        )

    # Coroutine
    yield TestCase(
        annotation=typing.Coroutine[None, None, int],
        type=int,
        is_coroutine=True,
    )
    yield TestCase(
        annotation=Union[int, typing.Coroutine[None, None, int]],
        type=int,
        is_union=True,
    )
    with suppress(TypeError):
        yield TestCase(
            annotation=collections.abc.Coroutine[None, None, int],
            type=int,
            is_coroutine=True,
        )
    with suppress(TypeError):
        yield TestCase(
            annotation=int | collections.abc.Coroutine[None, None, int],
            type=int,
            is_union=True,
        )


@pytest.mark.parametrize("test_case", _iter_test_cases())
def test_annotation_checker(test_case: TestCase) -> None:
    x = test_case
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


@pytest.mark.parametrize("test_case", _iter_test_cases())
def test_type_and_ndim(test_case: TestCase) -> None:
    x = test_case
    assert _get_type(x.annotation) is x.type
    assert _get_ndim(x.annotation) == x.ndim


@pytest.mark.parametrize(
    "annotation," "s," "value,",
    [
        (None, "", None),
        (float, "0.0", 0.0),
        (typing.List[float], "{0.0, 1.0}", [0.0, 1.0]),
        (typing.List[typing.List[float]], "{{0.0}, {1.0}}", [[0.0], [1.0]]),
        (int, "0", 0),
        (typing.List[int], "{0, 1}", [0, 1]),
        (typing.List[typing.List[int]], "{{0}, {1}}", [[0], [1]]),
        (bool, "false", False),
        (typing.List[bool], "{false, true}", [False, True]),
        (
            typing.List[typing.List[bool]],
            "{{false}, {true}}",
            [[False], [True]],
        ),
        (str, '""', ""),
        (typing.List[str], '{"a", "b"}', ["a", "b"]),
        (typing.List[typing.List[str]], '{{"a"}, {"b"}}', [["a"], ["b"]]),
        (TypeName, ".A.$A", TypeName(".A.$A")),
        (VariableName, "a", VariableName("a")),
        (
            typing.List[Component],
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
            Record,
            """
record Record
  Real=0.0;
  Integer=0;
  boolean=false;
  string="";
end Record;
            """,
            Record(real=0.0, integer=0, boolean=False, string=""),
        ),
        (Enumeration, "Enumeration.a", Enumeration.a),
        (
            NamedTuple,
            '(0.0, 0, false, "")',
            NamedTuple(real=0.0, integer=0, boolean=False, string=""),
        ),
    ],
)
def test_parse(annotation: Any, s: str, value: Any) -> None:
    assert parse(annotation, s) == value
