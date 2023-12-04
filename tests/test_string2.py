from __future__ import annotations

import types
from collections.abc import Generator
from contextlib import suppress
from typing import Any, NamedTuple

import pytest

from omc4py.string2 import SupportedType, _is_none


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


@pytest.mark.parametrize("test_case", _iter_test_cases())
def test_annotation_checker(test_case: TestCase) -> None:
    x = test_case
    assert _is_none(x.annotation) == x.is_none
