from __future__ import annotations

import inspect
from collections.abc import Callable, Coroutine, Generator
from functools import lru_cache, partial, wraps
from typing import (
    TYPE_CHECKING,
    Any,
    ClassVar,
    TypeVar,
    Union,
    get_args,
    get_origin,
    get_type_hints,
)

if TYPE_CHECKING:
    from typing_extensions import ParamSpec, Concatenate

from .algorithm import bind_to_awaitable
from .openmodelica import TypeName
from .parser import cast, parse
from .protocol import (
    Asynchronous,
    HasInteractive,
    SupportsInteractiveProperty,
    Synchronous,
    T_Calling,
)
from .string import to_omc_literal

if TYPE_CHECKING:
    _T = TypeVar("_T")
    _P = ParamSpec("_P")

    SupportsAnyInteractiveProperty = (
        SupportsInteractiveProperty[Synchronous]
        | SupportsInteractiveProperty[Asynchronous]
    )


class package(HasInteractive[T_Calling]):
    __omc_class__: ClassVar[TypeName]


if TYPE_CHECKING:
    SelfType = Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
    ReturnType = Union[_T, Coroutine[None, None, _T]]
    MethodType = Callable[
        Concatenate[SelfType, _P],
        Union[_T, Coroutine[None, None, _T]],
    ]


def external(
    funcname: str, rename: dict[str, str] | None = None
) -> Callable[[_T], _T]:
    if rename is None:
        rename = {}

    def decorator(f: MethodType[_P, _T]) -> MethodType[_P, _T]:
        @wraps(f)
        def wrapped(
            self: SelfType,
            *args: _P.args,
            **kwargs: _P.kwargs,
        ) -> ReturnType[_T]:
            return _call(f, funcname, rename, self, *args, **kwargs)

        return wrapped  # type: ignore

    return decorator  # type: ignore


def _call(
    f: MethodType[_P, _T],
    funcname: str,
    rename: dict[str, str],
    self: SupportsAnyInteractiveProperty,
    *args: _P.args,
    **kwargs: _P.kwargs,
) -> ReturnType[_T]:
    signature = inspect.signature(f)
    type_hints = get_type_hints(f)

    def _iter_arguments() -> Generator[str, None, None]:
        for key, value in signature.bind(
            None, *args, **kwargs
        ).arguments.items():
            if value is None:
                continue
            name = rename.get(key, key)
            literal = to_omc_literal(cast(type_hints[key], value))

            yield f"{name}={literal}"

    bound_parse = bind_to_awaitable(
        partial(parse, _extract_return_type(type_hints["return"]))
    )
    return bound_parse(  # type: ignore
        self.__omc_interactive__.evaluate(  # type: ignore
            f"{funcname}({','.join(_iter_arguments())})"
        )
    )


@lru_cache(None)
def _extract_return_type(type_hint: Any) -> Any:
    for arg in get_args(type_hint):
        if not isinstance(get_origin(arg), Coroutine):
            return arg
