
__all__ = (
    "parse_alias",
    "parse_enumerators",
    "parse_variableHasDefault",
)

import arpeggio  # type: ignore
import typing

import omc4py.parser.syntax

from omc4py.classes import (
    TypeName,
    VariableName,
)

from . import visitor


@omc4py.parser.omc_parser_getter
def get_stored_definition_parser() -> arpeggio.Parser:
    return arpeggio.ParserPython(
        omc4py.parser.syntax.stored_definition_withEOF,
        omc4py.parser.syntax.std.CPP_STYLE_COMMENT,
    )


def parse_alias(
    code: str
) -> typing.Optional[typing.Tuple[VariableName, TypeName]]:
    return arpeggio.visit_parse_tree(
        get_stored_definition_parser().parse(code),
        visitor.AliasVisitor(),
    )


def parse_enumerators(
    code: str
) -> typing.List[typing.Tuple[VariableName, str]]:
    return arpeggio.visit_parse_tree(
        get_stored_definition_parser().parse(code),
        visitor.EnumeratorsVisitor(),
    )


def parse_variableHasDefault(
    code: str
) -> typing.Dict[VariableName, bool]:
    return dict(
        arpeggio.visit_parse_tree(
            get_stored_definition_parser().parse(code),
            visitor.VariableHasDefaultVisitor(),
        )
    )
