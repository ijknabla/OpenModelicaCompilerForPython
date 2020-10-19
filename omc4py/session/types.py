
__all__ = (
    "VariableName",
    "TypeName",
)


import arpeggio  # type: ignore
import collections
import functools
import typing

from . import (
    parser,
    string,
)


def valid_identifier(
    ident: str
) -> bool:
    try:
        parser.IDENT_parser.parse(ident)
        return True
    except arpeggio.NoMatch:
        return False


class TypeSpecifierSplitVisitor(
    arpeggio.PTNodeVisitor,
):
    def visit_IDENT(
        self,
        node,
        children,
    ) -> str:
        return node.value

    def visit_name(
        self,
        node,
        children
    ) -> typing.Tuple[str, ...]:
        return tuple(children.IDENT)

    def visit_type_specifier(
        self,
        node,
        children,
    ) -> typing.Tuple[str, ...]:
        name = children.name[0]
        if node[0].value == ".":
            return ("", *name)
        else:
            return name


def split_type_specifier(
    type_specifier: str
) -> typing.Tuple[str, ...]:
    try:
        return arpeggio.visit_parse_tree(
            parser.type_specifier_parser.parse(
                type_specifier,
            ),
            TypeSpecifierSplitVisitor()
        )
    except arpeggio.NoMatch:
        raise ValueError(f"Invalid type_specifier, got {type_specifier!r}")


class VariableName(
    str
):
    def __repr__(
        self,
    ) -> str:
        return f"{type(self).__name__}({super().__repr__()})"

    def __to_omc_literal__(
        self,
    ) -> str:
        return super().__str__()


class NewVariableName(
):
    __slots__ = "__str"

    __str: str

    def __new__(
        cls,
        obj,
    ):
        if isinstance(obj, NewVariableName):
            return obj

        obj_str = str(obj)
        if not valid_identifier(obj_str):
            raise ValueError(
                f"Invalid modelica identifier, got {obj_str!r}"
            )

        self = object.__new__(cls)
        self.__str = obj_str
        return self

    def __eq__(
        self, other,
    ):
        if not isinstance(other, NewVariableName):
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

    __parts: typing.Tuple[VariableName, ...]

    @property
    def parts(
        self,
    ) -> typing.Tuple[VariableName, ...]:
        return self.__parts

    @property
    def parents(
        self,
    ) -> typing.Iterator["TypeName"]:
        parts = self.parts
        if parts[0]:
            begin = 0
        else:
            begin = 1
        end = len(parts)
        for end_of_slice in reversed(range(begin, end)):
            yield type(self)(*parts[:end_of_slice])

    @staticmethod
    def to_variableNames(
        name: typing.Union[str, VariableName, "TypeName"]
    ) -> typing.Tuple[VariableName, ...]:
        if isinstance(name, str):
            return tuple(
                map(VariableName, split_type_specifier(name))
            )
        elif isinstance(name, VariableName):
            return name,
        elif isinstance(name, TypeName):
            return name.parts
        else:
            raise TypeError()

    def __new__(cls, *parts):
        self = object.__new__(cls)
        self.__parts = sum(
            map(cls.to_variableNames, parts),
            (),
        )
        return self

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
        return ".".join(
            map(string.to_omc_literal, self.parts)
        )

    __to_omc_literal__ = __str__

    def __truediv__(
        self,
        other: typing.Union[str, VariableName, "TypeName"]
    ):
        return type(self)(self, other)


class OMCRecord(
    collections.UserDict,
):
    __typeName: TypeName

    def __init__(
        self,
        *args,
        typeName: typing.Union[str, TypeName],
        **kwrds,
    ):
        _dict = dict(*args, **kwrds)
        super().__init__(
            {
                str(key): value
                for key, value in _dict.items()
            }
        )
        self.__typeName = TypeName(typeName)

    @property
    def typeName(
        self
    ) -> TypeName:
        return self.__typeName

    def __repr__(
        self
    ):
        return (
            f"{type(self).__name__}("
            f"{super().__repr__()}, typeName={self.typeName!r}"
            f")"
        )

    def __to_omc_literal__(
        self,
    ) -> str:
        def lines():
            typeNameLiteral = string.to_omc_literal(self.typeName)
            yield f"record {typeNameLiteral} "
            if self:
                elements = [
                    f"{variableName}={string.to_omc_literal(value)}"
                    for variableName, value in self.items()
                ]
                yield ", ".join(elements) + " "
            yield f"end {typeNameLiteral};"

        return "".join(lines())
