
__all__ = (
    "parse_alias",
    "parse_components",
    "parse_enumerators",
    "parse_variableHasDefault",
)

import arpeggio  # type: ignore
import typing

from omc4py.parser import (
    parse_components,
    stored_definition_parser,
)
from omc4py.types import (
    TypeName,
    VariableName,
)

from . import visitor


def parse_alias(
    code: str
) -> typing.Optional[typing.Tuple[VariableName, TypeName]]:
    return arpeggio.visit_parse_tree(
        stored_definition_parser.parse(code),
        visitor.AliasVisitor(),
    )


def parse_enumerators(
    code: str
) -> typing.List[typing.Tuple[VariableName, str]]:
    return arpeggio.visit_parse_tree(
        stored_definition_parser.parse(code),
        visitor.EnumeratorsVisitor(),
    )


def parse_variableHasDefault(
    code: str
) -> typing.Dict[VariableName, bool]:
    return dict(
        arpeggio.visit_parse_tree(
            stored_definition_parser.parse(code),
            visitor.VariableHasDefaultVisitor(),
        )
    )
