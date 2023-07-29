from __future__ import annotations

import enum
import inspect
from collections.abc import Callable, Generator
from functools import partial, wraps
from typing import TYPE_CHECKING, Any, ClassVar, Generic, TypeVar

from typing_extensions import (
    Annotated,
    Literal,
    get_args,
    get_origin,
    get_type_hints,
)

from omc4py.protocol import SupportsAnyInteractive, SupportsInteractiveProperty

from .algorithm import bind_to_awaitable
from .openmodelica import TypeName
from .string import to_omc_literal

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
    elif isinstance(obj, classmethod):
        return _create_function(class_name, obj.__func__)  # type: ignore

    raise NotImplementedError(obj)


def _create_function(
    class_name: str, f: Callable[..., Any]
) -> Callable[..., Any]:
    from .parser import parse

    @wraps(f)
    def _wrapped(_: Any, *args: Any, **kwargs: Any) -> Any:
        self = _
        if not isinstance(self, SupportsInteractiveProperty):
            raise ValueError(f"{self} is not SupportsInteractiveProperty")

        return_type = get_type_hints(f)["return"]
        literal = self.__omc_interactive__.evaluate(
            f"{class_name}({_get_argument(f, *args, **kwargs)})"
        )
        bound_parse = bind_to_awaitable(partial(parse, return_type))
        return bound_parse(literal)

    _wrapped.__omc_class__ = TypeName(class_name)  # type: ignore

    return _wrapped


def _get_argument(f: Callable[..., Any], *args: Any, **kwargs: Any) -> str:
    from .parser import cast

    type_hints = get_type_hints(f)
    signature = inspect.signature(f)
    paraphrases = _get_paraphrases(signature)

    def _iter_arguments() -> Generator[str, None, None]:
        for key, value in signature.bind(
            None, *args, **kwargs
        ).arguments.items():
            if value is None:
                continue
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
