
from .. import parsers

import functools
import typing

from . import (
    StrOrPathLike,
    InteractiveOMC,
)


class OMCError(
    Exception
):
    ...


def with_errorcheck(
    func: typing.Callable
) -> typing.Callable:
    @functools.wraps(func)
    def wrapped(
        omc: InteractiveOMC,
        *args,
        check: bool = True,
        **kwrds,
    ):
        result = func(omc, *args, **kwrds)
        errorstring = omc.execute("getErrorString").rstrip()
        if errorstring:
            raise OMCError(errorstring)
        return result

    return wrapped


@with_errorcheck
def execute(
    omc: InteractiveOMC,
    expression: str,
):
    return omc.execute(expression)


def bootstrap(
    omc_command: StrOrPathLike
):
    with InteractiveOMC.open(omc_command) as omc:
        component_record_decl = execute(
            omc,
            "getComponentsTest("
            "    OpenModelica.Scripting.getComponentsTest.Component"
            ")",
        )

    tree = parsers.omc_value_parser.parse(component_record_decl)
    print(tree)
