
import arpeggio  # type: ignore
import typing

from omc4py.parser import (
    stored_definition_parser,
    visitor,
)
from omc4py.types import (
    TypeName,
    VariableName,
)


def parse_alias(
    code: str
) -> typing.Optional[typing.Tuple[VariableName, TypeName]]:
    return arpeggio.visit_parse_tree(
        stored_definition_parser.parse(code),
        visitor.AliasVisitor(),
    )


def parse_defaultValueInfoDict(
    code: str
) -> typing.Dict[VariableName, bool]:
    return dict(
        arpeggio.visit_parse_tree(
            stored_definition_parser.parse(code),
            visitor.DefaultValueInfoVisitor(),
        )
    )


def parse_enumerators(
    code: str
) -> typing.List[typing.Tuple[VariableName, str]]:
    return arpeggio.visit_parse_tree(
        stored_definition_parser.parse(code),
        visitor.EnumeratorVisitor(),
    )
