from __future__ import annotations

import enum
import sys
from collections.abc import Callable, Mapping, Sequence
from functools import lru_cache, wraps
from itertools import chain, islice
from typing import TYPE_CHECKING, Any, Iterable, TypeVar, Union
from typing import cast as typing_cast

from arpeggio import (
    EOF,
    NoMatch,
    NonTerminal,
    OneOrMore,
    Optional,
    ParserPython,
    PTNodeVisitor,
    RegExMatch,
    Terminal,
    ZeroOrMore,
    visit_parse_tree,
)
from modelicalang import (
    ParsingExpressionLike,
    returns_parsing_expression,
    v3_4,
)
from typing_extensions import (
    Annotated,
    Literal,
    Protocol,
    get_args,
    get_origin,
    get_type_hints,
)

from .exception import OMCRuntimeError
from .modelica import enumeration, record
from .openmodelica import Component, TypeName, VariableName
from .string import unquote_modelica_string

if TYPE_CHECKING:
    import typing
    from builtins import _ClassInfo

    import typing_extensions
    from typing_extensions import Concatenate, Never, ParamSpec, TypeGuard

    _SpecialForm = typing._SpecialForm | typing_extensions._SpecialForm


_T = TypeVar("_T")
_T_return = TypeVar("_T_return")

if TYPE_CHECKING:
    _P = ParamSpec("_P")
else:
    _P = ...

_Scalar = Union[
    float,
    int,
    bool,
    str,
    VariableName,
    TypeName,
    Component,
    enumeration,
    record,
]


def is_variablename(variablename: str) -> bool:
    parser = _get_variablename_parser()
    try:
        parser.parse(variablename)
        return True
    except NoMatch:
        return False


def split_typename_parts(typename: str) -> tuple[str, ...]:
    return visit_parse_tree(  # type: ignore
        _get_typename_parser().parse(typename),
        TypeNameSplitVisitor(),
    )


def parse(typ: type[_T], literal: str) -> _T:
    parser = _get_parser(
        *map(_Token.from_value_type, _get_types(typ, keep_component=True))
    )
    try:
        parse_tree = parser.parse(literal)
    except NoMatch:
        raise OMCRuntimeError(literal) from None
    return cast(typ, visit_parse_tree(parse_tree, Visitor()))


def cast(typ: type[_T], val: Any) -> _T:
    cast_type = _get_cast_type(typ)
    if _issubclass(cast_type, tuple):
        return _cast_tuple(val, cast_type, typ)  # type: ignore
    elif _is_enumeration_type(cast_type):
        return _cast_enumeration(val, cast_type, typ)
    elif _is_record_type(cast_type):
        return _cast_record(val, cast_type, typ)
    else:
        return _cast_value(val, cast_type, typ)


class _Token(enum.Enum):
    real = enum.auto()
    integer = enum.auto()
    boolean = enum.auto()
    string = enum.auto()
    variablename = enum.auto()
    typename = enum.auto()
    component = enum.auto()
    record = enum.auto()

    @property
    def primary(self) -> ParsingExpressionLike:
        return getattr(Syntax, f"{self.name}_primary")  # type: ignore

    @classmethod
    def from_value_type(
        cls, value_type: type[_Scalar] | type[Component]
    ) -> _Token:
        if issubclass(value_type, float):
            return cls.real
        elif not issubclass(value_type, bool) and issubclass(value_type, int):
            return cls.integer
        elif issubclass(value_type, bool):
            return cls.boolean
        elif issubclass(value_type, str):
            return cls.string
        elif issubclass(value_type, VariableName):
            return cls.variablename
        elif issubclass(value_type, (TypeName, enumeration)):
            return cls.typename
        elif issubclass(value_type, Component):
            return cls.component
        elif issubclass(value_type, record):
            return cls.record

        raise NotImplementedError(value_type)


@lru_cache(1)
def _get_variablename_parser() -> ParserPython:
    @returns_parsing_expression
    def root() -> ParsingExpressionLike:
        return Syntax.variablename, EOF

    with Syntax:
        return ParserPython(root)


@lru_cache(1)
def _get_typename_parser() -> ParserPython:
    @returns_parsing_expression
    def root() -> ParsingExpressionLike:
        return Syntax.typename, EOF

    with Syntax:
        return ParserPython(root)


@lru_cache(None)
def _get_parser(*tokens: _Token) -> ParserPython:
    @returns_parsing_expression
    def root() -> ParsingExpressionLike:
        if len(tokens) < 2:
            L = R = []
        else:
            L, R = ["("], [")"]

        return (*L, primary_list, *R, EOF)

    @returns_parsing_expression
    def primary_list() -> ParsingExpressionLike:
        primaries = (token.primary for token in tokens)
        return (
            *islice(primaries, 1),
            *chain.from_iterable([",", primary] for primary in primaries),
        )

    with Syntax:
        return ParserPython(root)


def _vectorize(
    f: Callable[Concatenate[_T, _P], _T_return]
) -> Callable[Concatenate[_T, _P], _T_return]:
    @wraps(f)
    def wrapped(_: _T, *args: _P.args, **kwargs: _P.kwargs) -> Any:
        val = _
        if isinstance(val, Sequence) and not isinstance(
            val, (str, bytes, tuple)
        ):
            return [wrapped(i, *args, **kwargs) for i in val]
        else:
            return f(val, *args, **kwargs)  # type: ignore

    return wrapped  # type: ignore


@_vectorize
def _cast_tuple(val: Any, typ: type[tuple[Any, ...]], hint: type[_T]) -> _T:
    def items() -> Iterable[Any]:
        for item, item_typ in zip(val, _get_types(typ, keep_component=False)):
            yield cast(item_typ, item)

    return typing_cast(_T, typ(*items()))


@_vectorize
def _cast_enumeration(val: Any, typ: type[enumeration], hint: type[_T]) -> _T:
    if isinstance(val, typ):
        return typing_cast(_T, val)
    elif isinstance(val, int):
        return typing_cast(_T, typ(val))
    elif isinstance(val, str):
        typename = TypeName(val).as_absolute()
        if typename.parent == typ.__omc_class__:
            name = f"{typename.last_identifier}"
        else:
            name = val
        return typing_cast(_T, typ[name])

    raise TypeError(val)


@_vectorize
def _cast_record(val: Any, typ: type[record], hint: type[_T]) -> _T:
    if isinstance(val, typ):
        return typing_cast(_T, val)
    elif isinstance(val, Mapping):
        type_hints = get_type_hints(typ)

        # Patch for bug at `.OpenModelica.Scripting.getMessagesStringInternal`
        if typ.__omc_class__ == TypeName(".OpenModelica.Scripting.SourceInfo"):
            if "fileName" in type_hints and "filename" in val:
                val = {
                    k if k != "filename" else "fileName": v
                    for k, v in val.items()
                }

        return typing_cast(
            _T, typ(**{k: cast(type_hints[k], v) for k, v in val.items()})
        )

    raise TypeError(val)


@_vectorize
def _cast_value(val: Any, typ: Any, hint: type[_T]) -> _T:
    if not isinstance(val, typ):
        val = typ(val)

    return typing_cast(_T, val)


def _get_types(typ: Any, *, keep_component: bool) -> tuple[type[_Scalar], ...]:
    if _is_none(typ):
        return ()
    elif _issubclass(typ, Component) and keep_component:
        return (typ,)
    elif _issubclass(typ, tuple):
        return tuple(map(_get_type, get_type_hints(typ).values()))
    else:
        return (_get_type(typ),)


def _get_type(typ: Any) -> type[_Scalar]:
    if _isorigin(typ, Annotated):
        arg, *_ = get_args(typ)
        return _get_type(arg)
    elif _issubclass(get_origin(typ), Sequence):
        (arg,) = get_args(typ)
        return _get_type(arg)
    elif _is_union(typ):
        return _select_type(map(_get_type, get_args(typ)))
    elif get_origin(typ) is Literal:
        return _select_type(map(type, get_args(typ)))
    elif _issubclass(typ, get_args(_Scalar)):
        return typ  # type: ignore
    else:
        raise NotImplementedError(typ)


def _get_cast_type(typ: Any) -> type[None | _Scalar | tuple[Any, ...]]:
    if _is_none(typ):
        return type(None)
    elif _isorigin(typ, Annotated):
        arg, *_ = get_args(typ)
        return _get_cast_type(arg)
    elif _issubclass(typ, tuple):
        return typ  # type: ignore
    elif _issubclass(get_origin(typ), Sequence):
        (arg,) = get_args(typ)
        return _get_cast_type(arg)
    elif _is_union(typ):
        return _select_type(map(_get_cast_type, get_args(typ)))
    elif _isorigin(typ, Literal):
        return _select_type(map(_get_cast_type, map(type, get_args(typ))))
    elif _issubclass(typ, get_args(_Scalar)):
        return typ  # type: ignore
    else:
        raise NotImplementedError(typ)


def _is_union(typ: Any) -> bool:
    if _isorigin(typ, Union):
        return True
    if sys.version_info >= (3, 10):
        from types import UnionType

        if isinstance(typ, UnionType):
            return True

    return False


def _select_type(typs: Iterable[type[Any]]) -> type[Any]:
    return max(typs, key=_priority)


def _priority(typ: type[_Scalar]) -> int:
    for i, base in reversed(
        list(enumerate([int, str, VariableName, TypeName, enumeration]))
    ):
        if _issubclass(typ, base):
            return i

    raise NotImplementedError(typ)


def _is_none(
    typ: Any,
) -> TypeGuard[type[None] | None]:
    return typ is None or _issubclass(typ, type(None))


def _is_enumeration_type(
    typ: Any,
) -> TypeGuard[type[enumeration]]:
    return isinstance(typ, type) and issubclass(typ, enumeration)


def _is_record_type(
    typ: Any,
) -> TypeGuard[type[record]]:
    return isinstance(typ, type) and issubclass(typ, record)


def _issubclass(__cls: Any, __class_or_tuple: _ClassInfo) -> bool:
    return isinstance(__cls, type) and issubclass(__cls, __class_or_tuple)


def _isorigin(__cls: Any, __special_form: _SpecialForm) -> bool:
    return get_origin(__cls) is __special_form


class Syntax(v3_4.Syntax):
    # Dialects

    @classmethod
    @returns_parsing_expression
    def IDENT(cls) -> ParsingExpressionLike:
        return [super().IDENT(), RegExMatch(r"\$\w*")]

    # Primitives

    @classmethod
    @returns_parsing_expression
    def real(cls) -> ParsingExpressionLike:
        return Optional(cls.SIGN), cls.UNSIGNED_NUMBER

    @classmethod
    @returns_parsing_expression
    def integer(cls) -> ParsingExpressionLike:
        return Optional(cls.SIGN), cls.UNSIGNED_INTEGER

    @classmethod
    @returns_parsing_expression
    def boolean(cls) -> ParsingExpressionLike:
        return [cls.TRUE, cls.FALSE]

    @classmethod
    @returns_parsing_expression
    def variablename(cls) -> ParsingExpressionLike:
        return [
            RegExMatch(
                "[A-Z_a-z][0-9A-Z_a-z]*|'([\\ !\\#-\\&\\(-\\[\\]-_a-\\~]|\\\\'|\\\\\"|\\\\\\?|\\\\\\\\|\\\\a|\\\\b|\\\\f|\\\\n|\\\\r|\\\\t|\\\\v)([\\ -\\&\\(-\\[\\]-_a-\\~]|\\\\'|\\\\\"|\\\\\\?|\\\\\\\\|\\\\a|\\\\b|\\\\f|\\\\n|\\\\r|\\\\t|\\\\v)*'"  # noqa: E501
            ),
            RegExMatch(r"\$\w*"),
        ]

    @classmethod
    @returns_parsing_expression
    def typename(cls) -> ParsingExpressionLike:
        return Optional(cls.DOT), OneOrMore(cls.variablename, sep=".")

    @classmethod
    @returns_parsing_expression
    def component(cls) -> ParsingExpressionLike:
        return (
            "{",
            (
                *(cls.typename, ","),  # className
                *(cls.IDENT, ","),  # name
                *(cls.STRING, ","),  # comment
                *(cls.STRING, ","),  # protected
                *(cls.boolean, ","),  # isFinal
                *(cls.boolean, ","),  # isFlow
                *(cls.boolean, ","),  # isStream
                *(cls.boolean, ","),  # isReplaceable
                *(cls.STRING, ","),  # variability
                *(cls.STRING, ","),  # innerOuter
                *(cls.STRING, ","),  # inputOutput
                cls.subscript_list,  # dimensions
            ),
            "}",
        )

    @classmethod
    @returns_parsing_expression
    def subscript_list(cls) -> ParsingExpressionLike:
        return "{", ZeroOrMore(cls.subscript, sep=","), "}"

    @classmethod
    @returns_parsing_expression
    def record(cls) -> ParsingExpressionLike:
        return (
            cls.RECORD,
            cls.type_specifier,
            ZeroOrMore(cls.record_element, sep=","),
            cls.END,
            cls.type_specifier,
            ";",
        )

    @classmethod
    @returns_parsing_expression
    def record_element(cls) -> ParsingExpressionLike:
        return cls.IDENT, "=", cls.record_expression

    @classmethod
    @returns_parsing_expression
    def record_expression(cls) -> ParsingExpressionLike:
        return [
            cls.record_primary,
            cls.real_primary,
            cls.boolean_primary,
            cls.string_primary,
            cls.typename_primary,
        ]

    # Additional rules

    @classmethod
    @returns_parsing_expression
    def DOT(cls) -> ParsingExpressionLike:
        return "."

    @classmethod
    @returns_parsing_expression
    def SIGN(cls) -> ParsingExpressionLike:
        return RegExMatch(r"[+-]")

    # Primary & Array

    @classmethod
    @returns_parsing_expression
    def real_primary(cls) -> ParsingExpressionLike:
        return [cls.real, cls.real_array]

    @classmethod
    @returns_parsing_expression
    def real_array(cls) -> ParsingExpressionLike:
        return "{", ZeroOrMore(cls.real_primary, sep=","), "}"

    @classmethod
    @returns_parsing_expression
    def integer_primary(cls) -> ParsingExpressionLike:
        return [cls.integer, cls.integer_array]

    @classmethod
    @returns_parsing_expression
    def integer_array(cls) -> ParsingExpressionLike:
        return "{", ZeroOrMore(cls.integer_primary, sep=","), "}"

    @classmethod
    @returns_parsing_expression
    def boolean_primary(cls) -> ParsingExpressionLike:
        return [cls.boolean, cls.boolean_array]

    @classmethod
    @returns_parsing_expression
    def boolean_array(cls) -> ParsingExpressionLike:
        return "{", ZeroOrMore(cls.boolean_primary, sep=","), "}"

    @classmethod
    @returns_parsing_expression
    def string_primary(cls) -> ParsingExpressionLike:
        return [cls.STRING, cls.string_array]

    @classmethod
    @returns_parsing_expression
    def string_array(cls) -> ParsingExpressionLike:
        return "{", ZeroOrMore(cls.string_primary, sep=","), "}"

    @classmethod
    @returns_parsing_expression
    def variablename_primary(cls) -> ParsingExpressionLike:
        return [cls.variablename, cls.variablename_array]

    @classmethod
    @returns_parsing_expression
    def variablename_array(cls) -> ParsingExpressionLike:
        return "{", ZeroOrMore(cls.variablename_primary, sep=","), "}"

    @classmethod
    @returns_parsing_expression
    def typename_primary(cls) -> ParsingExpressionLike:
        return [cls.typename, cls.typename_array]

    @classmethod
    @returns_parsing_expression
    def typename_array(cls) -> ParsingExpressionLike:
        return "{", ZeroOrMore(cls.typename_primary, sep=","), "}"

    @classmethod
    @returns_parsing_expression
    def component_primary(cls) -> ParsingExpressionLike:
        return [cls.component, cls.component_array]

    @classmethod
    @returns_parsing_expression
    def component_array(cls) -> ParsingExpressionLike:
        return "{", ZeroOrMore(cls.component_primary, sep=","), "}"

    @classmethod
    @returns_parsing_expression
    def record_primary(cls) -> ParsingExpressionLike:
        return [cls.record, cls.record_array]

    @classmethod
    @returns_parsing_expression
    def record_array(cls) -> ParsingExpressionLike:
        return "{", ZeroOrMore(cls.record_primary, sep=","), "}"


if TYPE_CHECKING:
    AnyPrimary = list[Any] | list[list[Any]]
    BooleanPrimary = list[bool] | list[list[bool]]
    StringPrimary = list[str] | list[list[str]]
    TuplePrimary = list[tuple[Any, ...]] | list[list[tuple[Any, ...]]]
else:
    AnyPrimary = ...
    BooleanPrimary = ...
    StringPrimary = ...
    TuplePrimary = ...


class Children(Protocol, Iterable[Any]):
    DOT: list[str]
    IDENT: list[str]
    real_primary: StringPrimary
    integer_primary: StringPrimary
    boolean_primary: BooleanPrimary
    string_primary: StringPrimary
    variablename: list[str]
    variablename_primary: StringPrimary
    typename_primary: StringPrimary
    component_primary: TuplePrimary
    record_primary: AnyPrimary
    record_element: list[tuple[str, Any]]
    record_expression: list[Any]
    subscript: list[str]


class Visitor(PTNodeVisitor):
    def visit_primary_list(
        self, _: Never, children: Any
    ) -> None | Any | tuple[Any, ...]:
        if len(children) == 0:
            return None
        elif len(children) == 1:
            return children[0]
        else:
            return tuple(children)

    def visit_IDENT(self, node: NonTerminal, _: Never) -> str:
        return node.flat_str()

    def visit_STRING(self, node: Terminal, _: Never) -> str:
        return unquote_modelica_string(node.flat_str())

    def visit_real(self, node: NonTerminal, _: Never) -> str:
        return node.flat_str()

    def visit_real_array(self, _: Never, children: Children) -> StringPrimary:
        return children.real_primary

    def visit_integer(self, node: NonTerminal, _: Never) -> str:
        return node.flat_str()

    def visit_integer_array(
        self, _: Never, children: Children
    ) -> StringPrimary:
        return children.integer_primary

    def visit_TRUE(self, *_: Never) -> Literal[True]:
        return True

    def visit_FALSE(self, *_: Never) -> Literal[False]:
        return False

    def visit_boolean_array(
        self, _: Never, children: Children
    ) -> BooleanPrimary:
        return children.boolean_primary

    def visit_string_array(
        self, _: Never, children: Children
    ) -> StringPrimary:
        return children.string_primary

    def visit_variablename(self, node: NonTerminal, _: Never) -> str:
        return node.flat_str()

    def visit_variablename_array(
        self, _: Never, children: Children
    ) -> StringPrimary:
        return children.variablename_primary

    def visit_typename(self, node: NonTerminal, _: Never) -> str:
        return node.flat_str()

    def visit_typename_array(
        self, _: Never, children: Children
    ) -> StringPrimary:
        return children.typename_primary

    def visit_subscript(self, node: NonTerminal, _: Never) -> str:
        return node.flat_str()

    def visit_subscript_list(self, _: Never, children: Children) -> list[str]:
        return children.subscript

    def visit_component(self, _: Never, children: Children) -> tuple[Any, ...]:
        return tuple(children)

    def visit_component_array(
        self, _: Never, children: Children
    ) -> TuplePrimary:
        return children.component_primary

    def visit_record_element(
        self, _: Never, children: Children
    ) -> tuple[str, Any]:
        (key,) = children.IDENT
        (value,) = children.record_expression
        return key, value

    def visit_record(self, _: Never, children: Children) -> dict[str, Any]:
        return dict(children.record_element)

    def visit_record_array(self, _: Never, children: Children) -> AnyPrimary:
        return children.record_primary


class TypeNameSplitVisitor(PTNodeVisitor):
    def visit_DOT(self, node: Terminal, _: Never) -> str:
        return node.flat_str()

    def visit_variablename(self, node: NonTerminal, _: Never) -> str:
        return node.flat_str()

    def visit_typename(self, _: Never, children: Children) -> tuple[str, ...]:
        return tuple(children.DOT + children.variablename)
