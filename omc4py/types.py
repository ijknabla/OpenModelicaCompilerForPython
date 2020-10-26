
import enum

from .primitive_types import TypeName


class Enumeration(
    enum.Enum,
):
    __className__: TypeName

    def __str__(
        self,
    ) -> str:
        return f"{self.__className__}.{self.name}"

    __to_omc_literal__ = __str__
