import pytest

from omc4py import TypeName, VariableName, latest, open_session


@pytest.mark.dependency()
def test_open_session() -> None:
    with open_session() as session:
        assert session is not None
        session.check()


@pytest.mark.dependency(depends=["test_open_session"])
def test_loadString(session: latest.Session) -> None:
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
def test_getClassNames(session: latest.Session) -> None:
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
    assert session.getClassNames("Test_getClassNames") == [
        TypeName("C"),
    ]
    assert session.getClassNames("Test_getClassNames", sort=True) == [
        TypeName("C"),
    ]
    assert session.getClassNames("Test_getClassNames", qualified=True) == [
        TypeName("Test_getClassNames.C"),
    ]

    assert session.loadString(
        """
within Test_getClassNames;
type A = enumeration(a);
        """
    )
    assert session.getClassNames("Test_getClassNames") == [
        TypeName("C"),
        TypeName("A"),
    ]
    assert session.getClassNames("Test_getClassNames", sort=True) == [
        TypeName("A"),
        TypeName("C"),
    ]
    assert session.getClassNames("Test_getClassNames", qualified=True) == [
        TypeName("Test_getClassNames.C"),
        TypeName("Test_getClassNames.A"),
    ]

    assert session.loadString(
        """
within Test_getClassNames;
type B = enumeration(b);
        """
    )
    assert session.getClassNames("Test_getClassNames") == [
        TypeName("C"),
        TypeName("A"),
        TypeName("B"),
    ]
    assert session.getClassNames("Test_getClassNames", sort=True) == [
        TypeName("A"),
        TypeName("B"),
        TypeName("C"),
    ]
    assert session.getClassNames("Test_getClassNames", qualified=True) == [
        TypeName("Test_getClassNames.C"),
        TypeName("Test_getClassNames.A"),
        TypeName("Test_getClassNames.B"),
    ]


@pytest.mark.dependency(depends=["test_open_session"])
def test_getComponents(session: latest.Session) -> None:
    assert session.loadString(
        """
class Test_getComponents
public
    A a;
    A a_comment "comment";
    final A a_final;
    flow A a_flow;
    stream A a_stream;
    replaceable A a_replaceable;
    discrete A a_discrete;
    parameter A a_parameter;
    constant A a_constant;
    inner A a_inner;
    outer A a_outer;
    input A a_input;
    output A a_output;
    A[:] a_any;
    A[:,:] a_any_any;
    A[:,:,:] a_any_any_any;
    A[1,2,3] a_1_2_3;
    A[3,2,1] a_3_2_1;
protected
    A a_protected;
end Test_getComponents;
        """
    )

    for component in session.getComponents("Test_getComponents"):
        assert component.className == TypeName("A")

        assert isinstance(component.name, VariableName)
        assert str(component.name).startswith("a")

        if component.name == VariableName("a_comment"):
            assert component.comment == "comment"
        else:
            assert component.comment == ""

        if component.name == VariableName("a_protected"):
            assert component.protected == "protected"
        else:
            assert component.protected == "public"

        if component.name == VariableName("a_final"):
            assert component.isFinal
        else:
            assert not component.isFinal

        if component.name == VariableName("a_flow"):
            assert component.isFlow
        else:
            assert not component.isFlow

        if component.name == VariableName("a_stream"):
            assert component.isStream
        else:
            assert not component.isStream

        if component.name == VariableName("a_replaceable"):
            assert component.isReplaceable
        else:
            assert not component.isReplaceable

        if component.name == VariableName("a_discrete"):
            assert component.variability == "discrete"
        elif component.name == VariableName("a_parameter"):
            assert component.variability == "parameter"
        elif component.name == VariableName("a_constant"):
            assert component.variability == "constant"
        else:
            assert component.variability == "unspecified"

        if component.name == VariableName("a_inner"):
            assert component.innerOuter == "inner"
        elif component.name == VariableName("a_outer"):
            assert component.innerOuter == "outer"
        else:
            assert component.innerOuter == "none"

        if component.name == VariableName("a_input"):
            assert component.inputOutput == "input"
        elif component.name == VariableName("a_output"):
            assert component.inputOutput == "output"
        else:
            assert component.inputOutput == "unspecified"

        if component.name == VariableName("a_any"):
            assert component.dimensions == [
                ":",
            ]
        elif component.name == VariableName("a_any_any"):
            assert component.dimensions == [
                ":",
                ":",
            ]
        elif component.name == VariableName("a_any_any_any"):
            assert component.dimensions == [
                ":",
                ":",
                ":",
            ]
        elif component.name == VariableName("a_1_2_3"):
            assert component.dimensions == [
                "1",
                "2",
                "3",
            ]
        elif component.name == VariableName("a_3_2_1"):
            assert component.dimensions == [
                "3",
                "2",
                "1",
            ]
        else:
            assert component.dimensions == []


@pytest.mark.dependency(depends=["test_open_session"])
def test_OpenModelica(session: latest.Session) -> None:
    assert session.isPackage("OpenModelica")


def test_getMessagesStringInternal(session: latest.Session) -> None:
    session.getMessagesStringInternal()
    for name in ["XXX", "YYY", "ZZZ"]:
        session.__omc_interactive__.evaluate(name)
        for message in session.getMessagesStringInternal():
            assert message.message.startswith(f"Variable {name} not found")
