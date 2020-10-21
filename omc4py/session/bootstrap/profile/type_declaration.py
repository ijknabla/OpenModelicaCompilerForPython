
from lxml import etree as xml  # type: ignore
import typing

from omc4py.session.types import (
    TypeName
)

from . base import (
    AbstractTypeProfile,
)


class IntrinsicTypeConfig(
    typing.NamedTuple,
):
    primitive: bool


IntrinsicTypeConfigs = typing.Dict[
    TypeName, IntrinsicTypeConfig
]

_intrinsicTypeConfigs: IntrinsicTypeConfigs = {
    TypeName("Real"):
        IntrinsicTypeConfig(
            primitive=True,
        ),
    TypeName("Integer"):
        IntrinsicTypeConfig(
            primitive=True,
        ),
    TypeName("Boolean"):
        IntrinsicTypeConfig(
            primitive=True,
        ),
    TypeName("String"):
        IntrinsicTypeConfig(
            primitive=True,
        ),
    TypeName("OpenModelica.$Code.VariableName"):
        IntrinsicTypeConfig(
            primitive=False,
        ),
    TypeName("OpenModelica.$Code.VariableNames"):
        IntrinsicTypeConfig(
            primitive=False,
        ),
    TypeName("OpenModelica.$Code.TypeName"):
        IntrinsicTypeConfig(
            primitive=False,
        ),
}


# @AbstractTypeProfile.register_concrete_class
class IntrinsicTypeProfile(
    AbstractTypeProfile,
):
    @classmethod
    def match(
        cls,
        root: xml._Element,
        name: TypeName,
    ) -> bool:
        return name in _intrinsicTypeConfigs
