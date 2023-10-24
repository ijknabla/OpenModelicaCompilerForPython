from __future__ import annotations

from contextlib import ExitStack
from itertools import count
from typing import TYPE_CHECKING, Any, Optional

import pytest

from omc4py import TypeName, VariableName

if TYPE_CHECKING:
    from _pytest._code import ExceptionInfo


@pytest.mark.parametrize(
    "obj", ["a", "b", VariableName("a"), TypeName("a"), 0, 0.0, lambda: None]
)
def test_variablename(obj: Any) -> None:
    variablename: Optional[VariableName] = None
    expected_exception: ExceptionInfo[TypeError] | None = None

    with ExitStack() as stack:
        if not isinstance(obj, (str, VariableName, TypeName)):
            expected_exception = stack.enter_context(pytest.raises(TypeError))
        variablename = VariableName(obj)

    print(expected_exception.__class__)

    if variablename is not None:
        assert expected_exception is None

        assert VariableName(variablename) is variablename
        assert variablename == variablename
        if variablename == VariableName("a"):
            assert str(variablename) == "a"
        else:
            assert str(variablename) != "a"
        assert variablename != "a"
        assert isinstance(hash(variablename), int)
        assert str(variablename) in repr(variablename)
    else:
        assert expected_exception is not None
        (arg,) = expected_exception.value.args
        assert isinstance(arg, str)
        assert repr(obj) in arg
        assert repr(type(obj)) in arg


@pytest.mark.parametrize(
    "s",
    [
        "",
        "a",
        "a$",
        "aa",
        "''",
        "'a'",
        "'\\a'",
        "'aa'",
        "'\"'",
        "'a\"'",
        "$",
        "$$",
        "$a",
        "$aa",
    ],
)
def test_variablename_constructor(s: str) -> None:
    excepted_exception: ExceptionInfo[ValueError] | None = None
    with ExitStack() as stack:
        if not is_valid_identifer(s):
            excepted_exception = stack.enter_context(pytest.raises(ValueError))
        VariableName(s)

    if excepted_exception is not None:
        (arg,) = excepted_exception.value.args
        assert isinstance(arg, str)
        assert repr(s) in arg


def test_typename() -> None:
    typename = TypeName("A")
    assert TypeName(typename) is typename


def test_typename_combine() -> None:
    parts_a = ("A1", "A2")
    parts_b = ("B1", "B2")

    assert (TypeName(*parts_a) / TypeName(*parts_b)).parts == parts_a + parts_b


def test_typename_parts() -> None:
    typename = TypeName("A.B.C.D")

    assert typename.last_identifier == VariableName(typename.parts[-1])

    for i, parent in enumerate(typename.parents, start=1):
        assert parent.parts == typename.parts[:-i]


def test_absolute_typename() -> None:
    typename = TypeName("A.B.C.D")
    assert not typename.is_absolute
    assert typename.as_absolute().is_absolute

    assert f"{typename.as_absolute()}" == f".{typename}"
    assert typename.as_absolute().parts == (".", *typename.parts)

    assert typename.as_absolute().as_absolute() == typename.as_absolute()


NONDIGIT = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz")
DIGIT = set("0123456789")
Q_CHAR = set(" !#$%&()*+,-./:;<=>?@[]^{|}~")
S_ESCAPE = set(f"\\{c}" for c in "\"'?\\abfnrtv")


def is_valid_identifer(s: str) -> bool:
    if len(s) <= 1:
        head, body, tail = s[:1], "", ""
    else:
        head, body, tail = s[:1], s[1:-1], s[-1:]

    if head in NONDIGIT:
        if not set(body + tail):
            return True
        elif set(body + tail) <= (NONDIGIT | DIGIT):
            return True
        else:
            return False
    elif set(head + tail) == {"'"}:
        for i in count():
            if 2 <= len(body):
                if body[:2] in S_ESCAPE:
                    body = body[2:]
                    continue
            if 1 <= len(body):
                if body[:1] in NONDIGIT | DIGIT | Q_CHAR or (
                    0 < i and body[:1] == '"'
                ):
                    body = body[1:]
                    continue
            if not body:
                if i == 0:
                    return False
                else:
                    return True
            else:
                return False
    elif head == "$":
        if not set(body + tail):
            return True
        if set(body + tail) <= NONDIGIT | DIGIT:
            return True
        else:
            return False

    return False
