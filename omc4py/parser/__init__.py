from __future__ import annotations

__all__ = (
    "is_valid_identifier",
    "parse_typeName",
)

from functools import lru_cache
from typing import TYPE_CHECKING, Any, NewType, overload

from arpeggio import (
    EOF,
    NoMatch,
    ParserPython,
    ParseTreeNode,
    PTNodeVisitor,
    visit_parse_tree,
)
from modelicalang import ParsingExpressionLike, returns_parsing_expression
from typing_extensions import Literal

from .syntax import OMCDialectSyntax
from .visitor import TypeSpecifierVisitor

if TYPE_CHECKING:
    from neo.openmodelica import TypeName

TypeSpecifierParseTreeNode = NewType(
    "TypeSpecifierParseTreeNode", ParseTreeNode
)


def is_valid_identifier(ident: str) -> bool:
    try:
        _parse("IDENT", ident)
        return True
    except NoMatch:
        return False


def parse_typeName(type_specifier: str) -> TypeName:
    try:
        return _visit_parse_tree(
            _parse("type_specifier", type_specifier),
            TypeSpecifierVisitor(),
        )
    except NoMatch:
        raise ValueError(f"Invalid type_specifier, got {type_specifier!r}")


@overload
def _parse(syntax: Literal["IDENT"], text: str) -> ParseTreeNode:
    ...


@overload
def _parse(
    syntax: Literal["type_specifier"], text: str
) -> TypeSpecifierParseTreeNode:
    ...


def _parse(syntax: str, text: str) -> ParseTreeNode:
    return _get_parser(syntax).parse(text)


@lru_cache(None)
def _get_parser(syntax: str) -> ParserPython:
    @returns_parsing_expression
    def _root_rule_() -> ParsingExpressionLike:
        return getattr(OMCDialectSyntax, syntax), EOF

    with OMCDialectSyntax:
        return ParserPython(_root_rule_)


@overload
def _visit_parse_tree(
    parse_tree: TypeSpecifierParseTreeNode,
    visitor: TypeSpecifierVisitor,
) -> TypeName:
    ...


def _visit_parse_tree(
    parse_tree: ParseTreeNode,
    visitor: PTNodeVisitor,
) -> Any:
    return visit_parse_tree(parse_tree, visitor)
