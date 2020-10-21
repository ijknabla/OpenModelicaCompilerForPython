
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
    supported: bool


IntrinsicTypeConfigs = typing.Dict[
    TypeName, IntrinsicTypeConfig
]

_intrinsicTypeConfigs: IntrinsicTypeConfigs = {
    TypeName("Real"):
        IntrinsicTypeConfig(
            primitive=True,
            supported=True,
        ),
    TypeName("Integer"):
        IntrinsicTypeConfig(
            primitive=True,
            supported=True,
        ),
    TypeName("Boolean"):
        IntrinsicTypeConfig(
            primitive=True,
            supported=True,
        ),
    TypeName("String"):
        IntrinsicTypeConfig(
            primitive=True,
            supported=True,
        ),
    TypeName("OpenModelica.$Code.VariableName"):
        IntrinsicTypeConfig(
            primitive=False,
            supported=True,
        ),
    TypeName("OpenModelica.$Code.TypeName"):
        IntrinsicTypeConfig(
            primitive=False,
            supported=True,
        ),
}


@AbstractTypeProfile.register_concrete_class
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

    @property
    def config(
        self,
    ) -> IntrinsicTypeConfig:
        return _intrinsicTypeConfigs[self.name]

    @property
    def supported(
        self,
    ) -> bool:
        return self.config.supported


@AbstractTypeProfile.register_concrete_class
class UnsupportedIntrinsicTypeProfile(
    AbstractTypeProfile,
):
    @classmethod
    def match(
        cls,
        root: xml._Element,
        name: TypeName,
    ) -> bool:
        element = cls.find_element(root, name)
        if element is not None:
            return False
        return name not in _intrinsicTypeConfigs

    @property
    def supported(
        self
    ) -> bool:
        return False
