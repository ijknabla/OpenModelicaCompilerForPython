
import arpeggio  # type: ignore
import typing

from omc4py.parser import (
    stored_definition_parser,
    visitor,
)
from omc4py.types import (
    VariableName,
)


def parse_alias(
    code: str
) -> typing.Optional[visitor.AliasInfo]:
    return arpeggio.visit_parse_tree(
        stored_definition_parser.parse(code),
        visitor.AliasVisitor(),
    )


def parse_defaultValueInfoDict(
    interface: str
) -> typing.Dict[VariableName, typing.Optional[str]]:
    return dict(
        arpeggio.visit_parse_tree(
            stored_definition_parser.parse(interface),
            visitor.DefaultValueInfoVisitor(),
        )
    )


def parse_enumerator(
    code: str
) -> typing.Tuple[VariableName]:
    return arpeggio.visit_parse_tree(
        stored_definition_parser.parse(code),
        visitor.EnumeratorVisitor(),
    )
