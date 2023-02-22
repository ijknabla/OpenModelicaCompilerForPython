from __future__ import annotations

import builtins
from collections.abc import Iterable, Iterator, Sequence
from dataclasses import InitVar, dataclass, field
from functools import reduce
from itertools import product
from operator import getitem
from typing import Any, ClassVar, Optional, TypeVar, Union, cast

from typing_extensions import Literal, TypeAlias, TypedDict

from .meta import SupportsArrayIndexing

T_array_meta = TypeVar("T_array_meta", bound="_ArrayMeta")

DType: TypeAlias = Union[type, "tuple[type, ...]"]
Size = Optional[int]
Shape: TypeAlias = "tuple[Size, ...]"


class _ArrayMetaNameSpace(TypedDict):
    dtype: DType
    __shape__: Shape


class _ArrayMeta(type):
    dtype: DType = object
    __shape__: Shape = ()

    def __repr__(cls) -> str:
        if cls.__is_root:
            return super().__repr__()
        else:
            return (
                f"{_format_dtype(cls)}"
                f"[{_format_dtype(cls.dtype)}, {cls.__shape__!r}]"
            )

    def __getitem__(
        cls: T_array_meta,
        index: tuple[DType, Shape],
    ) -> T_array_meta:
        if not cls.__is_root:
            raise TypeError(
                f"There are no dtype, shape variables left in {cls!r}"
            )

        dtype, __shape__ = _sanitize_array_type_index(index)

        indexed_cls = type(cls)(
            cls.__name__,
            (cls,),
            dict(_ArrayMetaNameSpace(dtype=dtype, __shape__=__shape__)),
        )

        return indexed_cls

    @property
    def __is_root(cls) -> bool:
        return cls.dtype is object and cls.__shape__ == ()


@dataclass(frozen=True)
class Array:
    dtype: ClassVar[DType]
    __shape__: ClassVar[Shape]
    object: InitVar[Any]
    shape: tuple[int, ...] = field(init=False)
    __data__: list[Any] = field(init=False)

    def __class_getitem__(
        cls,
        index: tuple[DType, Shape],
    ) -> type[Array]:
        dtype, __shape__ = _sanitize_array_type_index(index)

        return cls.__get_array_type(dtype=dtype, __shape__=__shape__)

    @classmethod
    def __get_array_type(
        cls,
        dtype: Union[type, tuple[type, ...]],
        __shape__: tuple[Optional[int], ...],
    ) -> type[Array]:
        return type(
            cls.__name__, (Array,), dict(dtype=dtype, __shape__=__shape__)
        )

    def __post_init__(self, object: Any) -> None:
        shape = self.__assume_shape(object)
        self.__check_shape(object, *shape)
        self.__setattr("shape", shape)

        __data__ = self.__make_empty(*shape)
        for indices, value in self.__ndenumerate(object, *shape):
            if not isinstance(value, self.dtype):
                raise TypeError(
                    "object"
                    + "".join(f"[{i}]" for i in indices)
                    + f" must be instance of {self.dtype}, "
                    f"got {value}: {type(value)}"
                )
            self.__set_by_indices(__data__, *indices, value=value)

        self.__setattr("__data__", __data__)

    @property
    def ndim(self) -> int:
        return len(self.__shape__)

    def __len__(self) -> int:
        return self.shape[0]

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Array):
            return bool(self.__data__ == other.__data__)
        else:
            return bool(self.__data__ == other)

    def __repr__(self) -> str:
        if isinstance(self.dtype, type):
            s_dtype = self.dtype.__name__
        else:
            s_dtype = (
                "(" + " ".join(f"{typ.__name__}," for typ in self.dtype) + ")"
            )
        return (
            f"{type(self).__name__}"
            f"[{s_dtype}, {self.__shape__}]({self.__data__})"
        )

    def __getitem__(
        self, index: Union[int, slice, tuple[Union[int, slice]]]
    ) -> Any:
        indices: tuple[Union[int, slice], ...]
        if isinstance(index, (int, slice)):
            indices = (index,)
        elif isinstance(index, tuple) and all(
            isinstance(i, (int, slice)) for i in index
        ):
            indices = index
        else:
            raise TypeError(
                f"index must be int | slice | tuple[int | slice], got {index}"
            )

        if not (len(indices) <= self.ndim):
            raise IndexError(
                f"index length exceed ndim={self.ndim}, got {len(indices)}"
            )

        for size, index in zip(self.shape, indices):
            if size == 0 and isinstance(index, int):
                raise IndexError(f"{type(self).__name__} index out of range")

        def bounded_indices() -> Iterator[Union[int, range]]:
            for s, i in zip(self.shape, indices):
                yield ((i if isinstance(i, int) else range(s)[i]))
            yield from map(range, self.shape[len(indices) :])

        return self.__get_by_bounded_indices(tuple(bounded_indices()))

    def __get_by_bounded_indices(
        self, indices: Sequence[Union[int, range]]
    ) -> Any:
        shape = tuple(
            len(index) for index in indices if isinstance(index, range)
        )

        if not shape:
            return self.__get_by_indices(
                self.__data__, cast("Sequence[int]", indices)
            )

        array_type = self.__get_array_type(self.dtype, __shape__=shape)

        result = array_type.__new__(array_type)
        result.__setattr("shape", shape)

        __data__: Any
        if any(size == 0 for size in shape):
            __data__ = ...
        else:
            __data__ = self.__make_empty(*shape)

            srcs = list(
                product(*((i,) if isinstance(i, int) else i for i in indices))
            )
            for src, (dst, _) in zip(
                srcs, self.__ndenumerate(__data__, *shape)
            ):
                self.__set_by_indices(
                    __data__,
                    *dst,
                    value=self.__get_by_indices(self.__data__, src),
                )

        result.__setattr("__data__", __data__)

        return result

    def __assume_shape(self, object: Any) -> tuple[int, ...]:
        result: list[int]
        result = []
        for i, expected_size in enumerate(self.__shape__):
            if not isinstance(object, SupportsArrayIndexing):
                raise TypeError(
                    "object"
                    + "[0]" * i
                    + f" is not valid sequence, got {object!r}"
                )
            size = len(object)
            if size != expected_size and expected_size is not None:
                raise ValueError(
                    "len(object"
                    + "[0]" * i
                    + f") must be {expected_size}, got {size}"
                )
            result.append(size)
            object = object[0]

        return tuple(result)

    @classmethod
    def __check_shape(
        cls, object: Any, size: int, *sizes: int, indices: tuple[int, ...] = ()
    ) -> None:
        if len(object) != size:
            raise ValueError(
                "len(object)"
                + "".join(f"[{i}]" for i in indices)
                + f" must be {size}, got {len(object)}"
            )

        if not sizes:
            return

        for i in range(size):
            cls.__check_shape(object[i], *sizes, indices=(*indices, i))

    @classmethod
    def __make_empty(cls, size: int, *sizes: int) -> list[Any]:
        return [
            cls.__make_empty(*sizes) if sizes else None for _ in range(size)
        ]

    @classmethod
    def __ndenumerate(
        cls, object: Any, size: int, *sizes: int, indices: tuple[int, ...] = ()
    ) -> Iterator[tuple[tuple[int, ...], Any]]:
        for i in range(size):
            if not sizes:
                yield (*indices, i), object[i]
            else:
                yield from cls.__ndenumerate(
                    object[i], *sizes, indices=(*indices, i)
                )

    def __setattr(
        self, name: Literal["__data__", "shape"], value: Any
    ) -> None:
        object.__setattr__(self, name, value)

    @classmethod
    def __get_by_indices(cls, object: Any, indices: Iterable[int]) -> Any:
        return reduce(getitem, indices, object)

    @classmethod
    def __set_by_indices(
        cls, object: Any, index: int, *indices: int, value: Any
    ) -> None:
        if not indices:
            object[index] = value
        else:
            cls.__set_by_indices(object[index], *indices, value=value)


def _sanitize_array_type_index(index: Any) -> tuple[DType, Shape]:
    if not (isinstance(index, tuple) and len(index) == 2):
        raise TypeError(f"index must be a tuple of length 2, got {index}")

    dtype, __shape__ = index
    if not (
        isinstance(dtype, type)
        or isinstance(dtype, tuple)
        and 0 < len(dtype)
        and all(isinstance(t, type) for t in dtype)
    ):
        raise TypeError(
            "dtype := index[0] must be type or not empty tuple[type, ...], "
            f"got {dtype}"
        )

    for i, t in enumerate(_iter_dtype(dtype)):
        if issubclass(t, SupportsArrayIndexing):
            t_repr = (
                "index[0]" if isinstance(dtype, type) else f"index[0][{i}]"
            )
            raise TypeError(
                f"dtype := {t_repr} "
                f"must not be sequence-like type, got {t}"
            )

    if not (
        isinstance(__shape__, tuple)
        and __shape__
        and all(isinstance(size, int) or size is None for size in __shape__)
    ):
        raise TypeError(
            "shape := index[1] must be not empty tuple[int | None, ...], "
            f"got {__shape__}"
        )

    t, *ts = sorted(set(_iter_dtype(dtype)), key=_type_order)
    if not ts:
        return t, __shape__
    else:
        return (t, *ts), __shape__


def _iter_dtype(dtype: DType) -> Iterator[type]:
    if isinstance(dtype, type):
        yield dtype
    else:
        yield from dtype


def _type_order(typ: type) -> tuple[int, str, str]:
    return (
        0 if _is_builtin(typ) else 1,
        typ.__module__,
        typ.__name__,
    )


def _is_builtin(obj: Any) -> bool:
    return obj in builtins.__dict__.values()


def _format_dtype(dtype: DType) -> str:
    name, *names = [
        ("" if _is_builtin(t) else f"{t.__module__}.") + t.__name__
        for t in _iter_dtype(dtype)
    ]

    if not names:
        return name
    else:
        return "(" + ", ".join([name, *names]) + ")"
