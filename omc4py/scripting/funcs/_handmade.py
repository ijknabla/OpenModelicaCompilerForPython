
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
    "_ask",
    "getComponents",
)

import typing
import OMPython
import arpeggio
from .. import (
    types, exceptions
)
from ... import parsers


def _ask(
    omc: OMPython.OMCSessionBase,
    command: str,
    *args,
    **kwrds,
) -> str:

    modelica_arguments: typing.List[str] = []

    modelica_arguments.extend(
        f"{format(arg)}"
        for arg in args
    )
    modelica_arguments.extend(
        f"{key}={format(value)}"
        for key, value in kwrds.items()
    )

    return omc.ask(
        command, ' '+', '.join(modelica_arguments),
        parsed=False,
    )


def getComponents(
    omc: OMPython.OMCSessionBase,
    name: types.TypeNameLike,
):
    '''
function getComponents
  input TypeName name;
  output Component[:] components;

  record Component
    TypeName className;
    VariableName name;
    String comment;
    String protected;
    Boolean isFinal;
    Boolean isFlow;
    Boolean isStream;
    Boolean isReplaceable;
    String variability "'constant', 'parameter', 'discrete', ''";
    String innerOuter "'inner', 'outer', ''";
    String inputOutput "'input', 'output', ''";
    String dimensions[:];
  end Component;
end getComponentsTest;
    '''
    args = (
        types.TypeName(name),
    )

    __answer = _ask(omc, "getComponents", *args)
    try:
        __value = parsers.parseComponents(__answer)
    except arpeggio.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return types.Component[:](__value)
