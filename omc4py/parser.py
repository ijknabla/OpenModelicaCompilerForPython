from __future__ import annotations

from functools import lru_cache
from typing import (
    TYPE_CHECKING,
    Any,
    Iterable,
    List,
    Literal,
    Protocol,
    Tuple,
    Union,
)

from arpeggio import (
    EOF,
    NoMatch,
    NonTerminal,
    OneOrMore,
    Optional,
    ParserPython,
    PTNodeVisitor,
    RegExMatch,
    Terminal,
    ZeroOrMore,
    visit_parse_tree,
)
from modelicalang import ParsingExpressionLike, v3_4

from .string2 import _unquote_modelica_string

if TYPE_CHECKING:
    from typing_extensions import Never


def is_variablename(variablename: str) -> bool:
    parser = _get_variablename_parser()
    try:
        parser.parse(variablename)
        return True
    except NoMatch:
        return False


def split_typename_parts(typename: str) -> tuple[str, ...]:
    return visit_parse_tree(  # type: ignore
        _get_typename_parser().parse(typename),
        TypeNameSplitVisitor(),
    )


@lru_cache(1)
def _get_variablename_parser() -> ParserPython:
    def root() -> ParsingExpressionLike:
        return Syntax.variablename, EOF

    with Syntax:
        return ParserPython(root)


@lru_cache(1)
def _get_typename_parser() -> ParserPython:
    def root() -> ParsingExpressionLike:
        return Syntax.typename, EOF

    with Syntax:
        return ParserPython(root)


class Syntax(v3_4.Syntax):
    # Dialects

    @classmethod
    def IDENT(cls) -> ParsingExpressionLike:
        return [super().IDENT(), RegExMatch(r"\$\w*")]

    # Primitives

    @classmethod
    def real(cls) -> ParsingExpressionLike:
        return Optional(cls.SIGN), cls.UNSIGNED_NUMBER

    @classmethod
    def integer(cls) -> ParsingExpressionLike:
        return Optional(cls.SIGN), cls.UNSIGNED_INTEGER

    @classmethod
    def boolean(cls) -> ParsingExpressionLike:
        return [cls.TRUE, cls.FALSE]

    @classmethod
    def variablename(cls) -> ParsingExpressionLike:
        return [
            RegExMatch(
                "[A-Z_a-z][0-9A-Z_a-z]*|'([\\ !\\#-\\&\\(-\\[\\]-_a-\\~]|\\\\'|\\\\\"|\\\\\\?|\\\\\\\\|\\\\a|\\\\b|\\\\f|\\\\n|\\\\r|\\\\t|\\\\v)([\\ -\\&\\(-\\[\\]-_a-\\~]|\\\\'|\\\\\"|\\\\\\?|\\\\\\\\|\\\\a|\\\\b|\\\\f|\\\\n|\\\\r|\\\\t|\\\\v)*'"  # noqa: E501
            ),
            RegExMatch(r"\$\w*"),
        ]

    @classmethod
    def typename(cls) -> ParsingExpressionLike:
        return Optional(cls.DOT), OneOrMore(cls.variablename, sep=".")

    @classmethod
    def component(cls) -> ParsingExpressionLike:
        return (
            "{",
            (
                *(cls.typename, ","),  # className
                *(cls.IDENT, ","),  # name
                *(cls.STRING, ","),  # comment
                *(cls.STRING, ","),  # protected
                *(cls.boolean, ","),  # isFinal
                *(cls.boolean, ","),  # isFlow
                *(cls.boolean, ","),  # isStream
                *(cls.boolean, ","),  # isReplaceable
                *(cls.STRING, ","),  # variability
                *(cls.STRING, ","),  # innerOuter
                *(cls.STRING, ","),  # inputOutput
                cls.subscript_list,  # dimensions
            ),
            "}",
        )

    @classmethod
    def subscript_list(cls) -> ParsingExpressionLike:
        return "{", ZeroOrMore(cls.subscript, sep=","), "}"

    @classmethod
    def record(cls) -> ParsingExpressionLike:
        return (
            cls.RECORD,
            cls.type_specifier,
            ZeroOrMore(cls.record_element, sep=","),
            cls.END,
            cls.type_specifier,
            ";",
        )

    @classmethod
    def record_element(cls) -> ParsingExpressionLike:
        return cls.IDENT, "=", cls.record_expression

    @classmethod
    def record_expression(cls) -> ParsingExpressionLike:
        return [
            cls.record_primary,
            cls.real_primary,
            cls.boolean_primary,
            cls.string_primary,
            cls.typename_primary,
        ]

    # Additional rules

    @classmethod
    def DOT(cls) -> ParsingExpressionLike:
        return "."

    @classmethod
    def SIGN(cls) -> ParsingExpressionLike:
        return RegExMatch(r"[+-]")

    # Primary & Array

    @classmethod
    def real_primary(cls) -> ParsingExpressionLike:
        return [cls.real, cls.real_array]

    @classmethod
    def real_array(cls) -> ParsingExpressionLike:
        return "{", ZeroOrMore(cls.real_primary, sep=","), "}"

    @classmethod
    def integer_primary(cls) -> ParsingExpressionLike:
        return [cls.integer, cls.integer_array]

    @classmethod
    def integer_array(cls) -> ParsingExpressionLike:
        return "{", ZeroOrMore(cls.integer_primary, sep=","), "}"

    @classmethod
    def boolean_primary(cls) -> ParsingExpressionLike:
        return [cls.boolean, cls.boolean_array]

    @classmethod
    def boolean_array(cls) -> ParsingExpressionLike:
        return "{", ZeroOrMore(cls.boolean_primary, sep=","), "}"

    @classmethod
    def string_primary(cls) -> ParsingExpressionLike:
        return [cls.STRING, cls.string_array]

    @classmethod
    def string_array(cls) -> ParsingExpressionLike:
        return "{", ZeroOrMore(cls.string_primary, sep=","), "}"

    @classmethod
    def variablename_primary(cls) -> ParsingExpressionLike:
        return [cls.variablename, cls.variablename_array]

    @classmethod
    def variablename_array(cls) -> ParsingExpressionLike:
        return "{", ZeroOrMore(cls.variablename_primary, sep=","), "}"

    @classmethod
    def typename_primary(cls) -> ParsingExpressionLike:
        return [cls.typename, cls.typename_array]

    @classmethod
    def typename_array(cls) -> ParsingExpressionLike:
        return "{", ZeroOrMore(cls.typename_primary, sep=","), "}"

    @classmethod
    def component_primary(cls) -> ParsingExpressionLike:
        return [cls.component, cls.component_array]

    @classmethod
    def component_array(cls) -> ParsingExpressionLike:
        return "{", ZeroOrMore(cls.component_primary, sep=","), "}"

    @classmethod
    def record_primary(cls) -> ParsingExpressionLike:
        return [cls.record, cls.record_array]

    @classmethod
    def record_array(cls) -> ParsingExpressionLike:
        return "{", ZeroOrMore(cls.record_primary, sep=","), "}"


if TYPE_CHECKING:
    AnyPrimary = Union[List[Any], List[List[Any]]]
    BooleanPrimary = Union[List[bool], List[List[bool]]]
    StringPrimary = Union[List[str], List[List[str]]]
    TuplePrimary = Union[Tuple[Any, ...], List[List[Tuple[Any, ...]]]]

    class Children(Protocol, Iterable[Any]):
        DOT: List[str]
        IDENT: List[str]
        real_primary: StringPrimary
        integer_primary: StringPrimary
        boolean_primary: BooleanPrimary
        string_primary: StringPrimary
        variablename: List[str]
        variablename_primary: StringPrimary
        typename_primary: StringPrimary
        component_primary: TuplePrimary
        record_primary: AnyPrimary
        record_element: List[tuple[str, Any]]
        record_expression: List[Any]
        subscript: List[str]


class Visitor(PTNodeVisitor):
    def visit_primary_list(
        self, _: Never, children: Any
    ) -> None | Any | tuple[Any, ...]:
        if len(children) == 0:
            return None
        elif len(children) == 1:
            return children[0]
        else:
            return tuple(children)

    def visit_IDENT(self, node: NonTerminal, _: Never) -> str:
        return node.flat_str()

    def visit_STRING(self, node: Terminal, _: Never) -> str:
        return _unquote_modelica_string(node.flat_str())

    def visit_real(self, node: NonTerminal, _: Never) -> str:
        return node.flat_str()

    def visit_real_array(self, _: Never, children: Children) -> StringPrimary:
        return children.real_primary

    def visit_integer(self, node: NonTerminal, _: Never) -> str:
        return node.flat_str()

    def visit_integer_array(
        self, _: Never, children: Children
    ) -> StringPrimary:
        return children.integer_primary

    def visit_TRUE(self, *_: Never) -> Literal[True]:
        return True

    def visit_FALSE(self, *_: Never) -> Literal[False]:
        return False

    def visit_boolean_array(
        self, _: Never, children: Children
    ) -> BooleanPrimary:
        return children.boolean_primary

    def visit_string_array(
        self, _: Never, children: Children
    ) -> StringPrimary:
        return children.string_primary

    def visit_variablename(self, node: NonTerminal, _: Never) -> str:
        return node.flat_str()

    def visit_variablename_array(
        self, _: Never, children: Children
    ) -> StringPrimary:
        return children.variablename_primary

    def visit_typename(self, node: NonTerminal, _: Never) -> str:
        return node.flat_str()

    def visit_typename_array(
        self, _: Never, children: Children
    ) -> StringPrimary:
        return children.typename_primary

    def visit_subscript(self, node: NonTerminal, _: Never) -> str:
        return node.flat_str()

    def visit_subscript_list(self, _: Never, children: Children) -> List[str]:
        return children.subscript

    def visit_component(self, _: Never, children: Children) -> tuple[Any, ...]:
        return tuple(children)

    def visit_component_array(
        self, _: Never, children: Children
    ) -> TuplePrimary:
        return children.component_primary

    def visit_record_element(
        self, _: Never, children: Children
    ) -> tuple[str, Any]:
        (key,) = children.IDENT
        (value,) = children.record_expression
        return key, value

    def visit_record(self, _: Never, children: Children) -> dict[str, Any]:
        return dict(children.record_element)

    def visit_record_array(self, _: Never, children: Children) -> AnyPrimary:
        return children.record_primary


class TypeNameSplitVisitor(PTNodeVisitor):
    def visit_DOT(self, node: Terminal, _: Never) -> str:
        return node.flat_str()

    def visit_variablename(self, node: NonTerminal, _: Never) -> str:
        return node.flat_str()

    def visit_typename(self, _: Never, children: Children) -> tuple[str, ...]:
        return tuple(children.DOT + children.variablename)
