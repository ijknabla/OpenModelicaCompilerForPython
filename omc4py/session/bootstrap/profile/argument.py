
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


class OutputArgument(
    typing.NamedTuple,
):
    typeProfile: AbstractTypeProfile
    sizes: Sizes
    name: VariableName
    comment: str
