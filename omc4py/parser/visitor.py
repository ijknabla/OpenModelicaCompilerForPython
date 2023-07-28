from __future__ import annotations

import operator
from collections.abc import Iterator, Sequence
from typing import TYPE_CHECKING, Any, NamedTuple, TypeVar, Union

import numpy
from arpeggio import NonTerminal, ParseTreeNode, PTNodeVisitor, Terminal
from numpy.typing import NDArray
from typing_extensions import SupportsIndex

from omc4py import string

if TYPE_CHECKING:
    from neo.openmodelica import TypeName, VariableName


T = TypeVar("T")


OMCValue = Union[
    "VariableName",
    "TypeName",
    NDArray[Any],
    "tuple[Any, ...]",
    "dict[str, Any]",
]


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


class OMCValueChildren(
    TypeSpecifierChildren, NumberChildren, BooleanChildren, StringChildren
):
    omc_value: list[OMCValue]
    omc_value_list: list[list[OMCValue]]
    omc_record_element: list[tuple[str, OMCValue]]
    omc_record_element_list: list[list[tuple[str, OMCValue]]]


class OMCValueVisitor(
    TypeSpecifierVisitor,
    NumberVisitor,
    BooleanVisitor,
    StringVisitor,
):
    def visit_omc_value_list(
        self, _: object, children: OMCValueChildren
    ) -> list[OMCValue]:
        return children.omc_value

    def visit_omc_tuple(
        self, _: object, children: OMCValueChildren
    ) -> tuple[OMCValue, ...]:
        if children.omc_value_list:
            return tuple(children.omc_value_list[0])
        else:
            return tuple()

    def visit_omc_array(
        self, _: object, children: OMCValueChildren
    ) -> NDArray[Any] | list[OMCValue]:
        if children.omc_value_list:
            (value_list,) = children.omc_value_list
            return numpy.array(value_list)
        else:
            return list()

    def visit_omc_record_element(
        self, _: object, children: OMCValueChildren
    ) -> tuple[str, OMCValue]:
        (key,) = map(str, children.IDENT)
        (value,) = children.omc_value
        return key, value

    def visit_omc_record_element_list(
        self, _: object, children: OMCValueChildren
    ) -> list[tuple[str, OMCValue]]:
        return children.omc_record_element

    def visit_omc_record_literal(
        self, _: object, children: OMCValueChildren
    ) -> dict[str, OMCValue]:
        (elements,) = children.omc_record_element_list
        return dict(elements)


class OMCValueVisitor__v_1_13(OMCValueVisitor):
    def visit_omc_record_literal(
        self, node: object, children: OMCValueChildren
    ) -> dict[str, OMCValue]:
        from neo.openmodelica import TypeName

        className, _ = children.type_specifier
        record = super().visit_omc_record_literal(node, children)

        if (
            className == TypeName("OpenModelica.Scripting.SourceInfo")
            and "filename" in record
            and "fileName" not in record
        ):
            record["fileName"] = record.pop("filename")

        return record


class ComponentTuple(
    NamedTuple,
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
    dimensions: tuple[str, ...]


class ComponentArrayChildren(
    BooleanChildren, StringChildren, TypeSpecifierChildren
):
    subscript: list[str]
    subscript_list: list[list[str]]
    omc_dimensions: list[tuple[str, ...]]
    omc_component: list[ComponentTuple]
    omc_component_list: list[list[ComponentTuple]]


class ComponentArrayVisitor(
    BooleanVisitor,
    StringVisitor,
    TypeSpecifierVisitor,
):
    __source: str

    @property
    def source(self) -> str:
        return self.__source

    def __init__(self, source: str):
        super().__init__()
        self.__source = source

    def visit_omc_component_array(
        self, _: object, children: ComponentArrayChildren
    ) -> list[ComponentTuple]:
        return getitem_with_default(
            children.omc_component_list,
            0,
            default=[],
        )

    def visit_omc_component_list(
        self, _: object, children: ComponentArrayChildren
    ) -> list[ComponentTuple]:
        return children.omc_component

    def visit_omc_component(
        self, _: object, children: ComponentArrayChildren
    ) -> ComponentTuple:
        (className,) = children.type_specifier
        (name,) = children.IDENT
        (
            comment,
            protected,
            variability,
            innerOuter,
            inputOutput,
        ) = children.STRING
        (
            isFinal,
            isFlow,
            isStream,
            isReplaceable,
        ) = children.boolean
        (dimensions,) = children.omc_dimensions

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

    def visit_omc_dimensions(
        self, _: object, children: ComponentArrayChildren
    ) -> tuple[str, ...]:
        return tuple(
            getitem_with_default(
                children.subscript_list,
                0,
                default=[],
            )
        )

    def visit_subscript_list(
        self,
        _: object,
        children: ComponentArrayChildren,
    ) -> list[str]:
        return children.subscript

    def visit_subscript(self, node: ParseTreeNode, _: object) -> str:
        return self.source[node.position : node.position_end]
