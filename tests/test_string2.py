from __future__ import annotations

import collections.abc
import os
import types
import typing
from collections.abc import Generator
from contextlib import suppress
from typing import Any, Literal, NamedTuple, Union

import pytest

import omc4py.protocol
from omc4py import TypeName, VariableName
from omc4py.string2 import (
    SupportedType,
    _is_coroutine,
    _is_literal,
    _is_named_tuple,
    _is_none,
    _is_path_like,
    _is_primitive,
    _is_sequence,
    _is_union,
    get_ndim,
    get_type,
)


class TestCase(NamedTuple):
    annotation: Any
    type: SupportedType
    ndim: int = 0
    is_none: bool = False
    is_literal: bool = False
    is_union: bool = False
    is_primitive: bool = False
    is_path_like: bool = False
    is_sequence: bool = False
    is_coroutine: bool = False
    is_named_tuple: bool = False


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

    # NamedTuple
    class Output(NamedTuple):
        real: float
        integer: int
        boolean: bool
        string: str

    yield TestCase(
        Output,
        type=Output,
        is_named_tuple=True,
    )


@pytest.mark.parametrize("test_case", _iter_test_cases())
def test_annotation_checker(test_case: TestCase) -> None:
    x = test_case
    assert _is_none(x.annotation) == x.is_none
    assert _is_literal(x.annotation) == x.is_literal
    assert _is_union(x.annotation) == x.is_union
    assert _is_primitive(x.annotation) == x.is_primitive
    assert _is_path_like(x.annotation) == x.is_path_like
    assert _is_sequence(x.annotation) == x.is_sequence
    assert _is_coroutine(x.annotation) == x.is_coroutine
    assert _is_named_tuple(x.annotation) == x.is_named_tuple


@pytest.mark.parametrize("test_case", _iter_test_cases())
def test_type_and_ndim(test_case: TestCase) -> None:
    x = test_case
    assert get_type(x.annotation) is x.type
    assert get_ndim(x.annotation) == x.ndim
