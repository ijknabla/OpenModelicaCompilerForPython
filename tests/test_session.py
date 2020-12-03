
from omc4py import (
    TypeName,
    open_session,
)
import pytest


@pytest.mark.dependency()
def test_open_session():
    with open_session() as session:
        assert session is not None
        session.__check__()


@pytest.fixture
def session():
    with open_session() as session:
        yield session
        session.__check__()


@pytest.mark.dependency(depends=["test_open_session"])
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


@pytest.mark.dependency(depends=["test_open_session"])
def test_getClassNames(
    session  # fixture
):
    assert session.loadString(
        """
package Test_getClassNames
end Test_getClassNames;
        """
    )
    assert session.isPackage("Test_getClassNames")
    assert 0 == len(session.getClassNames("Test_getClassNames"))

    assert session.loadString(
        """
within Test_getClassNames;
type C = enumeration(c);
        """
    )
    assert (
        session.getClassNames("Test_getClassNames") == [
            TypeName("C"),
        ]
    ).all()
    assert (
        session.getClassNames("Test_getClassNames", sort=True) == [
            TypeName("C"),
        ]
    ).all()
    assert (
        session.getClassNames("Test_getClassNames", qualified=True) == [
            TypeName("Test_getClassNames.C"),
        ]
    ).all()

    assert session.loadString(
        """
within Test_getClassNames;
type A = enumeration(a);
        """
    )
    assert (
        session.getClassNames("Test_getClassNames") == [
            TypeName("C"),
            TypeName("A"),
        ]
    ).all()
    assert (
        session.getClassNames("Test_getClassNames", sort=True) == [
            TypeName("A"),
            TypeName("C"),
        ]
    ).all()
    assert (
        session.getClassNames("Test_getClassNames", qualified=True) == [
            TypeName("Test_getClassNames.C"),
            TypeName("Test_getClassNames.A"),
        ]
    ).all()

    assert session.loadString(
        """
within Test_getClassNames;
type B = enumeration(b);
        """
    )
    assert (
        session.getClassNames("Test_getClassNames") == [
            TypeName("C"),
            TypeName("A"),
            TypeName("B"),
        ]
    ).all()
    assert (
        session.getClassNames("Test_getClassNames", sort=True) == [
            TypeName("A"),
            TypeName("B"),
            TypeName("C"),
        ]
    ).all()
    assert (
        session.getClassNames("Test_getClassNames", qualified=True) == [
            TypeName("Test_getClassNames.C"),
            TypeName("Test_getClassNames.A"),
            TypeName("Test_getClassNames.B"),
        ]
    ).all()


@pytest.mark.dependency(depends=["test_open_session"])
def test_OpenModelica(
    session  # fixture
):
    assert session.isPackage("OpenModelica")
