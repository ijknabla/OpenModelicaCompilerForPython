from __future__ import annotations

import os
import types
from collections.abc import Generator
from contextlib import suppress
from typing import Any, Literal, NamedTuple, Union

import pytest

import omc4py.protocol
from omc4py import TypeName, VariableName
from omc4py.openmodelica import Component
from omc4py.string2 import (
    _is_component,
    _is_literal,
    _is_named_tuple,
    _is_none,
    _is_path_like,
    _is_primitive,
    _is_union,
    _StringableType,
)


class TestCase(NamedTuple):
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
    class _NamedTuple(NamedTuple):
        real: float
        integer: int
        boolean: bool
        string: str

    yield TestCase(
        _NamedTuple,
        type=_NamedTuple,
        is_named_tuple=True,
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
