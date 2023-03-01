from __future__ import annotations

import builtins
from collections.abc import Iterator, Sequence
from dataclasses import InitVar, dataclass, field
from functools import partial, reduce
from itertools import chain, islice, product
from typing import Any, ClassVar, Optional, TypeVar, Union, cast
from weakref import WeakValueDictionary

from typing_extensions import TypeAlias, TypedDict

from .meta import SupportsArrayIndexing

T_array_meta = TypeVar("T_array_meta", bound="_ArrayMeta")

DType: TypeAlias = Union[type, "tuple[type, ...]"]
Size = Optional[int]
Shape: TypeAlias = "tuple[Size, ...]"


class _ArrayMetaNameSpace(TypedDict):
    dtype: DType
    shape: Shape


class _ArrayMeta(type):
    __cache: ClassVar[
        WeakValueDictionary[
            tuple[_ArrayMeta, frozenset[type], Shape], _ArrayMeta
        ]
    ]
    __cache = WeakValueDictionary()
    dtype: DType = object
    shape: Shape = ()

    def __repr__(cls) -> str:
        if cls.__is_root:
            return super().__repr__()
        else:
            return (
                f"{_format_dtype(cls)}"
                f"[{_format_dtype(cls.dtype)}, {cls.shape!r}]"
            )

    def __getitem__(
        cls: T_array_meta,
        index: tuple[DType, Shape],
    ) -> T_array_meta:
        if not cls.__is_root:
            raise TypeError(
                f"There are no dtype, shape variables left in {cls!r}"
            )

        dtype, shape = _sanitize_array_type_index(index)
        key = (cls, frozenset(_iter_dtype(dtype)), shape)

        try:
            return cast(T_array_meta, cls.__cache[key])
        except KeyError:
            pass

        indexed_cls = type(cls)(
            cls.__name__,
            (cls,),
            dict(_ArrayMetaNameSpace(dtype=dtype, shape=shape)),
        )
        cls.__cache[key] = indexed_cls

        return indexed_cls

    @property
    def __is_root(cls) -> bool:
        return cls.dtype is object and cls.shape == ()


@dataclass(frozen=True)
class Array(metaclass=_ArrayMeta):
    dtype: ClassVar[DType]
    object: InitVar[Any]
    shape: tuple[int, ...] = field(init=False)
    ndim: int = field(init=False)
    __array__: tuple[Any, ...] = field(init=False)

    def __post_init__(self, object: Any) -> None:
        shape = self.__assume_shape(object)
        self.__check_shape(object, *shape)

        array = tuple(
            reduce(lambda x, _: chain.from_iterable(x), shape[:-1], object)
        )
        for i, value in enumerate(array):
            if not isinstance(value, self.dtype):
                raise TypeError(
                    "object"
                    + "".join(f"[{i}]" for i in Array.__unpack(shape, i))
                    + f" must be instance of {self.dtype}, "
                    f"got {value}: {type(value)}"
                )
        self.__setup(shape, array)

    def __setup(self, shape: tuple[int, ...], array: tuple[Any, ...]) -> None:
        object.__setattr__(self, "shape", shape)
        object.__setattr__(self, "ndim", len(shape))
        object.__setattr__(self, "__array__", array)

    @property
    def __nested(self) -> list[Any]:
        def impl(iterator: Iterator[Any], size: int, *sizes: int) -> list[Any]:
            if not sizes:
                return list(islice(iterator, size))
            else:
                return [impl(iterator, *sizes) for _ in range(size)]

        return impl(iter(self.__array__), *self.shape)

    @property
    def __shape(self) -> Shape:
        return cast(_ArrayMeta, type(self)).shape

    def __len__(self) -> int:
        return self.shape[0]

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Array):
            return (
                self.shape == other.shape and self.__array__ == other.__array__
            )
        else:
            return bool(self.__nested == other)

    def __repr__(self) -> str:
        return f"{type(self)!r}({self.__nested})"

    def __getitem__(
        self, index: Union[int, slice, tuple[Union[int, slice]]]
    ) -> Any:
        sanitized = self.__sanitize_index(index)

        shape: tuple[int, ...] = ()
        indices: list[Sequence[int]] = []
        for i, size in zip(sanitized, self.shape):
            if isinstance(i, int):
                if i not in range(-size, size):
                    raise IndexError(
                        f"{type(self).__name__} index out of range"
                    )
                indices.append((range(size)[i],))
            else:
                r = range(size)[i]
                indices.append(r)
                shape += (len(r),)

        if not shape:
            return self.__array__[
                self.__pack(self.shape, next(product(*indices)))
            ]

        __array__ = tuple(  # noqa: F841
            map(
                self.__array__.__getitem__,
                map(partial(self.__pack, self.shape), product(*indices)),
            )
        )

        sliced_type: type[Array]
        sliced_type = Array[self.dtype, shape]
        sliced = sliced_type.__new__(sliced_type)
        sliced.__setup(
            shape,
            tuple(
                map(
                    self.__array__.__getitem__,
                    map(partial(self.__pack, self.shape), product(*indices)),
                )
            ),
        )

        return sliced

    @staticmethod
    def __pack(shape: tuple[int, ...], indices: tuple[int, ...]) -> int:
        result = 0
        for s, i in zip(shape, indices):
            result *= s
            result += i
        return result

    @staticmethod
    def __unpack(shape: tuple[int, ...], index: int) -> tuple[int, ...]:
        indices: list[int] = []
        for size in reversed(shape):
            indices.append(index % size)
            index //= size
        return tuple(reversed(indices))

    def __sanitize_index(
        self, index: Union[int, slice, tuple[Union[int, slice], ...]]
    ) -> tuple[Union[int, slice], ...]:
        indices: tuple[Union[int, slice], ...]
        if isinstance(index, tuple):
            indices = index
        else:
            indices = (index,)

        if len(indices) > self.ndim:
            raise IndexError(
                f"index length exceed ndim={self.ndim}, got {len(indices)}"
            )

        return indices + (slice(None, None),) * (self.ndim - len(indices))

    def __assume_shape(self, object: Any) -> tuple[int, ...]:
        result: list[int]
        result = []
        for i, expected_size in enumerate(self.__shape):
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


def _sanitize_array_type_index(index: Any) -> tuple[DType, Shape]:
    if not (isinstance(index, tuple) and len(index) == 2):
        raise TypeError(f"index must be a tuple of length 2, got {index}")

    dtype, shape = index
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
        isinstance(shape, tuple)
        and shape
        and all(isinstance(size, int) or size is None for size in shape)
    ):
        raise TypeError(
            "shape := index[1] must be not empty tuple[int | None, ...], "
            f"got {shape}"
        )

    t, *ts = sorted(set(_iter_dtype(dtype)), key=_type_order)
    if not ts:
        return t, shape
    else:
        return (t, *ts), shape


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
    return ("({})" if names else "{}").format(", ".join([name, *names]))
