
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
    "NoMatch",
    "parseOMCValue",
    "parseComponents",
)

from arpeggio import (
    NoMatch,
    EOF, ParserPython, visit_parse_tree,
)
from .syntax import (
    omc_dialect_context,
    omc_value, component_record_array,
)
from .visitor import (
    OMCValueVisitor,
    ComponentsVisitor,
)


def omc_value_withEOF():
    return omc_value, EOF


with omc_dialect_context:
    omc_value_parser = ParserPython(omc_value_withEOF)


def parseOMCValue(omc_string: str):
    tree = omc_value_parser.parse(omc_string)
    return visit_parse_tree(
        tree, OMCValueVisitor(),
    )


def component_record_array_withEOF():
    return component_record_array, EOF


with omc_dialect_context:
    components_perser = ParserPython(component_record_array_withEOF)


def parseComponents(omc_string: str):
    tree = components_perser.parse(omc_string)
    return visit_parse_tree(
        tree, ComponentsVisitor(omc_string),
    )
