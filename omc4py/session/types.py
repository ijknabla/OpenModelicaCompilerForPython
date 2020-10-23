
__all__ = (
    "Boolean",
    "Integer",
    "Real",
    "String",
    "VariableName",
    "TypeName",
)


import arpeggio  # type: ignore
import functools
import numpy
import typing

from . import (
    parser,
    string,
)


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

        self = object.__new__(cls)
        self.__str = obj_str
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

    __parts: typing.Tuple[VariableName, ...]

    @property
    def parts(
        self,
    ) -> typing.Tuple[VariableName, ...]:
        return self.__parts

    @property
    def last_identifier(
        self,
    ) -> VariableName:
        return VariableName(self.parts[-1])

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


RecordFields = typing.Dict[
    str,
    typing.Callable[[typing.Any], typing.Any],
]


class OMCRecord(
    dict,
):
    __recordName__: typing.ClassVar[TypeName]
    __fields__: typing.ClassVar[RecordFields]

    def __init__(
        self,
        *args,
        **kwrds,
    ):
        _dict = dict(*args, **kwrds)
        expected_keys = self.__fields__.keys()
        actual_keys = _dict.keys()

        if actual_keys != expected_keys:
            raise KeyError(
                f"{type(self)} keys must be {expected_keys}, "
                f"got {actual_keys}"
            )

        self.update(_dict)

    def keys(
        self,
    ) -> typing.KeysView[str]:
        return self.__fields__.keys()

    def __setitem__(
        self,
        key, value
    ) -> None:
        if key not in self.keys():
            raise KeyError(
                f"Key must be one of the {self.keys()}, "
                f"got {key!r}"
            )
        value__internal__ = self.__fields__[key](value)
        super().__setitem__(
            key,
            value__internal__,
        )

    def __to_omc_literal__(
        self,
    ) -> str:
        def lines():
            recordNameLiteral = string.to_omc_literal(self.__recordName__)
            yield f"record {recordNameLiteral} "
            if self:
                elements = [
                    f"{variableName}={string.to_omc_literal(value)}"
                    for variableName, value in self.items()
                ]
                yield ", ".join(elements) + " "
            yield f"end {recordNameLiteral};"

        return "".join(lines())
