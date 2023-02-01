__all__ = (
    "parse_alias",
    "parse_enumerators",
    "parse_variableHasDefault",
)

import typing
from functools import lru_cache

from arpeggio import EOF, ParserPython, visit_parse_tree
from modelicalang import ParsingExpressionLike, returns_parsing_expression

from omc4py.classes import TypeName, VariableName
from omc4py.parser.syntax import OMCDialectSyntax

from . import visitor


class Syntax(OMCDialectSyntax):
    @classmethod
    @returns_parsing_expression
    def stored_definition_withEOF(cls) -> ParsingExpressionLike:
        return cls.stored_definition, EOF


@lru_cache(1)
def get_stored_definition_parser() -> ParserPython:
    with Syntax:
        return ParserPython(
            Syntax.stored_definition_withEOF,
            Syntax.COMMENT,
        )


def parse_alias(
    code: str,
) -> typing.Optional[typing.Tuple[VariableName, TypeName]]:
    return visit_parse_tree(
        get_stored_definition_parser().parse(code),
        visitor.AliasVisitor(),
    )


def parse_enumerators(
    code: str,
) -> typing.List[typing.Tuple[VariableName, str]]:
    return visit_parse_tree(
        get_stored_definition_parser().parse(code),
        visitor.EnumeratorsVisitor(),
    )


def parse_variableHasDefault(code: str) -> typing.Dict[VariableName, bool]:
    return dict(
        visit_parse_tree(
            get_stored_definition_parser().parse(code),
            visitor.VariableHasDefaultVisitor(),
        )
    )
