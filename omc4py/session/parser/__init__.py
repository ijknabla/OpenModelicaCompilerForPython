
__all__ = (
    "type_specifier_withEOF",
    "stored_definition_parser",
)

import arpeggio  # type: ignore

import modelica_language.parsers.syntax as std_syntax  # type: ignore

from ...parsers import omc_dialect_context


def type_specifier_withEOF():
    return std_syntax.type_specifier, arpeggio.EOF


def stored_definition_withEOF():
    return std_syntax.stored_definition, arpeggio.EOF


with omc_dialect_context:
    type_specifier_parser = arpeggio.ParserPython(
        type_specifier_withEOF
    )

    stored_definition_parser = arpeggio.ParserPython(
        stored_definition_withEOF,
        std_syntax.CPP_STYLE_COMMENT,
    )
