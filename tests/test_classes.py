from omc4py.classes import TypeName


def test_typename_combine() -> None:
    parts_a = ("A1", "A2")
    parts_b = ("B1", "B2")

    assert (TypeName(*parts_a) / TypeName(*parts_b)).parts == parts_a + parts_b


def test_typename_parents() -> None:
    typename = TypeName("A.B.C.D")

    for i, parent in enumerate(typename.parents, start=1):
        assert parent.parts == typename.parts[:-i]
