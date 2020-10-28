
__all__ = (
    "AliasVisitor",
    "EnumeratorsVisitor",
    "VariableHasDefaultVisitor",
)

import typing

from omc4py.parser.visitor import (
    StringVisitor,
    TypeSpecifierVisitor,
    flatten_list,
    getitem_with_default,
)

from omc4py.types import (
    TypeName,
    VariableName,
)


class AliasInfo(
    typing.NamedTuple
):
    name: VariableName
    target: TypeName


class AliasVisitor(
    TypeSpecifierVisitor,
):
    def visit_short_class_specifier(
        self,
        node,
        children
    ) -> typing.Optional[typing.Tuple[VariableName, TypeName]]:
        variableName = VariableName(children.IDENT[0])
        type_specifier = getitem_with_default(
            children.type_specifier, 0,
            default=None
        )

        if type_specifier is None:
            return None
        else:
            return AliasInfo(
                name=variableName,
                target=type_specifier
            )

    def visit_stored_definition(
        self,
        node,
        children,
    ):
        aliases = [
            child
            for child in children
            if isinstance(child, AliasInfo)
        ]
        if aliases:
            return aliases[0]
        return None


class Enumerator(
    typing.NamedTuple,
):
    name: VariableName
    comment: str


class EnumeratorsVisitor(
    TypeSpecifierVisitor,
    StringVisitor,
):
    def visit_enumeration_literal(
        self,
        node,
        children,
    ) -> Enumerator:
        name = children.IDENT[0]
        comment = getitem_with_default(
            children.comment, 0,
            default=""
        )
        return Enumerator(
            name=name,
            comment=comment,
        )

    def visit_comment(
        self,
        node,
        children
    ):
        return children.string_comment[0]

    def visit_string_comment(
        self,
        node,
        children,
    ):
        return "".join(children.STRING)

    def visit__default__(
        self,
        node,
        children
    ):
        return [
            child
            for child in flatten_list(children)
            if isinstance(child, Enumerator)
        ]


class VariableHasDefault(
    typing.NamedTuple
):
    name: VariableName
    hasDefault: bool


class VariableHasDefaultVisitor(
    TypeSpecifierVisitor,
):
    def visit__default__(
        self,
        node,
        children,
    ) -> typing.List[VariableHasDefault]:
        return [
            child
            for child in flatten_list(children)
            if isinstance(child, VariableHasDefault)
        ]

    def visit_declaration(
        self,
        node,
        children
    ) -> VariableHasDefault:
        name = children.IDENT[0]
        hasDefault = bool(children.modification)
        return VariableHasDefault(
            name=name,
            hasDefault=hasDefault,
        )
