from __future__ import annotations

__all__ = (
    # Primitive types
    "Real",
    "Integer",
    "String",
    "Boolean",
    # $Code types
    "VariableName",
    "TypeName",
    # compiler & session class
    "AbstractOMCInteractive",
    "AbstractOMCSession",
    # modelica class
    "ModelicaEnumeration",
    "ModelicaPackage",
    "ModelicaRecord",
    "ModelicaFunction",
    # for modelica class definition
    "Component",
    "alias",
    "element",
    "enum",
    "external",
    "modelica_name",
)

import abc
import enum
import functools
import itertools
from collections.abc import Callable, Iterable, Iterator, Sequence
from typing import (
    TYPE_CHECKING,
    Any,
    ClassVar,
    NamedTuple,
    Optional,
    TypeVar,
    Union,
    cast,
)

import numpy
from arpeggio import PTNodeVisitor, Terminal
from typing_extensions import Literal, Protocol, TypeAlias, runtime_checkable

from .string import to_omc_literal

# Type hints

KT = TypeVar("KT")

Dimensions: TypeAlias = "tuple[Optional[int], ...]"

REQUIRED = Literal["required"]
OPTIONAL = Literal["optional"]
REQUIRED_or_OPTIONAL = Union[REQUIRED, OPTIONAL]

VariableNameLike = Union[
    "TypeName",
    "VariableName",
    str,
]

TypeNameLike = Union[
    "ModelicaClassMeta",
    "ModelicaEnumeration",
    VariableNameLike,
]

EnumerationLike = Union[
    "ModelicaEnumerationMeta",
    "TypeName",
]


InputArgument: TypeAlias = "tuple[Component, str, Any, REQUIRED_or_OPTIONAL]"
OutputArgument: TypeAlias = "tuple[Component, str]"

if TYPE_CHECKING:
    Parser = Callable[[str], Any]


# Primitive classes {Real, Integer, Boolean, String}

if TYPE_CHECKING:
    Real = float
    Integer = int
    Boolean = bool
    String = str
else:
    Real = numpy.double
    Integer = numpy.intc
    Boolean = numpy.bool_
    String = numpy.str_


@runtime_checkable
class SupportsToOMCLiteral(Protocol):
    def __to_omc_literal__(self) -> str:
        ...


# $Code classes OpenModelica.$Code.{VariableName, TypeName}

T_bvn = TypeVar("T_bvn", bound="_BaseVariableName")


class _BaseVariableName:
    __slots__ = ("__identifier",)
    __identifier: str

    def __new__(cls: type[T_bvn], identifier: Union[str, T_bvn]) -> T_bvn:
        if not isinstance(identifier, str):
            return identifier
        else:
            self = super(_BaseVariableName, cls).__new__(cls)
            self.__identifier = identifier
            return self

    def __eq__(self, other: Any) -> bool:
        return (
            isinstance(other, _BaseVariableName)
            and self.__identifier == other.__identifier
        )

    def __hash__(self) -> int:
        return hash(self.__identifier)

    def __str__(self) -> str:
        return self.__identifier

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.__identifier!r})"

    __to_omc_literal__ = __str__


T_vn = TypeVar("T_vn", bound="VariableName")


class VariableName(_BaseVariableName):
    def __new__(cls: type[T_vn], obj: VariableNameLike) -> T_vn:
        identifier: Union[str, T_vn]

        if isinstance(obj, (str, cls)):
            identifier = obj
        elif isinstance(obj, TypeName):
            identifier = to_omc_literal(obj)
        else:
            raise TypeError(
                "obj must be TypeName, VariableName or str, "
                f"got {obj!r}: {type(obj)}"
            )

        if isinstance(identifier, str) and not parser.is_valid_identifier(
            identifier
        ):
            raise ValueError(
                f"Invalid modelica identifier, got {identifier!r}"
            )

        return _BaseVariableName.__new__(cls, identifier)


class VariableNameVisitor(
    PTNodeVisitor,
):
    def visit_IDENT(
        self,
        node: Terminal,
        _: object,
    ) -> VariableName:
        return _BaseVariableName.__new__(VariableName, node.value)


class TypeName:
    __slots__ = ("__parts",)

    __parts: tuple[str, ...]

    def __new__(cls, part, *parts):
        if not parts:
            if isinstance(part, TypeName):
                return part

        self = super().__new__(TypeName)
        self.__parts = tuple(cls.__split_parts((part, *parts)))

        return self

    @staticmethod
    def __split_parts(
        parts: Iterable[TypeNameLike],
    ) -> Iterator[str]:
        for i, part in enumerate(
            itertools.chain(*map(TypeName.__split_part, parts))
        ):
            if part == "." and not i == 0:
                raise ValueError(f"parts[{i}] is invalid, got {part!r}")
            yield part

    @staticmethod
    def __split_part(
        part: TypeNameLike,
    ) -> Iterator[str]:
        if isinstance(part, ModelicaClassMeta):
            yield from part.__modelica_name__.parts
        elif isinstance(part, ModelicaEnumeration):
            yield from part.__as_typeName__().parts
        elif isinstance(part, TypeName):
            yield from part.parts
        elif isinstance(part, VariableName):
            yield str(part)
        elif isinstance(part, str):
            if part == ".":
                yield part
            else:
                yield from parser.parse_typeName(part).parts
        else:
            raise TypeError(f"Unexpected part, got {part}: {type(part)}")

    @property
    def parts(
        self,
    ) -> tuple[str, ...]:
        return self.__parts

    @property
    def is_absolute(self) -> bool:
        return bool(self.parts) and self.parts[0] == "."

    def as_absolute(self):
        if self.is_absolute:
            return self
        else:
            return TypeName(".", self)

    @property
    def last_identifier(
        self,
    ) -> VariableName:
        return VariableName(self.parts[-1])

    @property
    def parents(
        self,
    ) -> Iterator["TypeName"]:
        for end in reversed(range(1, len(self.parts))):
            yield TypeName(
                *self.parts[:end],
            )

    @property
    def parent(
        self,
    ) -> "TypeName":
        for parent in self.parents:
            return parent
        else:
            return self

    def __hash__(self):
        return hash(self.parts)

    def __eq__(self, other):
        return self.parts == type(self)(other).parts

    def __repr__(
        self,
    ) -> str:
        return f"{type(self).__name__}({str(self)!r})"

    def __str__(
        self,
    ) -> str:
        if self.is_absolute:
            return self.parts[0] + ".".join(self.parts[1:])
        else:
            return ".".join(self.parts)

    __to_omc_literal__ = __str__

    def __truediv__(self, other: Union[str, VariableName, "TypeName"]):
        return type(self)(self, other)


def split_dict(
    dictionary: dict[KT, Any],
    condition: Callable[[Any], bool],
) -> tuple[dict[KT, Any], dict[KT, Any]]:
    yes, no = {}, {}
    for k, v in dictionary.items():
        if condition(v):
            yes[k] = v
        else:
            no[k] = v
    return yes, no


class AbstractOMCInteractive(abc.ABC):
    @abc.abstractmethod
    def close(self) -> None:
        ...

    @abc.abstractmethod
    def evaluate(
        self,
        expression: str,
    ) -> str:
        ...

    @abc.abstractmethod
    def call_function(
        self,
        funcName: str,
        inputArguments: Sequence[InputArgument],
        outputArguments: Sequence[OutputArgument],
        parser: Parser,
    ):
        ...

    def __enter__(
        self,
    ) -> "AbstractOMCInteractive":
        return self

    def __exit__(
        self,
        exc_type,
        exc_value,
        traceback,
    ) -> Literal[False]:
        self.close()
        return False


class AbstractOMCSession(
    abc.ABC,
):
    __omc: AbstractOMCInteractive

    def __init__(
        self,
        omc: AbstractOMCInteractive,
    ):
        self.__omc = omc

    @property
    def __omc__(self) -> AbstractOMCInteractive:
        return self.__omc

    @abc.abstractmethod
    def __check__(self) -> None:
        ...

    def __enter__(self) -> "AbstractOMCSession":
        return self

    def __close__(self):
        self.__omc__.close()

    def __exit__(
        self,
        exc_type,
        exc_value,
        traceback,
    ) -> Literal[False]:
        self.__close__()
        return False


# Meta classes for modelica-like class


class ModelicaClassMeta:
    __modelica_name__: TypeName


class ModelicaEnumerationMeta(
    ModelicaClassMeta,
    enum.EnumMeta,
):
    def __call__(
        cls,
        value,
    ):
        if isinstance(value, TypeName):
            valueClassName = value.parent
            expectedClassName = cls.__modelica_name__
            if valueClassName.as_absolute() != expectedClassName.as_absolute():
                raise KeyError(
                    f"value: TypeName must be {cls.__modelica_name__}.* "
                    f"got {value!s}"
                )
            return cls[str(value.last_identifier)]
        else:
            return super().__call__(value)


class ModelicaLongClassMeta(
    ModelicaClassMeta,
    type,
):
    # BoundModelicaLongClassMeta will be assigned
    # after BoundModelicaLongClassMeta is defined.
    __bound_class__: type["BoundModelicaLongClassMeta"]

    __bind_session: Any

    def __new__(
        mtcls,
        name,
        bases,
        namespace,
    ):
        cls = cast(
            ModelicaLongClassMeta,
            super().__new__(
                mtcls,
                name,
                bases,
                namespace,
            ),
        )

        def bind_session(
            session: AbstractOMCSession,
        ) -> "BoundModelicaLongClassMeta":
            bound_cls = cast(
                BoundModelicaLongClassMeta,
                type.__new__(
                    cls.__bound_class__,
                    name,
                    (BoundModelicaLongClass,),
                    namespace,
                ),
            )
            bound_cls.__modelica_name__ = cls.__modelica_name__
            bound_cls.__unbound_class__ = ModelicaLongClassReference(cls)
            bound_cls.__session__ = session
            return bound_cls

        cls.__bind_session = bind_session

        return cls

    if TYPE_CHECKING:

        @classmethod
        def __bind_session__(
            cls, session: AbstractOMCSession
        ) -> "BoundModelicaLongClassMeta":
            ...

    else:

        def __bind_session__(
            cls,
            session: AbstractOMCSession,
        ) -> "BoundModelicaLongClassMeta":
            return cls.__bind_session(session)

    def __get__(
        cls,
        obj,
        objType=None,
    ):
        # session: AbstractOMCSession
        # session.{className}
        # >>> {class bound to session}
        if isinstance(obj, AbstractOMCSession):
            return cls.__bind_session__(obj)

        # boundClass: BoundModelicaLongClassMeta
        # boundClass.{class}
        # >>> {class bound to boundClass.__session__}
        if (
            obj is None
            and objType is not None
            and isinstance(objType, BoundModelicaLongClassMeta)
        ):
            return cls.__bind_session__(objType.__session__)

        return cls

    def __set__(cls, obj, value):
        raise AttributeError(
            f"can't set attribute {cls.__name__!r} of {obj!r}"
        )


class ModelicaLongClassReference(NamedTuple):
    value: ModelicaLongClassMeta


class BoundModelicaLongClassMeta(
    ModelicaClassMeta,
    type,
):
    __unbound_class__: ModelicaLongClassReference
    __session__: AbstractOMCSession

    @property
    def __call__(cls):
        unbound_class = cls.__unbound_class__.value

        @functools.wraps(unbound_class.__call__)
        def wrapped(*args, **kwrds):
            return unbound_class(*args, **kwrds)

        return wrapped


ModelicaLongClassMeta.__bound_class__ = BoundModelicaLongClassMeta


class ModelicaPackageMeta(
    ModelicaLongClassMeta,
):
    ...


class ModelicaRecordMeta(
    ModelicaLongClassMeta,
):
    def __new__(
        mtcls,
        name,
        bases,
        namespace,
    ):
        element_definitions, actual_namespace = split_dict(
            namespace,
            lambda obj: isinstance(obj, element),
        )

        cls = super().__new__(
            mtcls,
            name,
            bases,
            actual_namespace,
        )

        elements: dict[str, Component]

        def newfunc(cls: type["ModelicaRecord"], obj) -> "ModelicaRecord":
            nonlocal elements
            elements = {
                name: definition.get_component(cls)
                for name, definition in element_definitions.items()
            }

            if isinstance(obj, cls):
                return obj

            self = super(ModelicaRecord, cls).__new__(cls)

            if isinstance(obj, ModelicaRecord):
                self.__dict = obj.__as_dict__()
            else:
                self.__dict = dict(obj)

            keys = self.__dict.keys()
            if elements.keys() - keys:
                raise ValueError(f"Missing keys {elements.keys() - keys}")
            elif keys - elements.keys():
                raise ValueError(f"Unexpected keys {keys - elements.keys()}")

            for key, value in self.__dict.items():
                component = cast(Component, elements[key])
                self.__dict[key] = component.cast(key, value)

            return self

        def itemsfunc(
            self: "ModelicaRecord",
        ) -> Iterator[tuple[str, Any]]:
            for key, value in self.__dict.items():
                yield key, value

        cls.__new__ = newfunc
        cls.__items__ = itemsfunc

        def get_property(
            key: str,
        ) -> property:
            def getter(
                self: ModelicaRecord,
            ) -> Any:
                return self.__dict[key]

            def setter(self: ModelicaRecord, value) -> None:
                raise AttributeError(f"Can't set attribute {key!r}")

            return property(getter, setter)

        for key in element_definitions.keys():
            setattr(cls, key, get_property(key))

        return cls


class ModelicaFunctionMeta(
    ModelicaLongClassMeta,
):
    def __new__(
        mtcls,
        name,
        bases,
        namespace,
    ):
        if not bases:
            return super().__new__(
                mtcls,
                name,
                (),
                namespace,
            )

        external_dict, actual_namespace = split_dict(
            namespace,
            lambda obj: isinstance(obj, external),
        )

        if not external_dict:
            raise TypeError(
                f"ModelicaFunction {name!r} " f"does not define @external"
            )
        elif 1 < len(external_dict):
            raise TypeError(
                f"ModelicaFunction {name!r} " f"duplicate @external definition"
            )
        external_definition: external
        (external_definition,) = external_dict.values()

        unbound_metaclass = type(
            f"Unbound_{name}Meta",
            (ModelicaFunctionMeta,),
            {"__call__": external_definition.unbound_implementation},
        )

        bound_metaclass = type(
            f"Bound_{name}Meta",
            (BoundModelicaLongClassMeta,),
            {"__call__": external_definition.bound_implementation},
        )

        cls = cast(
            ModelicaFunctionMeta,
            super().__new__(
                unbound_metaclass,
                name,
                bases,
                actual_namespace,
            ),
        )
        cls.__bound_class__ = bound_metaclass

        return cls


# declaration class for modelica-like class definition


class Component:
    class_: type
    dimensions: Dimensions

    def __init__(
        self,
        class_: type,
        dimensions: Optional[Dimensions] = None,
    ):
        self.class_ = class_
        if dimensions is None:
            self.dimensions = ()
        else:
            self.dimensions = dimensions

    def __getitem__(
        self,
        index,
    ) -> "Component":
        if not isinstance(index, tuple):
            return self[(index,)]

        def dimensions_generator() -> Iterator[Optional[int]]:
            for idim, dimension in enumerate(index):
                if isinstance(dimension, int):
                    if dimension < 0:
                        raise ValueError(
                            f"dimension #{idim}: int must be positive, "
                            f"got {dimension!r}"
                        )
                    else:
                        yield dimension
                elif isinstance(dimension, slice):
                    start = dimension.start
                    stop = dimension.stop
                    step = dimension.step
                    if not (start is None and stop is None and step is None):
                        raise ValueError(
                            f"dimension #{idim}: slice must be ':', "
                            f"got {start!s}:{stop!s}:{step!s}"
                        )
                    else:
                        yield None
                else:
                    raise TypeError(
                        f"dimension #{idim} must be int or slice, "
                        f"got {dimension!r}: {type(dimension)}"
                    )

        return Component(self.class_, tuple(dimensions_generator()))

    @property
    def ndim(self) -> int:
        return len(self.dimensions)

    @property
    def is_scalar(self) -> bool:
        return self.ndim == 0

    @property
    def is_array(self) -> bool:
        return not self.is_scalar

    @property
    def class_restrictions(
        self,
    ) -> tuple[type, ...]:
        if self.class_ is Real:
            return (Real, float)
        elif self.class_ is Integer:
            return (Integer, int)
        elif self.class_ is Boolean:
            return (Boolean, bool)
        elif self.class_ is String:
            return (String, str)
        elif self.class_ is TypeName:
            return (  # TypeNameLike
                ModelicaClassMeta,
                ModelicaEnumeration,
                TypeName,
                VariableName,
                str,
            )
        elif self.class_ is VariableName:
            return (  # VariableNameLike
                TypeName,
                VariableName,
                str,
            )
        elif issubclass(self.class_, ModelicaEnumeration):
            return (  # EnumerationLike
                self.class_,
                TypeName,
            )
        else:
            return ()

    @staticmethod
    def dimensions_to_str(
        dimensions: Dimensions,
    ) -> str:
        if not dimensions:
            return "<scalar>"
        else:
            return "[{}]".format(
                ",".join(str(d) if d is not None else ":" for d in dimensions)
            )

    def cast(
        self,
        name: str,
        value: Any,
        required: REQUIRED_or_OPTIONAL = "required",
    ) -> Any:
        if value is None:
            if required == "required":
                raise ValueError(f"Required value {name!r} is None")
            if required == "optional":
                return None
            else:
                raise ValueError(
                    f"'required' must be (required|optional) got {required!r}"
                )

        value_array = numpy.array(value, dtype=object)

        same_n_dimensions = self.ndim == value_array.ndim
        dimensions_are_correct = [
            True if expected is None else expected == actual
            for expected, actual in zip(self.dimensions, value_array.shape)
        ]

        if not (same_n_dimensions and all(dimensions_are_correct)):
            raise ValueError(
                f"Dimensions of {name!r} "
                f"must be {self.dimensions_to_str(self.dimensions)}, "
                f"got {self.dimensions_to_str(value_array.shape)}"
            )

        if self.class_restrictions:
            isinstance_vectorized = numpy.vectorize(
                lambda cls: isinstance(cls, self.class_restrictions),
                otypes=[numpy.dtype(bool)],
            )
            isinstance_mask = isinstance_vectorized(value_array)
            if not numpy.all(isinstance_mask):
                if self.is_scalar:
                    raise TypeError(
                        f"{name!r} "
                        f"must be instance of {self.class_restrictions}"
                    )
                else:
                    raise TypeError(
                        f"All items of {name!r} "
                        f"must be instances of {self.class_restrictions}"
                    )

        if self.is_scalar:
            return self.class_(value)
        else:
            class_vectorized = numpy.vectorize(
                self.class_, otypes=[numpy.dtype(self.class_)]
            )
            return class_vectorized(value_array)


# decorators for modelica-like class definition


def modelica_name(name: str):
    def decorator(obj: ModelicaClassMeta) -> ModelicaClassMeta:
        if not isinstance(obj, ModelicaClassMeta):
            raise TypeError(
                "@modelica_name can only decorate ModelicaClassMeta, "
                f"got {obj}: {type(obj)}"
            )
        obj.__modelica_name__ = TypeName(name)
        return obj

    return decorator


class alias(
    ModelicaClassMeta,
):
    def __init__(
        self,
        classmethod_like: Callable,
    ):
        self.__func__ = classmethod_like

    def __get__(self, obj, objType):
        modelica_class = self.__func__(objType)
        if hasattr(modelica_class, "__get__"):
            return modelica_class.__get__(obj, objType)
        else:
            return modelica_class


class element:
    def __init__(
        self,
        classmethod_like: Callable,
    ):
        self.__func__ = classmethod_like

    def get_component(
        self,
        cls: ModelicaRecordMeta,
    ):
        if not isinstance(cls, ModelicaRecordMeta):
            raise TypeError(
                "@element is only available in ModelicaRecord definition"
            )

        component = self.__func__(cls)
        if not isinstance(component, Component):
            raise TypeError(
                "@element must return Component, "
                f"got {component}: {type(component)}"
            )
        return component


class external:
    def __init__(
        self,
        classmethod_like: Callable,
    ):
        self.__func__ = classmethod_like

    @property
    def unbound_implementation(self):
        @functools.wraps(self.__func__)
        def implementation(
            cls: ModelicaFunctionMeta,
            session: AbstractOMCSession,
            *args,
            **kwrds,
        ):
            return self.__func__(cls, session, *args, **kwrds)

        return implementation

    @property
    def bound_implementation(
        self,
    ):
        @functools.wraps(functools.partial(self.__func__, None))
        def implementation(
            cls: BoundModelicaLongClassMeta,
            *args,
            **kwrds,
        ):
            return self.__func__(cls, cls.__session__, *args, **kwrds)

        return implementation


# base classes for modelica-like class


class ModelicaEnumeration(
    enum.Enum,
    metaclass=ModelicaEnumerationMeta,
):
    __modelica_name__: ClassVar[TypeName]

    def _generate_next_value_(name, start, count, last_values):
        return Integer(count + 1)

    def __as_typeName__(self) -> TypeName:
        return self.__modelica_name__ / self.name

    def __str__(self) -> str:
        return str(self.__as_typeName__())

    __to_omc_literal__ = __str__


class BoundModelicaLongClass(
    metaclass=BoundModelicaLongClassMeta,
):
    ...


class ModelicaPackage(
    metaclass=ModelicaPackageMeta,
):
    ...


class ModelicaRecord(
    metaclass=ModelicaRecordMeta,
):
    __modelica_name__: ClassVar[TypeName]

    __items__: Callable[
        ["ModelicaRecord"],
        Iterator[tuple[str, Any]],
    ]

    def __as_dict__(
        self,
    ) -> dict[str, Any]:
        return dict(self.__items__())

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.__as_dict__()})"

    def __str__(
        self,
    ) -> str:
        s_elements = ", ".join(
            f"{key} = {to_omc_literal(value)}"
            for key, value in self.__items__()
        )

        def words():
            yield f"{self.__modelica_name__}"
            if s_elements:
                yield s_elements
            yield "end"
            yield f"{self.__modelica_name__};"

        return " ".join(words())

    __to_omc_literal__ = __str__


class ModelicaFunction(
    metaclass=ModelicaFunctionMeta,
):
    ...


from . import parser  # noqa: E402
