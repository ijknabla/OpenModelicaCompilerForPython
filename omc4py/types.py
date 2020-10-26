
import enum
import typing

from .primitive_types import (
    TypeName,
    VariableName,
)


class OMCEnumerationMeta(
    enum.EnumMeta,
):
    __className__: TypeName

    def __call__(
        cls,
        value,
    ):
        if isinstance(value, VariableName):
            return cls[str(value)]
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
            return cls(value.last_identifier)
        elif isinstance(value, str):
            try:
                return cls(VariableName(value))
            except ValueError:
                pass
            return cls(TypeName(value))
        else:
            return super().__call__(value)


class OMCEnumeration(
    enum.Enum,
    metaclass=OMCEnumerationMeta,
):
    __className__: typing.ClassVar[TypeName]

    def __str__(
        self,
    ) -> str:
        return f"{self.__className__}.{self.name}"

    __to_omc_literal__ = __str__
