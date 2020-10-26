
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
    enum.Enum,
    metaclass=OMCEnumerationMeta,
):
    __className__: typing.ClassVar[TypeName]

    def __str__(
        self,
    ) -> str:
        return f"{self.__className__}.{self.name}"

    __to_omc_literal__ = __str__
