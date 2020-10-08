
__all__ = (
    "type_specifier_withEOF",
    "stored_definition_parser",
)

import arpeggio  # type: ignore

from . import syntax, visitor


with syntax.omc_dialect_context:
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


def parse_omc_value(
    literal: str
):
    return arpeggio.visit_parse_tree(
        omc_value_parser.parse(literal),
        visitor.OMCValueVisitor()
    )
