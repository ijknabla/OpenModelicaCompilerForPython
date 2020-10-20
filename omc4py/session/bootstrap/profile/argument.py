
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
