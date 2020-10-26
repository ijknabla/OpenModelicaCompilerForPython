
import enum

from .primitive_types import (
    TypeName,
    VariableName,
)


class EnumerationMeta(
    enum.EnumMeta,
):
    __className__: TypeName

    def __getitem__(
        cls,
        key,
    ):
        if isinstance(key, VariableName):
            return super().__getitem__(str(key))
        elif isinstance(key, TypeName):
            if not key.parent == cls.__className__:
                raise KeyError(
                    "key must be in {className}.{{{enumerator_list}}}"
                    ", got {key}".format(
                        className=cls.__className__,
                        enumerator_list=", ".join(cls.__members__),
                        key=key,
                    )
                )
            return cls[key.last_identifier]
        else:
            try:
                return cls[VariableName(key)]
            except ValueError:
                pass
            return cls[TypeName(key)]


class Enumeration(
    enum.Enum,
    metaclass=EnumerationMeta,
):
    def __str__(
        self,
    ) -> str:
        return f"{self.__className__}.{self.name}"

    __to_omc_literal__ = __str__
