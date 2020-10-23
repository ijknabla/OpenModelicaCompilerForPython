
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


def _VariableName_from_valid_identifier_no_check(
    cls: typing.Type["VariableName"],
    identifier: str,
):
    variableName = object.__new__(VariableName)
    variableName._VariableName__str = identifier
    return variableName


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

        return _VariableName_from_valid_identifier_no_check(
            cls,
            obj_str
        )

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
            cls.__checked_parts(
                parts
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
    def __checked_parts(
        objs: typing.Iterable,
    ) -> typing.Iterator[str]:

        def not_checked_parts(
        ) -> typing.Iterator[str]:
            for obj in objs:
                if isinstance(obj, TypeName):
                    yield from obj.parts
                elif isinstance(obj, VariableName):
                    yield str(obj)
                else:
                    yield from split_type_specifier(str(obj))

        for i, part in enumerate(
            not_checked_parts()
        ):
            if part == "." and not i == 0:
                raise ValueError(
                    f"parts[{i}] is invalid, got {part!r}"
                )
            yield part

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
            return self.parts[0] + ".".join(self.parts[1:])
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
