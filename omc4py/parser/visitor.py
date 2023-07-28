from __future__ import annotations

import operator
from collections.abc import Iterator, Sequence
from typing import TYPE_CHECKING, TypeVar, Union

from arpeggio import NonTerminal, PTNodeVisitor, Terminal
from typing_extensions import SupportsIndex

from omc4py import string

if TYPE_CHECKING:
    from neo.openmodelica import TypeName, VariableName


T = TypeVar("T")


def getitem_with_default(
    sequence: Sequence[T],
    index: SupportsIndex,
    *,
    default: T,
) -> T:
    try:
        return operator.getitem(sequence, index)
    except IndexError:
        return default


class TypeSpecifierChildren:
    IDENT: list[VariableName]
    type_specifier: list[TypeName]


class TypeSpecifierVisitor(PTNodeVisitor):
    def visit_IDENT(
        self,
        node: Terminal,
        _: object,
    ) -> VariableName:
        from neo.openmodelica import VariableName, _BaseVariableName

        return _BaseVariableName.__new__(VariableName, node.value)

    def visit_type_specifier(self, node: NonTerminal, _: object) -> TypeName:
        from neo.openmodelica import TypeName, _BaseTypeName

        parts = tuple(
            s
            for i, s in enumerate(self.__iter_terminal_nodes(node))
            if s != "." or i == 0
        )

        return _BaseTypeName.__new__(TypeName, parts)

    @classmethod
    def __iter_terminal_nodes(cls, node: NonTerminal) -> Iterator[str]:
        for child in node:
            if isinstance(child, Terminal):
                yield child.value
            elif isinstance(child, NonTerminal):
                yield from cls.__iter_terminal_nodes(child)


class NumberChildren:
    sign: list[str]
    UNSIGNED_NUMBER: list[Union[int, float]]
    number: list[Union[int, float]]


class NumberVisitor(
    PTNodeVisitor,
):
    def visit_sign(self, node: Terminal, _: object) -> str:
        return node.value

    def visit_UNSIGNED_NUMBER(
        self, node: Terminal, _: object
    ) -> Union[int, float]:
        try:
            return int(node.value)
        except ValueError:
            return float(node.value)

    def visit_number(
        self, _: object, children: NumberChildren
    ) -> Union[int, float]:
        sign = getitem_with_default(children.sign, 0, default="+")
        (unsigned,) = children.UNSIGNED_NUMBER

        if sign == "+":
            signed = +unsigned
        elif sign == "-":
            signed = -unsigned

        if isinstance(signed, int):
            return int(signed)
        elif isinstance(signed, float):
            return float(signed)
        else:
            raise NotImplementedError(
                f"Unexpected number type, got {signed!r}: {type(signed)}"
            )


class BooleanChildren:
    TRUE: list[bool]
    FALSE: list[bool]
    boolean: list[bool]


class BooleanVisitor(
    PTNodeVisitor,
):
    def visit_TRUE(self, *_: object) -> bool:
        return True

    def visit_FALSE(self, *_: object) -> bool:
        return False

    def visit_boolean(self, _: object, children: BooleanChildren) -> bool:
        (value,) = children.TRUE + children.FALSE
        return value


class StringChildren:
    STRING: list[str]


class StringVisitor(
    PTNodeVisitor,
):
    def visit_STRING(self, node: Terminal, _: object) -> str:
        return string.unquote_modelica_string(node.value)
