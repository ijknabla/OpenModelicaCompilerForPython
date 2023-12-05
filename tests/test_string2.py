from __future__ import annotations

import types
from collections.abc import Generator
from contextlib import suppress
from typing import Any, Literal, NamedTuple

import pytest

from omc4py.string2 import _is_literal, _is_none, _StringableType


class TestCase(NamedTuple):
    annotation: Any
    type: _StringableType
    ndim: int = 0
    is_none: bool = False
    is_literal: bool = False


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


@pytest.mark.parametrize("test_case", _iter_test_cases())
def test_annotation_checker(test_case: TestCase) -> None:
    x = test_case
    assert _is_none(x.annotation) == x.is_none
    assert _is_literal(x.annotation) == x.is_literal
