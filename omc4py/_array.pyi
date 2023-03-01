from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Generic, TypeVar, Union, overload

from typing_extensions import Literal

from omc4py.meta import SupportsArrayIndexing

DType = TypeVar("DType")
DType1 = TypeVar("DType1")
DType2 = TypeVar("DType2")
Size1 = TypeVar("Size1", bound=int)
Size2 = TypeVar("Size2", bound=int)
SizeArg1 = TypeVar(
    "SizeArg1",
    int,
    Literal[1],
    Literal[2],
    Literal[3],
    Literal[4],
    Literal[5],
    Literal[6],
    Literal[7],
    Literal[8],
)
SizeArg2 = TypeVar(
    "SizeArg2",
    int,
    Literal[1],
    Literal[2],
    Literal[3],
    Literal[4],
    Literal[5],
    Literal[6],
    Literal[7],
    Literal[8],
)

class ArrayMeta(type):
    @overload
    def __getitem__(
        cls,
        index: tuple[
            (Union[(type[DType], tuple[(type[DType],)])], tuple[(SizeArg1,)])
        ],
    ) -> type[_1DArray[(DType, SizeArg1)]]: ...
    @overload
    def __getitem__(
        cls,
        index: tuple[
            (Union[(type[DType], tuple[(type[DType],)])], tuple[(None,)])
        ],
    ) -> type[_1DArray[(DType, int)]]: ...
    @overload
    def __getitem__(
        cls,
        index: tuple[
            (tuple[(type[DType1], type[DType2])], tuple[(SizeArg1,)])
        ],
    ) -> type[_1DArray[(Union[(DType1, DType2)], SizeArg1)]]: ...
    @overload
    def __getitem__(
        cls,
        index: tuple[(tuple[(type[DType1], type[DType2])], tuple[(None,)])],
    ) -> type[_1DArray[(Union[(DType1, DType2)], int)]]: ...
    @overload
    def __getitem__(
        cls,
        index: tuple[
            (
                Union[(type[DType], tuple[(type[DType],)])],
                tuple[(SizeArg1, SizeArg2)],
            )
        ],
    ) -> type[_2DArray[(DType, SizeArg1, SizeArg2)]]: ...
    @overload
    def __getitem__(
        cls,
        index: tuple[
            (
                Union[(type[DType], tuple[(type[DType],)])],
                tuple[(SizeArg1, None)],
            )
        ],
    ) -> type[_2DArray[(DType, SizeArg1, int)]]: ...
    @overload
    def __getitem__(
        cls,
        index: tuple[
            (
                Union[(type[DType], tuple[(type[DType],)])],
                tuple[(None, SizeArg2)],
            )
        ],
    ) -> type[_2DArray[(DType, int, SizeArg2)]]: ...
    @overload
    def __getitem__(
        cls,
        index: tuple[
            (Union[(type[DType], tuple[(type[DType],)])], tuple[(None, None)])
        ],
    ) -> type[_2DArray[(DType, int, int)]]: ...
    @overload
    def __getitem__(
        cls,
        index: tuple[
            (tuple[(type[DType1], type[DType2])], tuple[(SizeArg1, SizeArg2)])
        ],
    ) -> type[_2DArray[(Union[(DType1, DType2)], SizeArg1, SizeArg2)]]: ...
    @overload
    def __getitem__(
        cls,
        index: tuple[
            (tuple[(type[DType1], type[DType2])], tuple[(SizeArg1, None)])
        ],
    ) -> type[_2DArray[(Union[(DType1, DType2)], SizeArg1, int)]]: ...
    @overload
    def __getitem__(
        cls,
        index: tuple[
            (tuple[(type[DType1], type[DType2])], tuple[(None, SizeArg2)])
        ],
    ) -> type[_2DArray[(Union[(DType1, DType2)], int, SizeArg2)]]: ...
    @overload
    def __getitem__(
        cls,
        index: tuple[
            (tuple[(type[DType1], type[DType2])], tuple[(None, None)])
        ],
    ) -> type[_2DArray[(Union[(DType1, DType2)], int, int)]]: ...

class Array(metaclass=ArrayMeta): ...

class _1DArray(Generic[(DType, Size1)], Sequence[DType]):
    ndim: Literal[1]
    shape: tuple[(Size1,)]

    def __init__(self, object: SupportsArrayIndexing[DType]) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    def __len__(self) -> Size1: ...
    @overload
    def __getitem__(self, index: Union[(int, tuple[int])]) -> DType: ...
    @overload
    def __getitem__(
        self, index: Union[(slice, tuple[slice])]
    ) -> _1DArray[(DType, int)]: ...

class _2DArray(
    Generic[(DType, Size1, Size2)], Sequence[_1DArray[(DType, Size2)]]
):
    ndim: Literal[2]
    shape: tuple[(Size1, Size2)]

    def __init__(
        self, object: SupportsArrayIndexing[SupportsArrayIndexing[DType]]
    ) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    def __len__(self) -> Size1: ...
    @overload
    def __getitem__(self, index: tuple[(int, int)]) -> DType: ...
    @overload
    def __getitem__(
        self, index: Union[(int, tuple[int])]
    ) -> _1DArray[(DType, Size2)]: ...
    @overload
    def __getitem__(
        self, index: Union[(tuple[(int, slice)], tuple[(slice, int)])]
    ) -> _1DArray[(DType, int)]: ...
    @overload
    def __getitem__(
        self, index: Union[(slice, tuple[slice])]
    ) -> _2DArray[(DType, int, Size2)]: ...
    @overload
    def __getitem__(
        self, index: tuple[(slice, slice)]
    ) -> _2DArray[(DType, int, int)]: ...
