
__all__ = (
    "omc_dialect_context",
    "std",
    "stored_definition_withEOF",
    "type_specifier_withEOF",
)


import arpeggio  # type: ignore
import typing

import modelica_language.parsers.syntax as std  # type: ignore


_MODELICA_STANDARD_IDENT = std.IDENT


def STANDARD_IDENT():
    return _MODELICA_STANDARD_IDENT


def IDENT():
    return [STANDARD_IDENT, arpeggio.RegExMatch(r"\$\w*")]


def sign():
    return ["+", "-"]


def number():
    return (
        arpeggio.Optional(sign),
        std.UNSIGNED_NUMBER
    )


def boolean():
    return [std.TRUE, std.FALSE]


def omc_array():
    return "{", omc_value_list, "}",


def omc_tuple():
    return "(", omc_value_list, ")",


def omc_value_list():
    return arpeggio.ZeroOrMore(omc_value, sep=",")


def omc_record_literal():
    return (
        std.RECORD, std.type_specifier,
        omc_record_element_list,
        std.END, std.type_specifier, ";"
    )


def omc_record_element_list():
    return arpeggio.ZeroOrMore(
        omc_record_element, sep=","
    )


def omc_record_element():
    return std.IDENT, "=", omc_value


def omc_value():
    return [
        std.type_specifier,
        number,
        boolean,
        std.STRING,
        omc_array,
        omc_tuple,
        omc_record_literal,
    ]


def subscript_list():
    return arpeggio.ZeroOrMore(std.subscript, sep=",")


def omc_dimensions():
    return "{", subscript_list, "}"


def omc_component():
    return (
        "{",
        (
            std.type_specifier, ",",  # className
            std.IDENT, ",",  # name
            std.STRING, ",",  # comment
            std.STRING, ",",  # protected
            boolean, ",",  # isFinal
            boolean, ",",  # isFlow
            boolean, ",",  # isStream
            boolean, ",",  # isReplaceable
            std.STRING, ",",  # variability
            std.STRING, ",",  # innerOuter
            std.STRING, ",",  # inputOutput
            omc_dimensions,  # dimensions
        ),
        "}",
    )


def omc_component_list():
    return arpeggio.ZeroOrMore(omc_component, sep=",")


def omc_component_array():
    return "{", omc_component_list, "}"


def IDENT_withEOF():
    return std.IDENT, arpeggio.EOF


def type_specifier_withEOF():
    return std.type_specifier, arpeggio.EOF


def omc_value_withEOF():
    return omc_value, arpeggio.EOF


def omc_component_array_withEOF():
    return omc_component_array, arpeggio.EOF


def stored_definition_withEOF():
    return std.stored_definition, arpeggio.EOF


class OMCDialectContext():
    __enabled: typing.ClassVar[bool] = False

    def __enter__(self):
        if OMCDialectContext.__enabled:
            raise ValueError("Duplicate OMCDialectContext")

        OMCDialectContext.__enabled = True
        std.IDENT = IDENT

    def __exit__(self, exc_type, exc_value, traceback):
        OMCDialectContext.__enabled = False
        std.IDENT = _MODELICA_STANDARD_IDENT

        return False


omc_dialect_context = OMCDialectContext()
