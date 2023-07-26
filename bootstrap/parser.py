import sys

if sys.version_info < (3, 10):
    raise ImportError(
        f"python=={sys.version_info.major}.{sys.version_info.minor}"
        " not supported!"
    )

import enum
from collections.abc import Generator
from typing import Any, cast

from arpeggio import (
    EOF,
    NonTerminal,
    OneOrMore,
    Optional,
    ParserPython,
    Terminal,
    visit_parse_tree,
)
from modelicalang import ParsingExpressionLike, returns_parsing_expression
from typing_extensions import Never, Protocol

import neo.parser

from .interface import VariableNameString

Enumerator = tuple[VariableNameString, str | None]


def get_enumerators(stored_definition: str) -> list[Enumerator]:
    return cast(
        list[Enumerator],
        visit_parse_tree(parser.parse(stored_definition), EnumeratorVisitor()),
    )


def get_optionals(stored_definition: str) -> tuple[VariableNameString, ...]:
    return cast(
        tuple[VariableNameString, ...],
        visit_parse_tree(parser.parse(stored_definition), OptionalVisitor()),
    )


class Syntax(neo.parser.Syntax):
    @classmethod
    @returns_parsing_expression
    def root(cls) -> ParsingExpressionLike:
        return cls.stored_definition, EOF

    @classmethod
    @returns_parsing_expression
    def long_class_specifier(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            long-class-specifier :
               IDENT [ generic ] description-string composition `end` IDENT
               | `extends` IDENT [ class-modification ] description-string composition
                 `end` IDENT
        """  # noqa: E501
        return [
            (
                cls.IDENT,
                Optional(cls.generic),
                cls.description_string,
                cls.composition,
                cls.END,
                cls.IDENT,
            ),
            (
                cls.EXTENDS,
                cls.IDENT,
                Optional(cls.class_modification),
                cls.description_string,
                cls.composition,
                cls.END,
                cls.IDENT,
            ),
        ]

    @classmethod
    @returns_parsing_expression
    def generic(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            generic :
                "<" IDENT { "," IDENT } ">"
        """
        return "<", OneOrMore(cls.IDENT, sep=","), ">"


with Syntax:
    parser = ParserPython(Syntax.root, Syntax.COMMENT)


class Token(enum.Flag):
    optional = enum.auto()


class Children(Protocol):
    IDENT: list[VariableNameString]
    STRING: list[str]
    description: list[str]
    description_string: list[str]
    modification: list[Token]


class EnumeratorVisitor(neo.parser.Visitor):
    def visit_description_string(
        self,
        _: Never,
        children: Children,
    ) -> str:
        return "".join(children.STRING)

    def visit_description(
        self,
        _: Never,
        children: Children,
    ) -> str:
        (description,) = children.description_string
        return description

    def visit_enumeration_literal(
        self,
        _: Never,
        children: Children,
    ) -> Enumerator:
        (name,) = children.IDENT
        if children.description:
            (comment,) = children.description
        else:
            comment = None

        return (
            name,
            comment,
        )

    def visit__default__(
        self, _: Never, children: Children
    ) -> list[Enumerator]:
        def flatten(obj: Any) -> Generator[Enumerator, None, None]:
            if isinstance(obj, list):
                for item in obj:
                    yield from flatten(item)
            elif isinstance(obj, tuple):
                yield cast(Enumerator, obj)

        return list(flatten(children))


class OptionalVisitor(neo.parser.Visitor):
    def visit_modification(self, node: NonTerminal, _: Never) -> Token | None:
        for child in node:
            if isinstance(child, Terminal) and child.flat_str() in {"=", ":="}:
                return Token.optional
        return None

    def visit_declaration(
        self, _: Never, children: Children
    ) -> tuple[VariableNameString] | None:
        (name,) = children.IDENT

        if Token.optional in children.modification:
            return (name,)
        return None

    def visit__default__(
        self, _: Never, children: list[Any]
    ) -> tuple[VariableNameString, ...]:
        def flatten(obj: Any) -> Generator[VariableNameString, None, None]:
            if isinstance(obj, list):
                for item in obj:
                    yield from flatten(item)
            elif isinstance(obj, tuple):
                yield from obj

        return tuple(flatten(children))
