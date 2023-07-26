from __future__ import annotations

import enum
import inspect
from collections.abc import Callable, Generator
from functools import partial, wraps
from typing import TYPE_CHECKING, Any, Awaitable, ClassVar, Generic, TypeVar

from typing_extensions import (
    Annotated,
    Literal,
    get_args,
    get_origin,
    get_type_hints,
)

from neo.protocol import SupportsAnyInteractive, SupportsInteractiveProperty
from omc4py.string import to_omc_literal

from .openmodelica import TypeName

_T = TypeVar("_T")


def external(class_name: str) -> Callable[[_T], _T]:
    return partial(_external, class_name=class_name)


class alias(Generic[_T]):
    ...


class enumeration(enum.Enum):
    __omc_class__: ClassVar[TypeName]


class PackageMeta(type):
    if not TYPE_CHECKING:

        def __get__(cls, obj, objtype=None):
            if isinstance(obj, SupportsInteractiveProperty):
                package = cls()
                package.__omc_interactive__ = obj.__omc_interactive__
                return package
            else:
                return cls


class package(metaclass=PackageMeta):
    __omc_class__: ClassVar[TypeName]
    __omc_interactive__: SupportsAnyInteractive


class record:
    __omc_class__: ClassVar[TypeName]


def _external(obj: _T, class_name: str) -> _T:
    if isinstance(obj, type) and issubclass(
        obj, (enumeration, package, record)
    ):
        obj.__omc_class__ = TypeName(class_name)
        return obj  # type: ignore
    elif isinstance(obj, staticmethod):
        return _create_function(class_name, obj.__func__)  # type: ignore

    raise NotImplementedError(obj)


def _create_function(
    class_name: str, f: Callable[..., Any]
) -> Callable[..., Any]:
    from .parser import parse

    @wraps(f)
    def _wrapped(self: Any, *args: Any, **kwargs: Any) -> Any:
        if not isinstance(self, SupportsInteractiveProperty):
            raise ValueError(f"{self} is not SupportsInteractiveProperty")

        return_type = get_type_hints(f)["return"]
        literal = self.__omc_interactive__.evaluate(
            f"{class_name}({_get_argument(f, *args, **kwargs)})"
        )
        if isinstance(literal, str):
            return parse(return_type, literal)
        else:

            async def _wrapped(literal: Awaitable[str]) -> Any:
                return parse(
                    return_type,
                    await literal,
                )

            return _wrapped(literal)

    _wrapped.__omc_class__ = TypeName(class_name)  # type: ignore

    return _wrapped


def _get_argument(f: Callable[..., Any], *args: Any, **kwargs: Any) -> str:
    from .parser import cast

    type_hints = get_type_hints(f)
    signature = inspect.signature(f)
    paraphrases = _get_paraphrases(signature)

    def _iter_arguments() -> Generator[str, None, None]:
        for key, value in signature.bind(*args, **kwargs).arguments.items():
            name = paraphrases[key]
            literal = to_omc_literal(cast(type_hints[key], value))

            yield f"{name}={literal}"

    return ",".join(_iter_arguments())


def _get_paraphrases(signature: inspect.Signature) -> dict[str, str]:
    def _find_value(key: str, annotation: Any) -> str:
        if get_origin(annotation) is Annotated:
            for alias_ in get_args(annotation)[1:]:
                if get_origin(alias_) is alias:
                    literal, *_ = get_args(alias)
                    if get_origin(literal) is Literal:
                        string, *_ = get_args(literal)
                        if isinstance(string, str):
                            return string
        return key

    return {
        key: _find_value(key, parameter.annotation)
        for key, parameter in signature.parameters.items()
    }
