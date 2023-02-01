__all__ = ("OMCDialectSyntax",)

from arpeggio import EOF, Optional, RegExMatch, ZeroOrMore
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

    @classmethod
    @returns_parsing_expression
    def sign(cls) -> ParsingExpressionLike:
        return ["+", "-"]

    @classmethod
    @returns_parsing_expression
    def number(cls) -> ParsingExpressionLike:
        return (Optional(cls.sign), cls.UNSIGNED_NUMBER)

    @classmethod
    @returns_parsing_expression
    def boolean(cls) -> ParsingExpressionLike:
        return [cls.TRUE, cls.FALSE]

    @classmethod
    @returns_parsing_expression
    def omc_array(cls) -> ParsingExpressionLike:
        return (
            "{",
            cls.omc_value_list,
            "}",
        )

    @classmethod
    @returns_parsing_expression
    def omc_tuple(cls) -> ParsingExpressionLike:
        return (
            "(",
            cls.omc_value_list,
            ")",
        )

    @classmethod
    @returns_parsing_expression
    def omc_value_list(cls) -> ParsingExpressionLike:
        return ZeroOrMore(cls.omc_value, sep=",")

    @classmethod
    @returns_parsing_expression
    def omc_record_literal(cls) -> ParsingExpressionLike:
        return (
            cls.RECORD,
            cls.type_specifier,
            cls.omc_record_element_list,
            cls.END,
            cls.type_specifier,
            ";",
        )

    @classmethod
    @returns_parsing_expression
    def omc_record_element_list(cls) -> ParsingExpressionLike:
        return ZeroOrMore(cls.omc_record_element, sep=",")

    @classmethod
    @returns_parsing_expression
    def omc_record_element(cls) -> ParsingExpressionLike:
        return cls.IDENT, "=", cls.omc_value

    @classmethod
    @returns_parsing_expression
    def omc_value(cls) -> ParsingExpressionLike:
        return [
            cls.type_specifier,
            cls.number,
            cls.boolean,
            cls.STRING,
            cls.omc_array,
            cls.omc_tuple,
            cls.omc_record_literal,
        ]

    @classmethod
    @returns_parsing_expression
    def subscript_list(cls) -> ParsingExpressionLike:
        return ZeroOrMore(cls.subscript, sep=",")

    @classmethod
    @returns_parsing_expression
    def omc_dimensions(cls) -> ParsingExpressionLike:
        return "{", cls.subscript_list, "}"

    @classmethod
    @returns_parsing_expression
    def omc_component(cls) -> ParsingExpressionLike:
        return (
            "{",
            (
                cls.type_specifier,
                ",",  # className
                cls.IDENT,
                ",",  # name
                cls.STRING,
                ",",  # comment
                cls.STRING,
                ",",  # protected
                cls.boolean,
                ",",  # isFinal
                cls.boolean,
                ",",  # isFlow
                cls.boolean,
                ",",  # isStream
                cls.boolean,
                ",",  # isReplaceable
                cls.STRING,
                ",",  # variability
                cls.STRING,
                ",",  # innerOuter
                cls.STRING,
                ",",  # inputOutput
                cls.omc_dimensions,  # dimensions
            ),
            "}",
        )

    @classmethod
    @returns_parsing_expression
    def omc_component_list(cls) -> ParsingExpressionLike:
        return ZeroOrMore(cls.omc_component, sep=",")

    @classmethod
    @returns_parsing_expression
    def omc_component_array(cls) -> ParsingExpressionLike:
        return "{", cls.omc_component_list, "}"

    @classmethod
    @returns_parsing_expression
    def IDENT_withEOF(cls) -> ParsingExpressionLike:
        return cls.IDENT, EOF

    @classmethod
    @returns_parsing_expression
    def type_specifier_withEOF(cls) -> ParsingExpressionLike:
        return cls.type_specifier, EOF

    @classmethod
    @returns_parsing_expression
    def omc_value_withEOF(cls) -> ParsingExpressionLike:
        return cls.omc_value, EOF

    @classmethod
    @returns_parsing_expression
    def omc_component_array_withEOF(cls) -> ParsingExpressionLike:
        return cls.omc_component_array, EOF
