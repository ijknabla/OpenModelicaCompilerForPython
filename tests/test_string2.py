from __future__ import annotations

import types
from collections.abc import Generator
from contextlib import suppress
from typing import Any, Literal, NamedTuple, Union

import pytest

from omc4py.string2 import SupportedType, _is_literal, _is_none, _is_union


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
        annotation=Literal[0],
        type=int,
        is_literal=True,
    )

    yield TestCase(
        annotation=Literal[0, 1, 2],
        type=int,
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


@pytest.mark.parametrize("test_case", _iter_test_cases())
def test_annotation_checker(test_case: TestCase) -> None:
    x = test_case
    assert _is_none(x.annotation) == x.is_none
    assert _is_literal(x.annotation) == x.is_literal
    assert _is_union(x.annotation) == x.is_union
