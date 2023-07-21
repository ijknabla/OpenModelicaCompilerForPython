from __future__ import annotations

import sys
from collections.abc import Callable, Iterable, Mapping, Sequence
from functools import wraps
from itertools import chain
from typing import TYPE_CHECKING, Any, TypeVar, Union
from typing import cast as typing_cast

from typing_extensions import (
    Annotated,
    Literal,
    get_args,
    get_origin,
    get_type_hints,
)

from .modelica import enumeration, record
from .openmodelica import Component, TypeName, VariableName

if TYPE_CHECKING:
    import typing
    from builtins import _ClassInfo

    import typing_extensions
    from typing_extensions import Concatenate, ParamSpec, TypeGuard

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
