
import abc
from lxml import etree as xml  # type: ignore
import typing
import typing_extensions

from omc4py.session import types
from omc4py.session.bootstrap import code


class AbstractProfile(
    abc.ABC
):
    __concrete_classes: \
        typing_extensions.Final[typing.List[typing.Type["AbstractProfile"]]] \
        = []

    @classmethod
    def register_concrete_class(
        cls,
        class_: typing.Type["AbstractProfile"],
    ) -> typing.Type["AbstractProfile"]:
        cls.__concrete_classes.append(class_)
        return class_

    @classmethod
    def find_concrete_class(
        cls,
        root: xml._Element,
        name: types.TypeName,
    ) -> typing.Type["AbstractProfile"]:
        for ProfileClass in cls.__concrete_classes:
            if ProfileClass.match(root, name):
                return ProfileClass

        raise ValueError(
            f"Can't find profile class for {name}"
        )

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

    def get_profile(
        self,
        name: types.TypeName,
    ) -> "AbstractProfile":
        return get_profile_from_xml(
            self.root, name
        )


def get_profile_from_xml(
    root: xml._Element,
    name: types.TypeName,
) -> AbstractProfile:
    return AbstractProfile.find_concrete_class(root, name)(root, name)


class AbstractExtrinsicProfile(
    AbstractProfile
):
    @property
    def element(
        self
    ) -> xml._Element:
        element = self.find_element(
            self.root,
            self.name,
        )
        if element is None:
            raise ValueError(
                "Can't find element "
                f"@id=\"{self.name}\" from {self.root}"
            )
        return element

    @property
    def code(
        self
    ) -> str:
        return self.element.find("code").text


class AbstractTypeProfile(
    AbstractProfile
):
    @property
    @abc.abstractmethod
    def primitive(
        self,
    ) -> bool:
        raise NotImplementedError()

    @property
    @abc.abstractmethod
    def py_cast_type_expression(
        self,
    ) -> str:
        raise NotImplementedError()


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
