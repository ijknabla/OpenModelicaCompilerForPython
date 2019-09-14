
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
    # basic primitive types
    "Real", "Integer", "Boolean", "String",
    # language element type in $Code (omc namespace)
    "VariableName", "VariableNames",
    "TypeName",
    "Component",
)

from typing import (
    Union,
    List,
)
import numbers
import arpeggio
from collections import namedtuple
from modelica_language.types import (
    PrimitiveModelicaObject,
    PrimitiveString,
)

from modelica_language.types import PrimitiveReal as Real
from modelica_language.types import PrimitiveInteger as Integer
from modelica_language.types import PrimitiveBoolean as Boolean
from modelica_language.types import PrimitiveString as String


class VariableName(
    PrimitiveString,
):
    def __format__(self, format_spec):
        return f"{str(self):{format_spec}}"


VariableNames = VariableName[:]


def IDENT():
    from modelica_language.parsers.regex import (
        digit, nondigit, q_ident,
    )
    return arpeggio.RegExMatch(
        rf'((\$|{nondigit})({digit}|{nondigit})*)|({q_ident})'
    )


def type_name():
    return arpeggio.OneOrMore(IDENT, sep='.')


type_name_parser = arpeggio.ParserPython(type_name)


class TypeNameSplitter(
    arpeggio.PTNodeVisitor,
):
    def visit_IDENT(self, node, *_):
        return node.value

    def visit_type_name(self, node, children):
        return children.IDENT


def split_type_name(string: str):
    tree = type_name_parser.parse(string)
    return arpeggio.visit_parse_tree(
        tree, TypeNameSplitter()
    )


class TypeName(
    PrimitiveModelicaObject,
):
    def __init__(self, obj=None):
        self.__parts: List[str] = []

        if obj is None:
            return
        elif isinstance(obj, TypeName):
            typename = obj
            self.copyin(typename)
            return
        elif isinstance(obj, str):
            ident = obj
            self.__parts.extend(split_type_name(ident))
        else:
            for elem in obj:
                self /= type(self)(elem)

    @property
    def parts(self):
        return tuple(self.__parts)

    def __repr__(self):
        return f"{type(self).__name__}({str(self)!r})"

    def __str__(self):
        return ".".join(self.parts)

    def copyin(self, other: 'TypeName'):
        self.__parts.clear()
        self /= other

    def __itruediv__(self, other):
        if not isinstance(other, TypeName):
            other = TypeName(other)
        self.__parts.extend(other.parts)
        return self

    def __truediv__(self, other):
        new = type(self)()
        new /= self
        new /= other
        return new


Component = namedtuple(
    "Component",
    [
        "className",  # TypeName
        "name",  # VariableName
        "comment",  # String
        "protected",  # String
        "isFinal",  # Boolean
        "isFlow",  # Boolean
        "isStream",  # Boolean
        "isReplaceable",  # Boolean
        "variability",  # String
        "innerOuter",  # String
        "inputOutput",  # String
        "dimensions",  # array of subscript
    ]
)

# Basic type annotation
IntegerLike = Union[Integer, numbers.Integral]
RealLike = Union[Real, numbers.Real]
BooleanLike = Union[Boolean, bool]
StringLike = Union[String, str]

# Language element type annotation
VariableNameLike = Union[VariableName, StringLike]
TypeNameLike = Union[TypeName, VariableNameLike]
