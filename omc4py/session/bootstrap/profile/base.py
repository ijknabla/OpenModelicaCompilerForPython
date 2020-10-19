
import abc
from lxml import etree as xml
import typing

from omc4py.session import types
from omc4py.session.bootstrap import code


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


class AbstractExtrinsicProfile(
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
