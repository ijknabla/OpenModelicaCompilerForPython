
import abc
from lxml import etree as xml  # type: ignore
import typing

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

    @classmethod
    @abc.abstractmethod
    def match(
        cls,
        root: xml._Element,
        name: types.TypeName,
    ) -> bool:
        return False


__profileClasses: typing.List[typing.Type[AbstractProfile]] \
    = []


def register_profileClass(
    profileClass: typing.Type[AbstractProfile],
) -> typing.Type[AbstractProfile]:
    __profileClasses.append(profileClass)
    return profileClass


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
