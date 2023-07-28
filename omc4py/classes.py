from __future__ import annotations

__all__ = (
    # $Code types
    "VariableName",
    "TypeName",
)

import itertools
from collections.abc import Callable, Iterable, Iterator
from typing import Any, TypeVar, Union

from typing_extensions import Protocol, runtime_checkable

from .string import to_omc_literal

# Type hints

KT = TypeVar("KT")

VariableNameLike = Union[
    "TypeName",
    "VariableName",
    str,
]

TypeNameLike = VariableNameLike


@runtime_checkable
class SupportsToOMCLiteral(Protocol):
    def __to_omc_literal__(self) -> str:
        ...


# $Code classes OpenModelica.$Code.{VariableName, TypeName}

T_bvn = TypeVar("T_bvn", bound="_BaseVariableName")


class _BaseVariableName:
    __slots__ = ("__identifier",)
    __identifier: str

    def __new__(cls: type[T_bvn], identifier: str) -> T_bvn:
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


T_vn = TypeVar("T_vn", bound="VariableName")


class VariableName(_BaseVariableName):
    def __new__(cls: type[T_vn], obj: VariableNameLike) -> T_vn:
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

        if not parser.is_valid_identifier(identifier):
            raise ValueError(
                f"Invalid modelica identifier, got {identifier!r}"
            )

        return _BaseVariableName.__new__(cls, identifier)


T_btn = TypeVar("T_btn", bound="_BaseTypeName")


class _BaseTypeName:
    __slots__ = ("parts",)

    parts: tuple[str, ...]

    def __new__(cls: type[T_btn], parts: tuple[str, ...]) -> T_btn:
        self = super(_BaseTypeName, cls).__new__(cls)
        self.parts = parts
        return self

    @property
    def is_absolute(self) -> bool:
        return bool(self.parts) and self.parts[0] == "."

    def as_absolute(self: T_btn) -> T_btn:
        if self.is_absolute:
            return self
        else:
            return _BaseTypeName.__new__(type(self), (".", *self.parts))

    @property
    def last_identifier(self) -> VariableName:
        return VariableName(self.parts[-1])

    @property
    def parents(self: T_btn) -> Iterator[T_btn]:
        for end in reversed(range(1, len(self.parts))):
            yield _BaseTypeName.__new__(
                type(self),
                self.parts[:end],
            )

    @property
    def parent(self: T_btn) -> T_btn:
        for parent in self.parents:
            return parent
        else:
            return self

    def __hash__(self) -> int:
        return hash(self.parts)

    def __eq__(self: T_btn, other: Any) -> bool:
        return isinstance(other, _BaseTypeName) and self.parts == other.parts

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.parts})"

    def __str__(self) -> str:
        if self.is_absolute:
            return self.parts[0] + ".".join(self.parts[1:])
        else:
            return ".".join(self.parts)

    __to_omc_literal__ = __str__


T_tn = TypeVar("T_tn", bound="TypeName")


class TypeName(_BaseTypeName):
    def __new__(
        cls: type[T_tn], part: TypeNameLike, *parts: TypeNameLike
    ) -> T_tn:
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
        if isinstance(part, TypeName):
            yield from part.parts
        elif isinstance(part, VariableName):
            yield str(part)
        elif isinstance(part, str):
            if part == ".":
                yield part
            else:
                yield from parser.parse_typeName(part).parts
        else:
            raise TypeError(f"Unexpected part, got {part}: {type(part)}")

    def __repr__(self) -> str:
        return f"{type(self).__name__}({str(self)!r})"

    def __truediv__(self: T_tn, other: TypeNameLike) -> T_tn:
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


from . import parser  # noqa: E402
