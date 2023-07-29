from __future__ import annotations

import operator
from collections.abc import Iterator, Sequence
from typing import TYPE_CHECKING, TypeVar

from arpeggio import NonTerminal, PTNodeVisitor, Terminal
from typing_extensions import SupportsIndex

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
