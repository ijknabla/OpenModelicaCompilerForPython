
__all__ = (
    "ComponentTuple",
    "is_valid_identifier",
    "parse_OMCExceptions",
    "parse_OMCValue",
    "parse_typeName",
    "parse_components",
)

import arpeggio  # type: ignore
import functools
import re
import typing

from ..classes import TypeName
from .. import exception

from . import (
    syntax,
    visitor,
)

from .visitor import ComponentTuple


def omc_parser_getter(
    fget: typing.Callable[[], arpeggio.Parser]
) -> typing.Callable[[], arpeggio.Parser]:
    @functools.lru_cache(1)
    @functools.wraps(fget)
    def wrapped():
        with syntax.omc_dialect_context:
            return fget()
    return wrapped


@omc_parser_getter
def get_IDENT_parser() -> arpeggio.Parser:
    return arpeggio.ParserPython(
        syntax.IDENT_withEOF,
    )


@omc_parser_getter
def get_type_specifier_parser() -> arpeggio.Parser:
    return arpeggio.ParserPython(
        syntax.type_specifier_withEOF,
    )


@omc_parser_getter
def get_omc_record_array_parser() -> arpeggio.Parser:
    return arpeggio.ParserPython(
        syntax.omc_component_array_withEOF,
    )


@omc_parser_getter
def get_omc_value_parser() -> arpeggio.Parser:
    return arpeggio.ParserPython(
        syntax.omc_value_withEOF,
    )


@functools.lru_cache(1)
def get_omc_exception_regex():
    return re.compile(
        (
            r"(\[(?P<info>[^]]*)\]\s+)?"
            r"(?P<level>\w+):\s+"
            r"(?P<message>((?!$).)*)$"
        ),
        re.MULTILINE,
    )


def is_valid_identifier(
    ident: str
) -> bool:
    try:
        get_IDENT_parser().parse(ident)
        return True
    except arpeggio.NoMatch:
        return False


def parse_typeName(
    type_specifier: str
) -> TypeName:
    try:
        return arpeggio.visit_parse_tree(
            get_type_specifier_parser().parse(
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
        get_omc_record_array_parser().parse(literal),
        visitor.ComponentArrayVisitor(source=literal),
    )


def parse_OMCValue(
    literal: str
):
    return arpeggio.visit_parse_tree(
        get_omc_value_parser().parse(literal),
        visitor.OMCValueVisitor(),
    )


def parse_OMCValue__v_1_13(
    literal: str
):
    return arpeggio.visit_parse_tree(
        get_omc_value_parser().parse(literal),
        visitor.OMCValueVisitor__v_1_13(),
    )


def parse_OMCExceptions(
    error_string: str,
) -> typing.Iterator[exception.OMCException]:
    for matched in get_omc_exception_regex().finditer(error_string):
        level = matched.group("level").lower()
        message = matched.group("message")

        if level == "notification":
            yield exception.OMCNotification(message)
        elif level == "warning":
            yield exception.OMCWarning(message)
        elif level == "error":
            yield exception.OMCError(message)
        else:  # Not-implemented now, but valid level (for future)
            yield exception.OMCError(message)
