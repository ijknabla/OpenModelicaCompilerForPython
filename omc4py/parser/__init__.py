from __future__ import annotations

__all__ = (
    "ComponentTuple",
    "is_valid_identifier",
    "parse_OMCExceptions",
    "parse_OMCValue",
    "parse_typeName",
    "parse_components",
)

import functools
import re
from collections.abc import Iterator
from functools import lru_cache
from typing import Any, NewType, Union, overload

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

from .. import exception
from ..classes import TypeName
from . import visitor
from .syntax import OMCDialectSyntax
from .visitor import ComponentTuple

OMCValue = Any
TypeSpecifierParseTreeNode = NewType(
    "TypeSpecifierParseTreeNode", ParseTreeNode
)
OMCComponentArrayParseTreeNode = NewType(
    "OMCComponentArrayParseTreeNode", ParseTreeNode
)
OMCValueParseTreeNode = NewType("OMCValueParseTreeNode", ParseTreeNode)


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
            visitor.TypeSpecifierVisitor(),
        )
    except NoMatch:
        raise ValueError(f"Invalid type_specifier, got {type_specifier!r}")


def parse_components(literal: str) -> list[ComponentTuple]:
    return _visit_parse_tree(
        _parse("omc_component_array", literal),
        visitor.ComponentArrayVisitor(source=literal),
    )


def parse_OMCValue(literal: str) -> OMCValue:
    return _visit_parse_tree(
        _parse("omc_value", literal),
        visitor.OMCValueVisitor(),
    )


def parse_OMCValue__v_1_13(literal: str) -> OMCValue:
    return _visit_parse_tree(
        _parse("omc_value", literal),
        visitor.OMCValueVisitor__v_1_13(),
    )


def parse_OMCExceptions(
    error_string: str,
) -> Iterator[exception.OMCException]:
    for matched in _get_omc_exception_pattern().finditer(error_string):
        level = matched.group("level").lower()
        message = matched.group("message")

        if level == "notification":
            yield exception.OMCNotification(message)
        elif level == "warning":
            yield exception.OMCWarning(message)
        elif level == "error":
            yield exception.OMCError(message)
        else:  # Not-implemented now, but valid level (for future)
            yield exception.OMCError(message)


@overload
def _parse(syntax: Literal["IDENT"], text: str) -> ParseTreeNode:
    ...


@overload
def _parse(
    syntax: Literal["type_specifier"], text: str
) -> TypeSpecifierParseTreeNode:
    ...


@overload
def _parse(
    syntax: Literal["omc_component_array"], text: str
) -> OMCComponentArrayParseTreeNode:
    ...


@overload
def _parse(syntax: Literal["omc_value"], text: str) -> OMCValueParseTreeNode:
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
    parse_tree: OMCComponentArrayParseTreeNode,
    visitor: visitor.ComponentArrayVisitor,
) -> list[ComponentTuple]:
    ...


@overload
def _visit_parse_tree(
    parse_tree: TypeSpecifierParseTreeNode,
    visitor: visitor.TypeSpecifierVisitor,
) -> TypeName:
    ...


@overload
def _visit_parse_tree(
    parse_tree: OMCValueParseTreeNode,
    visitor: Union[visitor.OMCValueVisitor, visitor.OMCValueVisitor__v_1_13],
) -> OMCValue:
    ...


def _visit_parse_tree(
    parse_tree: ParseTreeNode,
    visitor: PTNodeVisitor,
) -> Any:
    return visit_parse_tree(parse_tree, visitor)


@functools.lru_cache(1)
def _get_omc_exception_pattern() -> re.Pattern[str]:
    return re.compile(
        (
            r"(\[(?P<info>[^]]*)\]\s+)?"
            r"(?P<level>\w+):\s+"
            r"(?P<message>((?!$).)*)$"
        ),
        re.MULTILINE,
    )
