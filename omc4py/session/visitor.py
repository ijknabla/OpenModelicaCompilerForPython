
import arpeggio  # type: ignore

from .types import (
    Identifier,
    OMCRecord,
    TypeName,
)

from .. import parsers


class IdentifierVisitor(
    arpeggio.PTNodeVisitor,
):
    def visit_IDENT(self, node, *_):
        return Identifier(node.value)


class OMCValueVisitor(
    parsers.visitor.NumberVisitor,
    parsers.visitor.BooleanVisitor,
    parsers.visitor.StringVisitor,
    IdentifierVisitor,
    parsers.visitor.SequenceVisitor,
):
    def visit_name(
        self,
        node,
        children,
    ):
        return children.IDENT

    def visit_type_specifier(
        self,
        node,
        children
    ):
        name = children.name[0]
        if node[0].value == ".":
            return TypeName(Identifier(), *name)
        else:
            return TypeName(*name)

    def visit_omc_record_literal(
        self,
        node,
        children
    ):
        typeName = children.type_specifier[0]
        elements = children.omc_record_element_list[0]
        return OMCRecord(elements, typeName=typeName)

    def visit_omc_record_element(
        self,
        node,
        children,
    ):
        IDENT = children.IDENT[0]
        value = children.omc_value[0]
        return IDENT, value

    def visit_omc_record_element_list(
        self,
        node,
        children
    ):
        return children.omc_record_element
