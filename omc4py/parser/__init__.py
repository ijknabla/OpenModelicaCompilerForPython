
__all__ = (
    "omc_value_parser",
    "stored_definition_parser",
    "type_specifier_parser",
)

import arpeggio  # type: ignore

from omc4py.parser import syntax


with syntax.omc_dialect_context:
    IDENT_parser = arpeggio.ParserPython(
        syntax.IDENT_withEOF,
    )

    type_specifier_parser = arpeggio.ParserPython(
        syntax.type_specifier_withEOF,
    )

    stored_definition_parser = arpeggio.ParserPython(
        syntax.stored_definition_withEOF,
        syntax.std.CPP_STYLE_COMMENT,
    )

    omc_value_parser = arpeggio.ParserPython(
        syntax.omc_value_withEOF,
    )

    omc_record_array_parser = arpeggio.ParserPython(
        syntax.omc_component_array_withEOF,
    )
