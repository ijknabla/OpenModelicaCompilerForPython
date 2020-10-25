
__all__ = (
    "valid_identifier",
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

    omc_record_array_parser = arpeggio.ParserPython(
        syntax.omc_component_array_withEOF,
    )

    omc_value_parser = arpeggio.ParserPython(
        syntax.omc_value_withEOF,
    )


def valid_identifier(
    ident: str
) -> bool:
    try:
        IDENT_parser.parse(ident)
        return True
    except arpeggio.NoMatch:
        return False
