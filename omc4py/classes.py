
__all__ = (
    "Boolean",
    "Integer",
    "Real",
    "String",
    "TypeName",
    "VariableName",
)

import abc
import numpy  # type: ignore
import typing
import typing_extensions


# Type hints

Dimensions = typing.Tuple[typing.Optional[int], ...]

REQUIRED = typing_extensions.Literal["required"]
OPTIONAL = typing_extensions.Literal["optional"]
REQUIRED_or_OPTIONAL = typing.Union[REQUIRED, OPTIONAL]

InputArgument = typing.Tuple[
    "Component", str,
    typing.Any, REQUIRED_or_OPTIONAL
]
OutputArgument = typing.Tuple[
    "Component", str
]


# Primitive classes {Real, Integer, Boolean, String}

if typing.TYPE_CHECKING:
    Real: typing.Type[float]
    Integer: typing.Type[int]
    Boolean: typing.Type[bool]
    String: typing.Type[str]
else:
    Real = numpy.double
    Integer = numpy.intc
    Boolean = numpy.bool
    String = numpy.str


# $Code classes OpenModelica.$Code.{VariableName, TypeName}

class VariableName(
):
    __slots__ = "__str"

    __str: str

    def __new__(
        cls,
        obj,
    ):
        if isinstance(obj, VariableName):
            return obj

        obj_str = str(obj)
        if not parser.is_valid_identifier(obj_str):
            raise ValueError(
                f"Invalid modelica identifier, got {obj_str!r}"
            )

        return cls.__from_valid_identifier_no_check__(
            obj_str
        )

    @classmethod
    def __from_valid_identifier_no_check__(
        cls,
        identifier: str
    ) -> "VariableName":
        variableName = object.__new__(cls)
        variableName.__str = identifier
        return variableName

    def __eq__(
        self, other,
    ):
        if not isinstance(other, VariableName):
            return False
        else:
            return str(self) == str(other)

    def __hash__(
        self,
    ):
        return hash(str(self))

    def __str__(
        self,
    ) -> str:
        return self.__str

    def __repr__(
        self,
    ) -> str:
        return f"{type(self).__name__}({str(self)!r})"

    __to_omc_literal__ = __str__


class TypeName(
):
    __slots__ = (
        "__parts",
    )

    __parts: typing.Tuple[str, ...]

    def __new__(cls, part, *parts):
        if not parts:
            if isinstance(part, TypeName):
                return part

        return cls.__from_valid_parts_no_check__(
            cls.__checked_parts(
                (part, *parts)
            )
        )

    @classmethod
    def from_str(
        cls,
        s: str
    ) -> "TypeName":
        return parser.parse_typeName(s)

    @classmethod
    def __from_valid_parts_no_check__(
        cls,
        parts: typing.Iterable[typing.Union[str, VariableName]],
    ):
        typeName = object.__new__(TypeName)
        typeName.__parts = tuple(map(str, parts))
        return typeName

    @property
    def parts(
        self,
    ) -> typing.Tuple[str, ...]:
        return self.__parts

    @property
    def is_absolute(self) -> bool: return str(self.parts[0]) == "."

    @property
    def last_identifier(
        self,
    ) -> VariableName:
        return VariableName(self.parts[-1])

    @property
    def parents(
        self,
    ) -> typing.Iterator["TypeName"]:
        for end in reversed(range(1, len(self.parts))):
            yield self.__from_valid_parts_no_check__(
                self.parts[:end],
            )

    @property
    def parent(
        self,
    ) -> "TypeName":
        for parent in self.parents:
            return parent
        else:
            return self

    @classmethod
    def __checked_parts(
        cls,
        objs: typing.Iterable,
    ) -> typing.Iterator[typing.Union[str, VariableName]]:

        def not_checked_parts(
        ) -> typing.Iterator[typing.Union[str, VariableName]]:
            for obj in objs:
                if isinstance(obj, TypeName):
                    yield from obj.parts
                elif isinstance(obj, VariableName):
                    yield obj
                else:
                    yield from cls.from_str(str(obj)).parts

        for i, part in enumerate(
            not_checked_parts()
        ):
            if part == "." and not i == 0:
                raise ValueError(
                    f"parts[{i}] is invalid, got {part!r}"
                )
            yield part

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

    def __truediv__(
        self,
        other: typing.Union[str, VariableName, "TypeName"]
    ):
        return type(self)(self, other)


class Component(
):
    class_: typing.Type
    dimensions: Dimensions

    def __init__(
        self,
        class_: typing.Type,
        dimensions: typing.Optional[Dimensions] = None,
    ):
        self.class_ = class_
        if dimensions is None:
            self.dimensions = ()
        else:
            self.dimensions = dimensions

    def __getitem__(
        self, index,
    ) -> "Component":
        if not isinstance(index, tuple):
            return self[(index,)]

        def dimensions_generator(
        ) -> typing.Iterator[typing.Optional[int]]:
            for idim, dimension in enumerate(index):
                if isinstance(dimension, int):
                    if dimension < 0:
                        raise ValueError(
                            f'dimension #{idim}: int must be positive, '
                            f'got {dimension!r}'
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
                            f'got {start!s}:{stop!s}:{step!s}'
                        )
                    else:
                        yield None
                else:
                    raise TypeError(
                        f"dimension #{idim} must be int or slice, "
                        f"got {dimension!r}: {type(dimension)}"
                    )

        return Component(self.class_, tuple(dimensions_generator()))


class AbstractOMCInteractive(
    abc.ABC
):
    @abc.abstractmethod
    def close(self) -> None: ...

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
        inputArguments: typing.Sequence[InputArgument],
        outputArguments: typing.Sequence[OutputArgument],
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
    ) -> typing_extensions.Literal[False]:
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
    def __omc_check__(self) -> None: ...


from . import parser  # noqa: E402
