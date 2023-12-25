from __future__ import annotations

__all__ = ("Component", "TypeName", "VariableName")

import itertools
from collections.abc import Iterable, Iterator
from typing import (
    TYPE_CHECKING,
    Any,
    List,
    Literal,
    NamedTuple,
    TypeVar,
    Union,
)

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
    __identifier: str | None

    def __new__(cls, identifier: str | None = None) -> Self:
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
        if self.__identifier is None:
            return ""
        else:
            return self.__identifier

    def __repr__(self) -> str:
        if self.__identifier is None:
            return f"{type(self).__name__}()"
        else:
            return f"{type(self).__name__}({self.__identifier!r})"


class VariableName(_BaseVariableName):
    def __new__(cls, obj: VariableNameLike | None = None) -> Self:
        from .parser import is_variablename

        if obj is None:
            return _BaseVariableName.__new__(cls)

        if isinstance(obj, cls):
            return obj

        if isinstance(obj, str):
            identifier = obj
        elif isinstance(obj, TypeName):
            identifier = str(obj)
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

    def __new__(cls, parts: tuple[str, ...] = ()) -> Self:
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
        if self.parts in {(), (".",)}:
            return VariableName()
        else:
            return VariableName(self.parts[-1])

    @property
    def parents(self) -> tuple[Self, ...]:
        return tuple(
            _BaseTypeName.__new__(
                type(self),
                self.parts[:end],
            )
            for end in range(1 if self.is_absolute else 0, len(self.parts))
        )[::-1]

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
        if not self.parts:
            return f"{type(self).__name__}()"
        else:
            return f"{type(self).__name__}({str(self)!r})"

    def __str__(self) -> str:
        if not self.parts:
            return ""
        elif self.parts[0] == ".":
            return self.parts[0] + ".".join(self.parts[1:])
        else:
            return ".".join(self.parts)


class TypeName(_BaseTypeName):
    def __new__(cls, *parts: TypeNameLike) -> Self:
        if len(parts) == 1:
            (part,) = parts
            if isinstance(part, cls):
                return part

        return _BaseTypeName.__new__(cls, tuple(TypeName.__split_parts(parts)))

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

    def __truediv__(self, other: TypeNameLike) -> Self:
        return type(self)(self, other)
