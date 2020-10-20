
import keyword
import typing

from omc4py.session.types import (
    VariableName,
    TypeName,
)

from .base import (
    AbstractTypeProfile,
)

Size = typing.Optional[int]
Sizes = typing.Tuple[Size, ...]


def to_pyVariableName(
    variableName: VariableName,
) -> str:
    result = str(variableName)
    while keyword.iskeyword(result):
        result += "_"
    return result


class InputArgument(
    typing.NamedTuple,
):
    typeProfile: AbstractTypeProfile
    sizes: Sizes
    name: VariableName
    comment: str
    hasDefault: bool

    @property
    def py_argument(
        self,
    ) -> str:
        result = str(self.name)
        while keyword.iskeyword(result):
            result += "_"
        return result

    @property
    def py_internal_variable(
        self,
    ) -> str:
        return f"{self.py_argument!s}__internal__"


class OutputArgument(
    typing.NamedTuple,
):
    typeProfile: AbstractTypeProfile
    sizes: Sizes
    name: VariableName
    comment: str
