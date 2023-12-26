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
    unparse,
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
class Example:
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
        NamedTuple,
        type=NamedTuple,
        is_named_tuple=True,
        is_defined=True,
    )

    # record, enumeration
    yield Example(
        Record,
        type=Record,
        is_defined=True,
    )

    yield Example(
        Enumeration,
        type=Enumeration,
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


@pytest.mark.parametrize(
    "annotation," "s," "value,",
    [],
)
def test_parse(annotation: Any, s: str, value: Any) -> None:
    assert parse(annotation, s) == value
    assert parse(annotation, unparse(annotation, value)) == value
