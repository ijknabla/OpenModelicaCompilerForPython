from __future__ import annotations

import os
import types
from collections.abc import Generator
from contextlib import suppress
from typing import Any, Literal, NamedTuple, Union

import pytest

import omc4py.protocol
from omc4py.string2 import (
    _is_literal,
    _is_none,
    _is_path_like,
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


@pytest.mark.parametrize("test_case", _iter_test_cases())
def test_annotation_checker(test_case: TestCase) -> None:
    x = test_case
    assert _is_none(x.annotation) == x.is_none
    assert _is_literal(x.annotation) == x.is_literal
    assert _is_union(x.annotation) == x.is_union
    assert _is_path_like(x.annotation) == x.is_path_like
