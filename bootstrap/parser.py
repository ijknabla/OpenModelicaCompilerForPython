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
from modelicalang import ParsingExpressionLike
from typing_extensions import Never, Protocol

import omc4py.parser

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


class Syntax(omc4py.parser.Syntax):
    @classmethod
    def root(cls) -> ParsingExpressionLike:
        return cls.stored_definition, EOF

    @classmethod
    def long_class_specifier(cls) -> ParsingExpressionLike:
        """
        .. code-block:: modelicapeg

            long-class-specifier :
               IDENT [ generic ] string-comment composition `end` IDENT
               | `extends` IDENT [ class-modification ] string-comment composition
               `end` IDENT
        """  # noqa: E501
        return [
            (
                cls.IDENT,
                Optional(cls.generic),
                cls.string_comment,
                cls.composition,
                cls.END,
                cls.IDENT,
            ),
            (
                cls.EXTENDS,
                cls.IDENT,
                Optional(cls.class_modification),
                cls.string_comment,
                cls.composition,
                cls.END,
                cls.IDENT,
            ),
        ]

    @classmethod
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
    string_comment: list[str]
    modification: list[Token]


class EnumeratorVisitor(omc4py.parser.Visitor):
    def visit_string_comment(
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
        (description,) = children.string_comment
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


class OptionalVisitor(omc4py.parser.Visitor):
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
