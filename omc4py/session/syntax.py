
__all__ = (
    "omc_dialect_context",
    "std",
    "stored_definition_withEOF",
    "type_specifier_withEOF",
)


import arpeggio  # type: ignore

import modelica_language.parsers.syntax as std  # type: ignore

from ..parsers import omc_dialect_context


def change___name__(
    name: str
):
    def decorator(
        obj
    ):
        obj.__name__ = name
        return obj

    return decorator


@change___name__("file")
def stored_definition_withEOF():
    return std.stored_definition, arpeggio.EOF


@change___name__("file")
def type_specifier_withEOF():
    return std.type_specifier, arpeggio.EOF
