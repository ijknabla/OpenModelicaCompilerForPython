
from .. import parsers

import arpeggio
import enum
import functools
import operator
import typing

from . import (
    StrOrPathLike,
    InteractiveOMC,
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


def to_omc_literal(
    obj: typing.Any
) -> str:
    if hasattr(obj, "__to_omc_literal__"):
        return obj.__to_omc_literal__()
    if isinstance(obj, str):
        return f'"{parsers.visitor.escape_py_string(obj)}"'
    return str(obj)


class IdentifierVisitor(
    arpeggio.PTNodeVisitor,
):
    identifierType: typing.Type

    def __init__(
        self,
        *args,
        identifierType: typing.Type = str,
        **kwrds,
    ):
        super().__init__(*args, **kwrds)
        self.identifierType = identifierType

    def visit_IDENT(self, node, *_):
        return self.identifierType(node.value)


class Component(
    typing.NamedTuple
):
    """
OpenModelica.Scripting.getComponentsTest.Component
"""
    className: str
    name: str
    comment: str
    isProtected: bool
    isFinal: bool
    isFlow: bool
    isStream: bool
    isReplaceable: bool
    variability: str
    innerOuter: str
    inputOutput: str
    dimensions: typing.Tuple[str]


class GetComponentsTestVisitor(
    IdentifierVisitor,
    parsers.visitor.StringVisitor,
    parsers.visitor.BooleanVisitor,
    parsers.visitor.SequenceVisitor,
):
    def visit_omc_record_element(
        self,
        node,
        children,
    ):
        IDENT = children.IDENT[0]
        value = children.omc_value[0]
        if isinstance(value, typing.List):
            value = tuple(value)
        return IDENT, value

    def visit_omc_record_element_list(
        self,
        node,
        children,
    ):
        return children.omc_record_element

    def visit_omc_record_literal(
        self,
        node,
        children,
    ):
        return Component(**dict(children.omc_record_element_list[0]))


@with_errorcheck
def getComponents(
    omc: InteractiveOMC,
    class_: str,
) -> typing.Tuple[Component, ...]:
    literal = omc.execute(
        f"getComponentsTest({class_})",
    )
    result = arpeggio.visit_parse_tree(
        parsers.omc_value_parser.parse(literal),
        GetComponentsTestVisitor(),
    )
    return tuple(result)


def bootstrap(
    omc_command: StrOrPathLike
):
    with InteractiveOMC.open(omc_command) as omc:
        for component in getComponents(
            omc,
            "OpenModelica.Scripting.getComponentsTest.Component"
        ):
            print(component)


if __name__ == "__main__":
    bootstrap("omc")
