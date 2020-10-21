
from lxml import etree as xml  # type: ignore
import typing

from omc4py.session.types import (
    TypeName
)

from . base import (
    AbstractTypeProfile,
    AbstractExtrinsicTypeProfile,
)

from .. import code


class IntrinsicTypeConfig(
    typing.NamedTuple,
):
    primitive: bool
    py_cast_type_expression: str
    py_check_type_expression: str


IntrinsicTypeConfigs = typing.Dict[
    TypeName, IntrinsicTypeConfig
]

_intrinsicTypeConfigs: IntrinsicTypeConfigs = {
    TypeName("Real"):
        IntrinsicTypeConfig(
            primitive=True,
            py_cast_type_expression="numpy__.double",
            py_check_type_expression="(numpy__.float, numpy__.double)",
        ),
    TypeName("Integer"):
        IntrinsicTypeConfig(
            primitive=True,
            py_cast_type_expression="numpy__.intc",
            py_check_type_expression="(numpy__.int, numpy__.intc)",
        ),
    TypeName("Boolean"):
        IntrinsicTypeConfig(
            primitive=True,
            py_cast_type_expression="numpy__.bool_",
            py_check_type_expression="(numpy__.bool, numpy__.bool_)",
        ),
    TypeName("String"):
        IntrinsicTypeConfig(
            primitive=True,
            py_cast_type_expression="numpy__.str_",
            py_check_type_expression="(numpy__.str, numpy__.str_)",
        ),
    TypeName("OpenModelica.$Code.VariableName"):
        IntrinsicTypeConfig(
            primitive=False,
            py_cast_type_expression="types__.VariableName",
            py_check_type_expression="types__.VariableName",
        ),
    TypeName("OpenModelica.$Code.TypeName"):
        IntrinsicTypeConfig(
            primitive=False,
            py_cast_type_expression="types__.TypeName",
            py_check_type_expression="types__.TypeName",
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
    def supported(self) -> bool: return True

    @property
    def primitive(
        self,
    ) -> bool:
        return self.config.primitive

    @property
    def py_cast_type_expression(
        self,
    ) -> str:
        return self.config.py_cast_type_expression

    @property
    def py_check_type_expression(
        self,
    ) -> str:
        return self.config.py_check_type_expression


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
    def supported(self) -> bool: return False

    @property
    def primitive(self) -> bool: return False

    @property
    def py_cast_type_expression(
        self,
    ) -> str:
        raise ValueError(
            f"{self.name} is unsupported type"
        )


@AbstractExtrinsicTypeProfile.register_concrete_class
class EnumerationDeclarationProfile(
    AbstractExtrinsicTypeProfile
):
    @classmethod
    def match(
        cls,
        root: xml._Element,
        name: TypeName,
    ) -> bool:
        element = cls.find_element(root, name)
        if element is None:
            return False
        return element.tag == "type" and element.xpath(".//enumerators")

    @property
    def supported(self) -> bool: return False

    @property
    def primitive(self) -> bool: return False

    @property
    def py_cast_type_expression(
        self,
    ) -> str:
        return super().py_cast_type_expression

    def generate_class_definition(
        self,
    ) -> code.CodeBlock:
        return code.CodeBlock(
            f"class {self.name.parts[-1]}:",
            code.CodeBlock(
                "...",
                indent=code.INDENT,
            ),
        )
