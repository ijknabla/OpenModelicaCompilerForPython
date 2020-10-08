
__all__ = (
    "omc_dialect_context",
    "std",
    "stored_definition_withEOF",
    "type_specifier_withEOF",
)


import arpeggio  # type: ignore

import modelica_language.parsers.syntax as std  # type: ignore


def change___name__(
    name: str
):
    def decorator(
        obj
    ):
        obj.__name__ = name
        return obj

    return decorator


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


def omc_value_list():
    return arpeggio.ZeroOrMore(omc_value, sep=",")


def omc_tuple():
    return "(", omc_value_list, ")",


def omc_array():
    return "{", omc_value_list, "}",


def omc_value():
    return [
        boolean,
        std.STRING,
        number,
        std.type_specifier,
        omc_record_literal,
        omc_tuple,
        omc_array,
    ]


@change___name__("file")
def stored_definition_withEOF():
    return std.stored_definition, arpeggio.EOF


@change___name__("file")
def type_specifier_withEOF():
    return std.type_specifier, arpeggio.EOF


class OMCDialectContext():
    __enabled = False

    def __enter__(self):
        if self.__enabled:
            raise ValueError("Duplicate OMCDialectContext")

        self.__enabled = True
        std.IDENT = IDENT

    def __exit__(self, exc_type, exc_value, traceback):
        self.__enabled = False
        std.IDENT = _MODELICA_STANDARD_IDENT

        return False


omc_dialect_context = OMCDialectContext()
