from __future__ import annotations

from collections import defaultdict
from collections.abc import Iterable
from dataclasses import dataclass
from functools import reduce
from itertools import product
from operator import getitem
from typing import Any, Iterator, Optional, TypeVar, Union, cast

from typing_extensions import Protocol, runtime_checkable

from .backport import Sequence

DType = TypeVar("DType")


@dataclass(frozen=True)
class ArrayND(Sequence[Any]):
    __object: Any
    shape: tuple[int, ...]

    @property
    def ndim(self) -> int:
        return len(self.shape)

    def __len__(self) -> int:
        return len(self.__object)

    def __getitem__(
        self, index: Union[int, slice, Sequence[Union[int, slice]]]
    ) -> Any:
        if isinstance(index, int):
            if self.ndim == 1:
                return self.__object[index]
            else:
                return ArrayND(self.__object[index], shape=self.shape[1:])
        elif isinstance(index, slice):
            sliced = self.__object[index]
            return ArrayND(sliced, shape=(len(sliced), *self.shape[1:]))
        elif all(s == slice(None) for s in index):
            return self
        elif all(isinstance(i, int) for i in index):
            return self.__get_by_indices(self, *cast("Iterable[int]", index))
        else:
            normalized = self.__normalize_indices(index)

            shape = tuple(
                len(range_)
                for range_ in normalized
                if isinstance(range_, range)
            )

            result = self.__make_empty(*shape)
            for src, dst in zip(
                product(*normalized), self.__destination_indices(normalized)
            ):
                self.__set_by_indices(
                    result, self.__get_by_indices(self, *src), *dst
                )

            return ArrayND(result, shape)

        raise NotImplementedError()

    @staticmethod
    def __get_by_indices(obj: Any, *indices: int) -> Any:
        return reduce(getitem, indices, obj)

    @classmethod
    def __set_by_indices(
        cls, obj: Any, value: Any, index: int, *indices: int
    ) -> None:
        if not indices:
            obj[index] = value
        else:
            cls.__set_by_indices(obj[index], value, *indices)

    def __normalize_indices(
        self, indices: Sequence[Union[int, slice]]
    ) -> tuple[Union[tuple[int], range], ...]:
        int_or_slices = [*indices, *[slice(None)] * (self.ndim - len(indices))]
        return tuple(
            (i,) if isinstance(i, int) else range(size)[i]
            for size, i in zip(self.shape, int_or_slices)
        )

    @classmethod
    def __make_empty(cls, size: int, *sizes: int) -> Any:
        return [cls.__make_empty(*sizes) if sizes else None] * size

    @classmethod
    def __destination_indices(
        cls, indices: Sequence[Union[tuple[int], range]]
    ) -> Iterator[tuple[int, ...]]:
        if not indices:
            yield ()
            return

        heads: list[tuple[int, ...]]
        if isinstance(indices[0], range):
            heads = [(i,) for i, _ in enumerate(indices[0])]
        else:
            heads = [()]

        for head in heads:
            for tail in cls.__destination_indices(indices[1:]):
                yield (*head, *tail)

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, ArrayND):
            return bool(self.__object == other.__object)
        else:
            return bool(self.__object == other)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"({self.__object!r}, shape={self.shape!r})"
        )


def array(
    object: Any,
    *,
    dtype: Union[type[DType], tuple[type[DType], ...]],
    shape: tuple[int, ...],
) -> Any:
    categories: defaultdict[int, defaultdict[int, list[tuple[int, ...]]]]
    categories = defaultdict(lambda: defaultdict(list))
    for indices, size in _check_elements(object, dtype, shape):
        categories[len(indices)][size].append(indices)

    actual_shape: list[int]
    actual_shape = []
    for dim, size_opt in enumerate(shape):
        if size_opt is not None:
            actual_shape.append(size_opt)
        else:
            size_opt, *sizes = sorted(categories[dim])
            if sizes:
                raise ValueError(
                    f"Sizes in dimesion {dim} are different, "
                    f"got {(size_opt, *sizes)}"
                )
            actual_shape.append(size_opt)

    if not actual_shape:
        return object
    else:
        return ArrayND(object, tuple(actual_shape))


@runtime_checkable
class SupportsSequence(Protocol):
    def __len__(self) -> int:
        ...

    def __getitem__(self, index: int) -> Any:
        ...


def _check_elements(
    object: Any,
    dtype: Union[type[DType], tuple[type[DType], ...]],
    expected_shape: Sequence[Optional[int]],
    indices: tuple[int, ...] = (),
) -> Iterator[tuple[tuple[int, ...], int]]:
    if not expected_shape:
        if not isinstance(object, dtype):
            target = "object" + "".join(f"[{index}]" for index in indices)
            raise TypeError(
                f"{target} must be {dtype}, got {object!r}: {type(object)}"
            )
        return

    if isinstance(object, str) or not isinstance(object, SupportsSequence):
        target = "object" + "".join(f"[{index}]" for index in indices)
        raise TypeError(f"{target} must be Sequence, got {object!r}")

    expected_size, *next_expected_shape = expected_shape
    actual_size = len(object)
    if actual_size != expected_size and expected_size is not None:
        target = "object" + "".join(f"[{index}]" for index in indices)
        raise ValueError(
            f"len({target}) must be {expected_size}, "
            f"len({object!r}) is {actual_size}"
        )

    yield indices, actual_size

    for i in range(actual_size):
        yield from _check_elements(
            object[i], dtype, next_expected_shape, (*indices, i)
        )
