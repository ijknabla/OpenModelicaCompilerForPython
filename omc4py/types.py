
__all__ = (
    "Boolean",
    "Component",
    "Integer",
    "OMCEnumeration",
    "Real",
    "String",
    "TypeName",
    "VariableName",
)


import enum
import numpy  # type: ignore
import typing


Real: typing.Type = numpy.double
Integer: typing.Type = numpy.intc
Boolean: typing.Type = numpy.bool
String: typing.Type = numpy.str


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

    def __new__(cls, *parts):
        if len(parts) == 1:
            part, = parts
            if isinstance(part, TypeName):
                return part

        return cls.__from_valid_parts_no_check__(
            cls.__checked_parts(
                parts
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
        typeName._TypeName__parts = tuple(map(str, parts))
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


class OMCEnumerationMeta(
    enum.EnumMeta,
):
    __className__: TypeName

    def __call__(
        cls,
        value,
    ):
        if isinstance(value, VariableName):
            return cls[str(value)] \
                # pylint: disable=unsubscriptable-object
        if isinstance(value, TypeName):
            if not value.parent == cls.__className__:
                raise KeyError(
                    "TypeName must be in {className}.{{{enumerator_list}}}"
                    ", got {value}".format(
                        className=cls.__className__,
                        enumerator_list=", ".join(cls.__members__),
                        value=value,
                    )
                )
            return cls(value.last_identifier) \
                # pylint: disable=no-value-for-parameter
        elif isinstance(value, str):
            try:
                return cls(VariableName(value)) \
                    # pylint: disable=no-value-for-parameter
            except ValueError:
                pass
            return cls(TypeName(value)) \
                # pylint: disable=no-value-for-parameter
        else:
            return super().__call__(value)


class OMCEnumeration(
    Integer,  # type: ignore
    enum.Enum,
    metaclass=OMCEnumerationMeta,
):
    __className__: typing.ClassVar[TypeName]

    def __str__(
        self,
    ) -> str:
        return f"{self.__className__}.{self.name}"

    __to_omc_literal__ = __str__


class Component(
    typing.NamedTuple,
):
    className: TypeName
    name: VariableName
    comment: str
    protected: str
    isFinal: bool
    isFlow: bool
    isStream: bool
    isReplaceable: bool
    variability: str
    innerOuter: str
    inputOutput: str
    dimensions: typing.Tuple[str, ...]


from . import parser  # noqa: E402
