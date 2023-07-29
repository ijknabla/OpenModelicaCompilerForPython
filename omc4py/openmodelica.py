from __future__ import annotations

__all__ = ("Component", "TypeName", "VariableName")

import itertools
from collections.abc import Callable, Iterable, Iterator
from typing import TYPE_CHECKING, Any, List, NamedTuple, TypeVar, Union

from typing_extensions import Literal

from .string import to_omc_literal

if TYPE_CHECKING:
    from typing_extensions import Self


class Component(NamedTuple):
    className: TypeName
    name: VariableName
    comment: str
    protected: Literal["protected", "public"]
    isFinal: bool
    isFlow: bool
    isStream: bool
    isReplaceable: bool
    variability: Literal["constant", "parameter", "discrete", "unspecified"]
    innerOuter: Literal["inner", "outer", "none"]
    inputOutput: Literal["input", "output", "unspecified"]
    dimensions: List[str]


# Type hints

KT = TypeVar("KT")

VariableNameLike = Union[
    "TypeName",
    "VariableName",
    str,
]

TypeNameLike = VariableNameLike


# $Code classes OpenModelica.$Code.{VariableName, TypeName}


class _BaseVariableName:
    __slots__ = ("__identifier",)
    __identifier: str

    def __new__(cls, identifier: str) -> Self:
        self = super(_BaseVariableName, cls).__new__(cls)
        self.__identifier = identifier
        return self

    def __eq__(self, other: Any) -> bool:
        return (
            isinstance(other, _BaseVariableName)
            and self.__identifier == other.__identifier
        )

    def __hash__(self) -> int:
        return hash(self.__identifier)

    def __str__(self) -> str:
        return self.__identifier

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.__identifier!r})"

    __to_omc_literal__ = __str__


class VariableName(_BaseVariableName):
    def __new__(cls, obj: VariableNameLike) -> Self:
        from .parser import is_variablename

        if isinstance(obj, cls):
            return obj

        if isinstance(obj, str):
            identifier = obj
        elif isinstance(obj, TypeName):
            identifier = to_omc_literal(obj)
        else:
            raise TypeError(
                "obj must be TypeName, VariableName or str, "
                f"got {obj!r}: {type(obj)}"
            )

        if not is_variablename(identifier):
            raise ValueError(
                f"Invalid modelica identifier, got {identifier!r}"
            )

        return _BaseVariableName.__new__(cls, identifier)


class _BaseTypeName:
    __slots__ = ("parts",)

    parts: tuple[str, ...]

    def __new__(cls, parts: tuple[str, ...]) -> Self:
        self = super(_BaseTypeName, cls).__new__(cls)
        self.parts = parts
        return self

    @property
    def is_absolute(self) -> bool:
        return bool(self.parts) and self.parts[0] == "."

    def as_absolute(self) -> Self:
        if self.is_absolute:
            return self
        else:
            return _BaseTypeName.__new__(type(self), (".", *self.parts))

    @property
    def last_identifier(self) -> VariableName:
        return VariableName(self.parts[-1])

    @property
    def parents(self) -> Iterator[Self]:
        for end in reversed(range(1, len(self.parts))):
            yield _BaseTypeName.__new__(
                type(self),
                self.parts[:end],
            )

    @property
    def parent(self) -> Self:
        for parent in self.parents:
            return parent
        else:
            return self

    def __hash__(self) -> int:
        return hash(self.parts)

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, _BaseTypeName) and self.parts == other.parts

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.parts})"

    def __str__(self) -> str:
        if self.is_absolute:
            return self.parts[0] + ".".join(self.parts[1:])
        else:
            return ".".join(self.parts)

    __to_omc_literal__ = __str__


class TypeName(_BaseTypeName):
    def __new__(cls, part: TypeNameLike, *parts: TypeNameLike) -> Self:
        if isinstance(part, cls) and not parts:
            return part

        return _BaseTypeName.__new__(
            cls, tuple(TypeName.__split_parts((part, *parts)))
        )

    @staticmethod
    def __split_parts(parts: Iterable[TypeNameLike]) -> Iterator[str]:
        for i, part in enumerate(
            itertools.chain(*map(TypeName.__split_part, parts))
        ):
            if part == "." and not i == 0:
                raise ValueError(f"parts[{i}] is invalid, got {part!r}")
            yield part

    @staticmethod
    def __split_part(part: TypeNameLike) -> Iterator[str]:
        from .parser import split_typename_parts

        if isinstance(part, TypeName):
            yield from part.parts
        elif isinstance(part, VariableName):
            yield str(part)
        elif isinstance(part, str):
            if part == ".":
                yield part
            else:
                yield from split_typename_parts(part)
        else:
            raise TypeError(f"Unexpected part, got {part}: {type(part)}")

    def __repr__(self) -> str:
        return f"{type(self).__name__}({str(self)!r})"

    def __truediv__(self, other: TypeNameLike) -> Self:
        return type(self)(self, other)


def split_dict(
    dictionary: dict[KT, Any],
    condition: Callable[[Any], bool],
) -> tuple[dict[KT, Any], dict[KT, Any]]:
    yes, no = {}, {}
    for k, v in dictionary.items():
        if condition(v):
            yes[k] = v
        else:
            no[k] = v
    return yes, no
