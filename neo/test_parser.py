from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass
from itertools import product
from typing import Any, List, NamedTuple, Sequence, TypeVar, Union

import pytest
from typing_extensions import Annotated, Literal

from neo import TypeName, VariableName
from neo.modelica import alias, enumeration, external, record
from neo.parser import cast


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
            val = e.name  # type: ignore
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
