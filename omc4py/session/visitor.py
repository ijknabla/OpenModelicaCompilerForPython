
import arpeggio  # type: ignore
import enum
import operator
import typing

from . import string
from .types import (
    Identifier,
    OMCRecord,
    TypeName,
)


class __DefaultFlag(enum.Flag):
    no_default = enum.auto()


def getitem_with_default(
    sequence: typing.Sequence,
    index: typing.Any,
    *,
    default=__DefaultFlag.no_default,
):
    try:
        return operator.getitem(sequence, index)
    except IndexError:
        if default is not __DefaultFlag.no_default:
            return default
        else:
            raise


class TypeSpecifierVisitor(
    arpeggio.PTNodeVisitor,
):
    def visit_IDENT(
        self,
        node,
        children
    ) -> Identifier:
        return Identifier(node.value)

    def visit_name(
        self,
        node,
        children,
    ) -> typing.Tuple[Identifier, ...]:
        return tuple(children.IDENT)

    def visit_type_specifier(
        self,
        node,
        children
    ) -> TypeName:
        name = children.name[0]
        if node[0].value == ".":
            return TypeName(Identifier(), *name)
        else:
            return TypeName(*name)


class NumberVisitor(
    arpeggio.PTNodeVisitor,
):
    def visit_sign(self, node, *_):
        return node.value

    def visit_UNSIGNED_NUMBER(self, node, *_):
        try:
            return int(node.value)
        except ValueError:
            return float(node.value)

    def visit_number(self, node, children):
        sign = getitem_with_default(
            children.sign, 0,
            default="+"
        )
        unsigned, = children.UNSIGNED_NUMBER

        if sign == "+":
            return +unsigned
        elif sign == "-":
            return -unsigned
        else:
            raise ValueError(
                f"sign must be '+' or '-'"
                f"got {sign}"
            )


class BooleanVisitor(
    arpeggio.PTNodeVisitor,
):
    def visit_TRUE(self, *_):
        return True

    def visit_FALSE(self, *_):
        return False

    def visit_boolean(self, node, children):
        return children[0]


class StringVisitor(
    arpeggio.PTNodeVisitor,
):
    def visit_STRING(self, node, *_):
        return string.unquote_modelica_string(node.value)


class SequenceVisitor(
    arpeggio.PTNodeVisitor,
):
    def visit_omc_value_list(self, node, children):
        return children.omc_value

    def visit_omc_tuple(self, node, children):
        value_list = getitem_with_default(
            children.omc_value_list,
            0,
            default=[],
        )
        return tuple(value_list)

    def visit_omc_array(self, node, children):
        value_list = getitem_with_default(
            children.omc_value_list,
            0,
            default=[],
        )
        return list(value_list)


class OMCRecordVisitor(
    TypeSpecifierVisitor,
):
    def visit_omc_record_element(
        self,
        node,
        children,
    ) -> typing.Tuple[Identifier, typing.Any]:
        IDENT = children.IDENT[0]
        value = children.omc_value[0]
        return IDENT, value

    def visit_omc_record_element_list(
        self,
        node,
        children
    ) -> typing.List[typing.Tuple[Identifier, typing.Any]]:
        return children.omc_record_element

    def visit_omc_record_literal(
        self,
        node,
        children
    ) -> OMCRecord:
        typeName = children.type_specifier[0]
        elements = children.omc_record_element_list[0]
        return OMCRecord(elements, typeName=typeName)


class OMCValueVisitor(
    NumberVisitor,
    BooleanVisitor,
    StringVisitor,
    SequenceVisitor,
    OMCRecordVisitor,
):
    pass
