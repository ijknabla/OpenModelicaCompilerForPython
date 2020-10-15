
import abc
from lxml import etree as xml  # type: ignore
import typing

from . import (
    code
)

from .. import (
    types,
)


class AbstractProfile(
    abc.ABC
):
    def __init__(
        self,
        root: xml._Element,
        name: types.TypeName,
    ):
        self.root = root
        self.name = name

    def __hash__(
        self
    ):
        return hash(
            tuple(map(hash, [self.root, self.name]))
        )

    def __eq__(
        self,
        other
    ):
        if not isinstance(other, AbstractProfile):
            return False
        else:
            return (
                self.root == other.root
                and self.name == other.name
            )

    @classmethod
    @abc.abstractmethod
    def match(
        cls,
        root: xml._Element,
        name: types.TypeName,
    ) -> bool:
        return False

    @property
    @abc.abstractmethod
    def supported(
        self
    ) -> bool:
        return False

    @staticmethod
    def find_element(
        root: xml._Element,
        name: types.TypeName,
    ) -> typing.Optional[xml._Element]:
        element_list = root.xpath(
            f'//*[@id="{name!s}"]'
        )
        if element_list:
            return element_list[0]
        else:
            return None


class ExtrinsicProfile(
    AbstractProfile
):
    @property
    def element(
        self
    ) -> xml._Element:
        return self.root.xpath(
            f'//*[@id="{self.name!s}"]'
        )[0]

    @property
    def code(
        self
    ) -> str:
        return self.element.find("code").text


class AbstractTypeProfile(
    AbstractProfile
):
    ...


class AbstractFunctionProfile(
    AbstractProfile
):
    @abc.abstractmethod
    def generate_method_code(
        self,
    ) -> code.CodeBlock:
        raise NotImplementedError()

    @property
    def funcName(
        self,
    ) -> str:
        return str(self.name.parts[-1])


__profileClasses: typing.List[typing.Type[AbstractProfile]] \
    = []


def register_profileClass(
    profileClass: typing.Type[AbstractProfile],
) -> typing.Type[AbstractProfile]:
    __profileClasses.append(profileClass)
    return profileClass


builtinTypeNames = {
    types.TypeName("Real"),
    types.TypeName("Integer"),
    types.TypeName("Boolean"),
    types.TypeName("String"),
    types.TypeName("OpenModelica.$Code.VariableName"),
    types.TypeName("OpenModelica.$Code.TypeName"),
}


@register_profileClass
class BuiltinTypeProfile(
    AbstractTypeProfile,
):
    @classmethod
    def match(
        cls,
        root: xml._Element,
        name: types.TypeName,
    ) -> bool:
        element = cls.find_element(root, name)
        if element is not None:
            return False
        return name in builtinTypeNames

    @property
    def supported(
        self
    ) -> bool:
        return True


@register_profileClass
class UnsupportedBuiltinTypeProfile(
    AbstractTypeProfile,
):
    @classmethod
    def match(
        cls,
        root: xml._Element,
        name: types.TypeName,
    ) -> bool:
        element = cls.find_element(root, name)
        if element is not None:
            return False
        return name not in builtinTypeNames

    @property
    def supported(
        self
    ) -> bool:
        return False


@register_profileClass
class TypeDeclarationProfile(
    AbstractTypeProfile,
    ExtrinsicProfile,
):
    @classmethod
    def match(
        cls,
        root: xml._Element,
        name: types.TypeName,
    ) -> bool:
        element = cls.find_element(root, name)
        if element is None:
            return False
        return element.tag == "type"

    @property
    def supported(
        self
    ) -> bool:
        return False


@register_profileClass
class RecordDeclarationProfile(
    AbstractTypeProfile,
    ExtrinsicProfile,
):
    @classmethod
    def match(
        cls,
        root: xml._Element,
        name: types.TypeName,
    ) -> bool:
        element = cls.find_element(root, name)
        if element is None:
            return False
        return element.tag == "record"

    @property
    def supported(
        self
    ) -> bool:
        return False


@register_profileClass
class FunctionDeclarationProfile(
    AbstractFunctionProfile,
    ExtrinsicProfile,
):
    @classmethod
    def match(
        cls,
        root: xml.Element,
        name: types.TypeName
    ) -> bool:
        element = cls.find_element(root, name)
        if element is None:
            return False
        else:
            return (
                element.tag == "function"
                and "ref" not in element.attrib
            )

    @property
    def supported(
        self,
    ) -> bool:
        if not all(
            profile.supported
            for profile in self.variableProfiles
        ):
            return False
        return True

    def generate_method_code(
        self
    ) -> code.CodeBlock:
        return code.CodeBlock(
            [
                f"def {self.funcName}(",
                self.code_arguments,
                f"):",
                self.code___doc__,
            ]
        )

    @property
    def variableProfiles(
        self,
    ) -> typing.Set[AbstractTypeProfile]:
        return set(
            get_profile(
                self.root,
                types.TypeName(argument.attrib["className"]),
            )
            for argument in self.element.xpath(".//argument")
        )

    @property
    def code_arguments(
        self,
    ) -> code.CodeBlock:
        return code.CodeBlock(
            [
                "self,",
            ],
            indent=code.INDENT
        )

    @property
    def code___doc__(
        self,
    ) -> code.CodeBlock:
        return code.CodeBlock(
            [
                '"""',
                code.CodeBlock(
                    [
                        '```modelica',
                        self.code,
                        '```'
                    ],
                    indent=code.IGNORE_INDENT,
                ),
                '"""',
            ],
            indent=code.INDENT,
        )

@register_profileClass
class FunctionAliasProfile(
    AbstractFunctionProfile,
    ExtrinsicProfile,
):
    @classmethod
    def match(
        cls,
        root: xml.Element,
        name: types.TypeName,
    ) -> bool:
        element = cls.find_element(root, name)
        if element is None:
            return False
        else:
            return (
                element.tag == "function"
                and "ref" in element.attrib
            )

    @property
    def supported(
        self,
    ) -> bool:
        return self.target.supported

    def generate_method_code(
        self,
    ) -> code.CodeBlock:
        return code.CodeBlock(
            [
                f"{self.funcName} = {self.target.funcName}"
            ]
        )

    @property
    def target(
        self
    ) -> AbstractFunctionProfile:
        profile = get_profile(
            self.root,
            types.TypeName(self.element.attrib["ref"]),
        )
        assert(isinstance(profile, AbstractFunctionProfile))
        return profile


def get_profile(
    root: xml._Element,
    name: types.TypeName,
):
    profile: AbstractProfile
    for ProfileClass in __profileClasses:
        if ProfileClass.match(root, name):
            return ProfileClass(root, name)

    raise ValueError(
        f"Failed to create profile for {name}"
    )
