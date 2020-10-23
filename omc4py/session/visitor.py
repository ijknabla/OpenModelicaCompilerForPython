
import arpeggio  # type: ignore
import enum
import numpy  # type: ignore
import operator
import typing

from . import string
from .types import (
    VariableName,
    TypeName,
)


def flatten_list(
    lis: list
):
    for item in lis:
        if isinstance(item, list):
            yield from flatten_list(item)
        else:
            yield item


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
            return (".", *name)
        else:
            return name


class TypeSpecifierVisitor(
    arpeggio.PTNodeVisitor,
):
    def visit_IDENT(
        self,
        node,
        children
    ) -> str:
        return node.value

    def visit_name(
        self,
        node,
        children,
    ) -> typing.Tuple[str, ...]:
        return tuple(children.IDENT)

    def visit_type_specifier(
        self,
        node,
        children
    ) -> TypeName:
        name = children.name[0]
        if node[0].value == ".":
            return TypeName._from_parts_no_check((".", *name))
        else:
            return TypeName._from_parts_no_check(name)


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
        if children.omc_value_list:
            return tuple(children.omc_value_list[0])
        else:
            return tuple()

    def visit_omc_array(self, node, children):
        if children.omc_value_list:
            return numpy.array(children.omc_value_list[0])
        else:
            return list()


class OMCRecordVisitor(
    TypeSpecifierVisitor,
):
    def visit_omc_record_element(
        self,
        node,
        children,
    ) -> typing.Tuple[str, typing.Any]:
        IDENT = children.IDENT[0]
        value = children.omc_value[0]
        return str(IDENT), value

    def visit_omc_record_element_list(
        self,
        node,
        children
    ) -> typing.List[typing.Tuple[VariableName, typing.Any]]:
        return children.omc_record_element

    def visit_omc_record_literal(
        self,
        node,
        children
    ) -> dict:
        elements = children.omc_record_element_list[0]
        return dict(elements)


class OMCValueVisitor(
    NumberVisitor,
    BooleanVisitor,
    StringVisitor,
    SequenceVisitor,
    OMCRecordVisitor,
):
    pass


class DefaultValueInfo(
    typing.NamedTuple
):
    name: VariableName
    hasDefault: bool


class DefaultValueInfoVisitor(
    TypeSpecifierVisitor,
):
    def visit__default__(
        self,
        node,
        children,
    ) -> typing.List[DefaultValueInfo]:
        return [
            child
            for child in flatten_list(children)
            if isinstance(child, DefaultValueInfo)
        ]

    def visit_declaration(
        self,
        node,
        children
    ) -> DefaultValueInfo:
        name = children.IDENT[0]
        hasDefault = bool(children.modification)
        return DefaultValueInfo(
            name=name,
            hasDefault=hasDefault,
        )


class EnumeratorInfo(
    typing.NamedTuple,
):
    name: VariableName
    comment: str


class EnumeratorVisitor(
    TypeSpecifierVisitor,
    StringVisitor,
):
    def visit_enumeration_literal(
        self,
        node,
        children,
    ) -> EnumeratorInfo:
        name = children.IDENT[0]
        comment = getitem_with_default(
            children.comment, 0,
            default=""
        )
        return EnumeratorInfo(
            name=name,
            comment=comment,
        )

    def visit_comment(
        self,
        node,
        children
    ):
        return children.string_comment[0]

    def visit_string_comment(
        self,
        node,
        children,
    ):
        return "".join(children.STRING)

    def visit__default__(
        self,
        node,
        children
    ):
        return [
            child
            for child in flatten_list(children)
            if isinstance(child, EnumeratorInfo)
        ]


class AliasInfo(
    typing.NamedTuple
):
    name: VariableName
    target: TypeName


class AliasVisitor(
    TypeSpecifierVisitor,
):
    def visit_short_class_specifier(
        self,
        node,
        children
    ) -> typing.Optional[typing.Tuple[VariableName, TypeName]]:
        variableName = VariableName(children.IDENT[0])
        type_specifier = getitem_with_default(
            children.type_specifier, 0,
            default=None
        )

        if type_specifier is None:
            return None
        else:
            return AliasInfo(
                name=variableName,
                target=type_specifier
            )

    def visit_file(
        self,
        node,
        children,
    ):
        aliases = [
            child
            for child in children
            if isinstance(child, AliasInfo)
        ]
        if aliases:
            return aliases[0]
        return None
