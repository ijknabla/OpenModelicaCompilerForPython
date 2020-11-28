
import arpeggio  # type: ignore
import enum
import numpy  # type: ignore
import operator
import typing

from omc4py.classes import (
    Integer,
    Real,
    TypeName,
    VariableName,
    VariableNameVisitor,
)

from omc4py import string


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


class TypeSpecifierVisitor(
    VariableNameVisitor,
):
    def visit_name(
        self,
        node,
        children,
    ) -> typing.List[VariableName]:
        return children.IDENT

    def visit_type_specifier(
        self,
        node,
        children
    ) -> TypeName:
        name = children.name[0]
        if node[0].value == ".":
            return TypeName(".", *name)
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
            signed = +unsigned
        elif sign == "-":
            signed = -unsigned

        if isinstance(signed, int):
            return Integer(signed)
        elif isinstance(signed, float):
            return Real(signed)
        else:
            raise TypeError(
                f"Unexpected number type, got {signed!r}: {type(signed)}"
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
        key = str(children.IDENT[0])
        value = children.omc_value[0]
        return key, value

    def visit_omc_record_element_list(
        self,
        node,
        children
    ) -> typing.List[typing.Tuple[str, typing.Any]]:
        return children.omc_record_element

    def visit_omc_record_literal(
        self,
        node,
        children
    ) -> typing.Dict[str, typing.Any]:
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


class OMCValueVisitor__v_1_13(
    OMCValueVisitor
):
    def visit_omc_record_literal(
        self, node, children
    ) -> typing.Dict[str, typing.Any]:
        className, _ = children.type_specifier
        record = super().visit_omc_record_literal(node, children)

        if (
            className == TypeName("OpenModelica.Scripting.SourceInfo")
            and "filename" in record and "fileName" not in record
        ):
            record["fileName"] = record.pop("filename")

        return record


class ComponentTuple(
    typing.NamedTuple,
):
    className: TypeName
    name: VariableName
    comment: str
    protected: str
    isFinal: bool
    isFlow: bool
    isStream: bool
    isReplaceable: bool
    variability: str
    innerOuter: str
    inputOutput: str
    dimensions: typing.Tuple[str, ...]


class ComponentArrayVisitor(
    BooleanVisitor,
    StringVisitor,
    TypeSpecifierVisitor,
):
    __source: str

    @property
    def source(self) -> str: return self.__source

    def __init__(
        self,
        source: str
    ):
        super().__init__()
        self.__source = source

    def visit_omc_component_array(self, node, children):
        return getitem_with_default(
            children.omc_component_list, 0,
            default=[],
        )

    def visit_omc_component_list(self, node, children):
        return list(children.omc_component)

    def visit_omc_component(self, node, children):
        className, = children.type_specifier
        name, = children.IDENT
        (
            comment, protected, variability, innerOuter, inputOutput,
        ) = children.STRING
        isFinal, isFlow, isStream, isReplaceable, = children.boolean
        dimensions, = children.omc_dimensions

        return ComponentTuple(
            className=className,
            name=name,
            comment=comment,
            protected=protected,
            isFinal=isFinal,
            isFlow=isFlow,
            isStream=isStream,
            isReplaceable=isReplaceable,
            variability=variability,
            innerOuter=innerOuter,
            inputOutput=inputOutput,
            dimensions=dimensions,
        )

    def visit_omc_dimensions(self, node, children):
        return tuple(
            getitem_with_default(
                children.subscript_list, 0,
                default=(),
            )
        )

    def visit_subscript_list(
        self, node, children,
    ):
        return children.subscript

    def visit_subscript(self, node, children):
        return self.source[
            node.position:node.position_end
        ]
