from omc4py.classes import TypeName, VariableName


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
