
from omc4py import (
    TypeName,
    open_session,
)
import pytest


def test_open_session():
    with open_session() as session:
        assert session is not None


@pytest.fixture
def session():
    with open_session() as session:
        yield session


def test_loadString(
    session  # fixture
):
    assert session.loadString("type MyEnumeration = enumeration(e, n, u, m);")
    assert session.isType("MyEnumeration")
    assert session.isEnumeration("MyEnumeration")
    assert session.loadString("package MyPackage end MyPackage;")
    assert session.isPackage("MyPackage")
    assert session.loadString("record MyRecord end MyRecord;")
    assert session.isRecord("MyRecord")
    assert session.loadString("function MyFunction end MyFunction;")
    assert session.isFunction("MyFunction")
    session.__check__()


def test_OpenModelica(
    session  # fixture
):
    assert session.isPackage("OpenModelica")
