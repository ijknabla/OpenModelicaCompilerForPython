
__all__ = (
    "ComponentTuple",
    "is_valid_identifier",
    "parse_OMCValue",
    "parse_typeName",
    "parse_components",
)

import arpeggio  # type: ignore
import typing

from omc4py.classes import TypeName

from . import (
    syntax,
    visitor,
)

from .visitor import ComponentTuple


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


def is_valid_identifier(
    ident: str
) -> bool:
    try:
        IDENT_parser.parse(ident)
        return True
    except arpeggio.NoMatch:
        return False


def parse_typeName(
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


def parse_components(
    literal: str
) -> typing.List[ComponentTuple]:
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
