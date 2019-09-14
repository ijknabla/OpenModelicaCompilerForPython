
__license__ = '''
/*
 * This file is part of OpenModelica.
 *
 * Copyright (c) 1998-CurrentYear, Open Source Modelica Consortium (OSMC),
 * c/o Linköpings universitet, Department of Computer and Information Science,
 * SE-58183 Linköping, Sweden.
 *
 * All rights reserved.
 *
 * THIS PROGRAM IS PROVIDED UNDER THE TERMS OF GPL VERSION 3 LICENSE OR
 * THIS OSMC PUBLIC LICENSE (OSMC-PL) VERSION 1.2.
 * ANY USE, REPRODUCTION OR DISTRIBUTION OF THIS PROGRAM CONSTITUTES
 * RECIPIENT'S ACCEPTANCE OF THE OSMC PUBLIC LICENSE OR THE GPL VERSION 3,
 * ACCORDING TO RECIPIENTS CHOICE.
 *
 * The OpenModelica software and the Open Source Modelica
 * Consortium (OSMC) Public License (OSMC-PL) are obtained
 * from OSMC, either from the above address,
 * from the URLs: http://www.ida.liu.se/projects/OpenModelica or
 * http://www.openmodelica.org, and in the OpenModelica distribution.
 * GNU version 3 is obtained from: http://www.gnu.org/copyleft/gpl.html.
 *
 * This program is distributed WITHOUT ANY WARRANTY; without
 * even the implied warranty of  MERCHANTABILITY or FITNESS
 * FOR A PARTICULAR PURPOSE, EXCEPT AS EXPRESSLY SET FORTH
 * IN THE BY RECIPIENT SELECTED SUBSIDIARY LICENSE CONDITIONS OF OSMC-PL.
 *
 * See the full OSMC Public License conditions for more details.
 *
 */
'''

__all__ = (
    "OMCValueVisitor",
    "ComponentsVisitor",
)

from typing import Sequence, Tuple
from arpeggio import PTNodeVisitor
from ..scripting.types import Component


def get_first_item(lis: list, default=None):
    try:
        return lis[0]
    except IndexError:
        return default


def replace_all(
    string: str,
    pairs: Sequence[Tuple[str, str]]
):
    result = string
    for old, new in pairs:
        result = result.replace(old, new)
    return result


class NumberVisitor(
    PTNodeVisitor,
):
    def visit_sign(self, node, *_):
        return node.value

    def visit_UNSIGNED_NUMBER(self, node, *_):
        try:
            return int(node.value)
        except ValueError:
            return float(node.value)

    def visit_number(self, node, children):
        sign = get_first_item(children.sign, default="+")
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
    PTNodeVisitor,
):
    def visit_TRUE(self, *_):
        return True

    def visit_FALSE(self, *_):
        return False

    def visit_boolean(self, node, children):
        return children[0]


class StringVisitor(
    PTNodeVisitor,
):
    def visit_STRING(self, node, *_):
        return replace_all(
            node.value[1:-1],
            [
                (r"\\", "\\"),
                (r"\'", "\'"),
                (r'\"', '\"'),
                (r"\a", "\a"),
                (r"\b", "\b"),
                (r"\f", "\f"),
                (r"\n", "\n"),
                (r"\t", "\t"),
                (r"\v", "\v"),
            ],
        )


class TypeNameVisitor(
    PTNodeVisitor,
):
    def visit_IDENT(self, node, *_):
        return node.value

    def visit_name(self, node, children):
        if len(children.IDENT) == 1:
            return children.IDENT[0]
        else:
            return children.IDENT


class SequenceVisitor(
    PTNodeVisitor,
):
    def visit_omc_value_list(self, node, children):
        return children.omc_value

    def visit_omc_tuple(self, node, children):
        value_list = get_first_item(
            children.omc_value_list,
            default=[],
        )
        return tuple(value_list)

    def visit_omc_array(self, node, children):
        value_list = get_first_item(
            children.omc_value_list,
            default=[],
        )
        return list(value_list)


class OMCValueVisitor(
    NumberVisitor,
    BooleanVisitor,
    StringVisitor,
    TypeNameVisitor,
    SequenceVisitor,
):
    def visit_omc_value(self, node, children):
        return children[0]


class DimensionsVisitor(
    PTNodeVisitor,
):
    def __init__(
        self,
        source: str,
    ):
        super().__init__()
        self.source = source

    def visit_dimensions(self, node, children):
        return children.subscript

    def visit_subscript(self, node, children):
        _flat_str = self.source[node.position:node.position_end]
        return _flat_str


class ComponentsVisitor(
    BooleanVisitor,
    StringVisitor,
    TypeNameVisitor,
    DimensionsVisitor,
):
    def visit_component_record(self, node, children):
        className, = children.name
        name, = children.IDENT
        (
            comment, protected, variability, innerOuter, inputOutput,
        ) = children.STRING
        isFinal, isFlow, isStream, isReplaceable, = children.boolean
        dimensions, = children.dimensions

        return Component(
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

    def visit_component_record_list(self, node, children):
        return children.component_record

    def visit_component_record_array(self, node, children):
        return get_first_item(
            children.component_record_list, default=[]
        )
