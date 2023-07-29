__all__ = ("OMCDialectSyntax",)

from arpeggio import RegExMatch
from modelicalang import v3_4
from modelicalang._backend import (
    ParsingExpressionLike,
    returns_parsing_expression,
)


class OMCDialectSyntax(v3_4.Syntax):
    @classmethod
    @returns_parsing_expression
    def IDENT(cls) -> ParsingExpressionLike:
        return [super().IDENT(), RegExMatch(r"\$\w*")]
