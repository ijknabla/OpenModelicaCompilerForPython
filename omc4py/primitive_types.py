
__all__ = (
    "Boolean",
    "Integer",
    "Real",
    "String",
    "TypeName",
    "VariableName",
)

import arpeggio  # type: ignore
import functools
import numpy  # type: ignore
import typing


Real = numpy.double
Integer = numpy.intc
Boolean = numpy.bool
String = numpy.str


def valid_identifier(
    ident: str
) -> bool:
    try:
        parser.IDENT_parser.parse(ident)
        return True
    except arpeggio.NoMatch:
        return False


def split_type_specifier(
    type_specifier: str
) -> typing.Tuple[str, ...]:
    try:
        return arpeggio.visit_parse_tree(
            parser.type_specifier_parser.parse(
                type_specifier,
            ),
            visitor.TypeSpecifierSplitVisitor()
        )
    except arpeggio.NoMatch:
        raise ValueError(f"Invalid type_specifier, got {type_specifier!r}")


class VariableName(
):
    __slots__ = "__str"

    __str: str

    def __new__(
        cls,
        obj,
    ):
        if isinstance(obj, VariableName):
            return obj

        obj_str = str(obj)
        if not valid_identifier(obj_str):
            raise ValueError(
                f"Invalid modelica identifier, got {obj_str!r}"
            )

        return cls._from_str_no_check(obj_str)

    @classmethod
    def _from_str_no_check(
        cls,
        variableName: str,
    ) -> "VariableName":
        self = super().__new__(cls)
        self.__str = variableName
        return self

    def __eq__(
        self, other,
    ):
        if not isinstance(other, VariableName):
            return False
        else:
            return str(self) == str(other)

    def __hash__(
        self,
    ):
        return hash(str(self))

    def __str__(
        self,
    ) -> str:
        return self.__str

    def __repr__(
        self,
    ) -> str:
        return f"{type(self).__name__}({str(self)!r})"

    __to_omc_literal__ = __str__


@functools.total_ordering
class TypeName(
):
    __slots__ = (
        "__parts",
    )

    __parts: typing.Tuple[str, ...]

    def __new__(cls, *parts):
        return cls._from_parts_no_check(
            sum(
                map(cls.to_variableNames, parts),
                (),
            )
        )

    @classmethod
    def _from_parts_no_check(
        cls,
        parts: typing.Iterable[str]
    ) -> "TypeName":
        self = super().__new__(cls)
        self.__parts = tuple(parts)
        return self

    @property
    def parts(
        self,
    ) -> typing.Tuple[str, ...]:
        return self.__parts

    @property
    def is_absolute(self) -> bool: return str(self.parts[0]) == "."

    @property
    def last_identifier(
        self,
    ) -> VariableName:
        return VariableName(self.parts[-1])

    @property
    def parents(
        self,
    ) -> typing.Iterator["TypeName"]:
        for end in reversed(range(1, len(self.parts))):
            yield type(self)._from_parts_no_check(
                self.parts[:end]
            )

    @property
    def parent(
        self,
    ) -> "TypeName":
        for parent in self.parents:
            return parent
        else:
            return self

    @staticmethod
    def to_variableNames(
        name: typing.Union[str, VariableName, "TypeName"]
    ) -> typing.Tuple[str, ...]:
        if isinstance(name, str):
            return tuple(
                split_type_specifier(name)
            )
        elif isinstance(name, VariableName):
            return str(name),
        elif isinstance(name, TypeName):
            return name.parts
        else:
            raise TypeError()

    def __hash__(self):
        return hash(self.parts)

    def __eq__(self, other):
        return self.parts == type(self)(other).parts

    def __lt__(self, other):
        return self.parts < type(self)(other).parts

    def __repr__(
        self,
    ) -> str:
        return f"{type(self).__name__}({str(self)!r})"

    def __str__(
        self,
    ) -> str:
        if self.is_absolute:
            return "." + ".".join(self.parts[1:])
        else:
            return ".".join(self.parts)

    __to_omc_literal__ = __str__

    def __truediv__(
        self,
        other: typing.Union[str, VariableName, "TypeName"]
    ):
        return type(self)(self, other)


from omc4py.session import (  # noqa: E402
    parser,
    visitor,
)
