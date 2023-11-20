from __future__ import annotations

import enum
import inspect
from collections.abc import Callable, Coroutine, Generator
from functools import lru_cache, wraps
from typing import (
    TYPE_CHECKING,
    Any,
    ClassVar,
    TypeVar,
    Union,
    cast,
    get_args,
    get_origin,
    get_type_hints,
)

if TYPE_CHECKING:
    from typing_extensions import ParamSpec, Concatenate

from .algorithm import fmap
from .openmodelica import TypeName
from .protocol import (
    Asynchronous,
    HasInteractive,
    SupportsInteractiveProperty,
    Synchronous,
    T_Calling,
)
from .string import to_omc_literal


class package(HasInteractive[T_Calling]):
    __omc_class__: ClassVar[TypeName]


class record:
    __omc_class__: ClassVar[TypeName]


class enumeration(enum.Enum):
    __omc_class__: ClassVar[TypeName]


if TYPE_CHECKING:
    T = TypeVar("T")
    P = ParamSpec("P")

    SelfType = Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
    ReturnType = Union[T, Coroutine[None, None, T]]
    MethodType = Callable[
        Concatenate[SelfType, P],
        Union[T, Coroutine[None, None, T]],
    ]


def external(
    funcname: str, rename: dict[str, str] | None = None
) -> Callable[[T], T]:
    if rename is None:
        rename = {}

    def decorator(f: MethodType[P, T]) -> MethodType[P, T]:
        @wraps(f)
        def wrapped(
            self: SelfType, /, *args: P.args, **kwargs: P.kwargs
        ) -> ReturnType[T]:
            return _call(f, funcname, rename, self, *args, **kwargs)

        return wrapped

    return decorator  # type: ignore


def _call(
    f: MethodType[P, T],
    funcname: str,
    rename: dict[str, str],
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    *args: P.args,
    **kwargs: P.kwargs,
) -> ReturnType[T]:
    from . import parser

    signature = inspect.signature(f)
    type_hints = get_type_hints(f)

    def _iter_arguments() -> Generator[str, None, None]:
        for key, value in signature.bind(
            None, *args, **kwargs
        ).arguments.items():
            if value is None:
                continue
            name = rename.get(key, key)
            literal = to_omc_literal(parser.cast(type_hints[key], value))

            yield f"{name}={literal}"

    return fmap(
        lambda x: parser.parse(
            cast("type[T]", _extract_return_type(type_hints["return"])), x
        ),
        self.__omc_interactive__.evaluate(
            f"{funcname}({','.join(_iter_arguments())})"
        ),
    )


@lru_cache(None)
def _extract_return_type(type_hint: Any) -> Any:
    for arg in get_args(type_hint):
        if not isinstance(get_origin(arg), Coroutine):
            return arg

    raise NotImplementedError(type_hint)
