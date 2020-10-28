
__all__ = (
    "AliasVisitor",
    "EnumeratorVisitor",
    "DefaultValueInfoVisitor",
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


class DefaultValueInfo(
    typing.NamedTuple
):
    name: VariableName
    hasDefault: bool


class DefaultValueInfoVisitor(
    TypeSpecifierVisitor,
):
    def visit__default__(
        self,
        node,
        children,
    ) -> typing.List[DefaultValueInfo]:
        return [
            child
            for child in flatten_list(children)
            if isinstance(child, DefaultValueInfo)
        ]

    def visit_declaration(
        self,
        node,
        children
    ) -> DefaultValueInfo:
        name = children.IDENT[0]
        hasDefault = bool(children.modification)
        return DefaultValueInfo(
            name=name,
            hasDefault=hasDefault,
        )


class EnumeratorInfo(
    typing.NamedTuple,
):
    name: VariableName
    comment: str


class EnumeratorVisitor(
    TypeSpecifierVisitor,
    StringVisitor,
):
    def visit_enumeration_literal(
        self,
        node,
        children,
    ) -> EnumeratorInfo:
        name = children.IDENT[0]
        comment = getitem_with_default(
            children.comment, 0,
            default=""
        )
        return EnumeratorInfo(
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
            if isinstance(child, EnumeratorInfo)
        ]


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
