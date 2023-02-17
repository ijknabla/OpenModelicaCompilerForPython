import pytest
from typing_extensions import reveal_type

from omc4py._array import Array, array


def test_array_element() -> None:
    scalar = 0
    assert array(scalar, dtype=int, shape=()) is scalar

    data1d = range(4, 8)
    array1d = Array[int, (4,)](data1d)

    assert array1d.ndim == 1
    assert array1d.shape == (4,)
    assert len(array1d) == array1d.shape[0]

    reveal_type(array1d)
    reveal_type(array1d.ndim)
    reveal_type(array1d.shape)

    for i, data in enumerate(data1d):
        assert array1d[i] == data

    data2d = [[0, 1], [2, 3], [4, 5]]
    array2d = Array[int, (3, 2)](data2d)
    assert array2d.ndim == 2
    assert array2d.shape == (3, 2)
    assert len(array2d) == array2d.shape[0]

    reveal_type(array2d)
    reveal_type(array2d.ndim)
    reveal_type(array2d.shape)

    rows = data2d
    cols = list(map(list, zip(*data2d)))

    assert data2d == array2d == array2d[:] == array2d[:, :]
    for (i, row), (j, col) in zip(enumerate(rows), enumerate(cols)):
        assert (
            row[j]
            == col[i]
            == array2d[i, j]
            == array2d[i - array2d.shape[0], j - array2d.shape[1]]
        )
        assert (
            row
            == array2d[i]
            == array2d[i, :]
            == array2d[i - array2d.shape[0], 0 : array2d.shape[1]]
        )
        assert (
            col
            == array2d[:, j]
            == array2d[0 : array2d.shape[0], j - array2d.shape[1]]
        )

    assert array2d[1:2] == array2d[1:2, :] == data2d[1:2]


def test_array_repr() -> None:
    ixss = Array[int, (None, None)]([[0, 1], [2, 3], [4, 5]])
    assert eval(repr(ixss)) == ixss


def test_array_shape_check() -> None:
    assert Array[int, (None, 2)](
        [
            [1, 1],
            [2, 2],
        ]
    ).shape == (2, 2)

    assert Array[int, (2, None)](
        [
            [1, 1],
            [2, 2],
        ]
    ).shape == (2, 2)

    assert Array[int, (None, None)](
        [
            [1, 1],
            [2, 2],
        ]
    ).shape == (2, 2)

    with pytest.raises(ValueError):
        Array[int, (1, 2)](
            [
                [1, 1],
                [2, 2],
            ],
        )

    with pytest.raises(ValueError):
        Array[int, (2, None)](
            [
                [1],
                [2, 2],
            ]
        )


def test_array_type_check() -> None:
    with pytest.raises(TypeError):
        Array[str, (2,)]("01")
    with pytest.raises(TypeError):
        Array[int, (2,)]([0, "1"])
    with pytest.raises(TypeError):
        Array[str, (2,)]([0, "1"])

    reveal_type(Array[(int, str), (2,)]([0, "0"]))
