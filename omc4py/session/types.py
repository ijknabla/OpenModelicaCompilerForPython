
__all__ = (
    "Identifier",
    "TypeName",
)


import arpeggio  # type: ignore
import functools
import typing

from . import (
    parser,
    string,
)


class TypeSpecifierVisitor(
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
    return arpeggio.visit_parse_tree(
        parser.type_specifier_parser.parse(
            type_specifier,
        ),
        TypeSpecifierVisitor()
    )


class Identifier(
    str
):
    def __to_omc_literal__(
        self
    ) -> str:
        return str(self)


IdentifierTuple = typing.Tuple[Identifier, ...]


@functools.total_ordering
class TypeName(
):
    __slots__ = (
        "__parts",
    )

    __parts: IdentifierTuple

    @property
    def parts(self) -> IdentifierTuple:
        return self.__parts

    @staticmethod
    def to_identifiers(
        name: typing.Union[str, Identifier, "TypeName"]
    ) -> IdentifierTuple:
        if isinstance(name, str):
            return tuple(
                map(Identifier, split_type_specifier(name))
            )
        elif isinstance(name, Identifier):
            return name,
        elif isinstance(name, TypeName):
            return name.parts
        else:
            raise TypeError()

    def __new__(cls, *parts):
        self = object.__new__(cls)
        self.__parts = sum(
            map(cls.to_identifiers, parts),
            (),
        )
        return self

    def __hash__(self):
        return hash(self.parts)

    def __eq__(self, other):
        return self.parts == type(self)(other).parts

    def __lt__(self, other):
        return self.parts < type(self)(other).parts

    def __str__(
        self
    ) -> str:
        return ".".join(
            map(string.to_omc_literal, self.parts)
        )

    __to_omc_literal__ = __str__

    def __truediv__(
        self,
        other: typing.Union[str, Identifier, "TypeName"]
    ):
        return type(self)(self, other)
