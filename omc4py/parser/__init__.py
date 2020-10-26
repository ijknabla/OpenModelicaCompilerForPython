
__all__ = (
    "_TypeName_from_str",
    "valid_identifier",
)

import arpeggio  # type: ignore

from omc4py.types import TypeName

from . import (
    syntax,
    visitor,
)


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


def _TypeName_from_str(
    type_specifier: str
) -> TypeName:
    try:
        return arpeggio.visit_parse_tree(
            type_specifier_parser.parse(
                type_specifier,
            ),
            visitor.TypeSpecifierVisitor()
        )
    except arpeggio.NoMatch:
        raise ValueError(f"Invalid type_specifier, got {type_specifier!r}")


def parse_ComponentArray(
    literal: str
):
    return arpeggio.visit_parse_tree(
        omc_record_array_parser.parse(literal),
        visitor.ComponentArrayVisitor(source=literal),
    )


def parse_OMCValue(
    literal: str
):
    return arpeggio.visit_parse_tree(
        omc_value_parser.parse(literal),
        visitor.OMCValueVisitor()
    )
