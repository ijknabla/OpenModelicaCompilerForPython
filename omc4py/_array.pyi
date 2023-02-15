from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Generic, TypeVar, Union, overload

from typing_extensions import Literal

DType = TypeVar("DType")
DType1 = TypeVar("DType1")
DType2 = TypeVar("DType2")
Size1 = TypeVar("Size1", bound=int)
Size2 = TypeVar("Size2", bound=int)
SizeArg1 = TypeVar(
    "SizeArg1",
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
    Literal[1],
    Literal[2],
    Literal[3],
    Literal[4],
    Literal[5],
    Literal[6],
    Literal[7],
    Literal[8],
)

class Array1D(Generic[(DType, Size1)], Sequence[DType]):
    ndim: Literal[1]
    shape: tuple[(Size1,)]

    def __eq__(self, other: Any) -> bool: ...
    def __len__(self) -> Size1: ...
    @overload
    def __getitem__(self, index: Union[(int, tuple[int])]) -> DType: ...
    @overload
    def __getitem__(
        self, index: Union[(slice, tuple[slice])]
    ) -> Array1D[(DType, int)]: ...

class Array2D(
    Generic[(DType, Size1, Size2)], Sequence[Array1D[(DType, Size2)]]
):
    ndim: Literal[2]
    shape: tuple[(Size1, Size2)]

    def __eq__(self, other: Any) -> bool: ...
    def __len__(self) -> Size1: ...
    @overload
    def __getitem__(self, index: tuple[(int, int)]) -> DType: ...
    @overload
    def __getitem__(
        self, index: Union[(int, tuple[int])]
    ) -> Array1D[(DType, Size2)]: ...
    @overload
    def __getitem__(
        self, index: Union[(tuple[(int, slice)], tuple[(slice, int)])]
    ) -> Array1D[(DType, int)]: ...
    @overload
    def __getitem__(
        self, index: Union[(slice, tuple[slice])]
    ) -> Array2D[(DType, int, Size2)]: ...
    @overload
    def __getitem__(
        self, index: tuple[(slice, slice)]
    ) -> Array2D[(DType, int, int)]: ...

@overload
def array(
    object: Any,
    *,
    dtype: Union[(type[DType], tuple[(type[DType],)])],
    shape: tuple[()],
) -> DType: ...
@overload
def array(
    object: Any,
    *,
    dtype: tuple[(type[DType1], type[DType2])],
    shape: tuple[()],
) -> Union[(DType1, DType2)]: ...
@overload
def array(
    object: Sequence[Any],
    *,
    dtype: Union[(type[DType], tuple[(type[DType],)])],
    shape: tuple[(SizeArg1,)],
) -> Array1D[(DType, SizeArg1)]: ...
@overload
def array(
    object: Sequence[Any],
    *,
    dtype: Union[(type[DType], tuple[(type[DType],)])],
    shape: tuple[(None,)],
) -> Array1D[(DType, int)]: ...
@overload
def array(
    object: Sequence[Any],
    *,
    dtype: tuple[(type[DType1], type[DType2])],
    shape: tuple[(SizeArg1,)],
) -> Array1D[(Union[(DType1, DType2)], SizeArg1)]: ...
@overload
def array(
    object: Sequence[Any],
    *,
    dtype: tuple[(type[DType1], type[DType2])],
    shape: tuple[(None,)],
) -> Array1D[(Union[(DType1, DType2)], int)]: ...
@overload
def array(
    object: Sequence[Sequence[Any]],
    *,
    dtype: Union[(type[DType], tuple[(type[DType],)])],
    shape: tuple[(SizeArg1, SizeArg2)],
) -> Array2D[(DType, SizeArg1, SizeArg2)]: ...
@overload
def array(
    object: Sequence[Sequence[Any]],
    *,
    dtype: Union[(type[DType], tuple[(type[DType],)])],
    shape: tuple[(SizeArg1, None)],
) -> Array2D[(DType, SizeArg1, int)]: ...
@overload
def array(
    object: Sequence[Sequence[Any]],
    *,
    dtype: Union[(type[DType], tuple[(type[DType],)])],
    shape: tuple[(None, SizeArg2)],
) -> Array2D[(DType, int, SizeArg2)]: ...
@overload
def array(
    object: Sequence[Sequence[Any]],
    *,
    dtype: Union[(type[DType], tuple[(type[DType],)])],
    shape: tuple[(None, None)],
) -> Array2D[(DType, int, int)]: ...
@overload
def array(
    object: Sequence[Sequence[Any]],
    *,
    dtype: tuple[(type[DType1], type[DType2])],
    shape: tuple[(SizeArg1, SizeArg2)],
) -> Array2D[(Union[(DType1, DType2)], SizeArg1, SizeArg2)]: ...
@overload
def array(
    object: Sequence[Sequence[Any]],
    *,
    dtype: tuple[(type[DType1], type[DType2])],
    shape: tuple[(SizeArg1, None)],
) -> Array2D[(Union[(DType1, DType2)], SizeArg1, int)]: ...
@overload
def array(
    object: Sequence[Sequence[Any]],
    *,
    dtype: tuple[(type[DType1], type[DType2])],
    shape: tuple[(None, SizeArg2)],
) -> Array2D[(Union[(DType1, DType2)], int, SizeArg2)]: ...
@overload
def array(
    object: Sequence[Sequence[Any]],
    *,
    dtype: tuple[(type[DType1], type[DType2])],
    shape: tuple[(None, None)],
) -> Array2D[(Union[(DType1, DType2)], int, int)]: ...
