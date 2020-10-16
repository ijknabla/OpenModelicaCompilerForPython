
import abc
import keyword
from lxml import etree as xml  # type: ignore
import typing

from . import (
    code
)

from .. import (
    types,
)


def to_pyVariableName(
    variableName: types.VariableName,
) -> str:
    result = str(variableName)
    while keyword.iskeyword(result):
        result += "_"
    return result


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


Sizes = typing.Tuple[typing.Union[None, int, str], ...]


def dimensions2sizes(
    dimensions: xml._Element,
) -> Sizes:
    def size_generator(
    ) -> typing.Iterator[typing.Union[None, int, str]]:
        assert(dimensions.tag == "dimensions")
        for dimension in dimensions.xpath("./dimension"):
            size = dimension.attrib["size"]
            if size == ":":
                yield None
            else:
                try:
                    yield int(size)
                except ValueError:
                    yield size

    return tuple(size_generator())


class AbstractTypeProfile(
    AbstractProfile
):
    ...


class TypeWithSizes(
    typing.NamedTuple,
):
    typeProfile: AbstractTypeProfile
    sizes: Sizes


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


primitiveTypeNames = {
    types.TypeName("Real"),
    types.TypeName("Integer"),
    types.TypeName("Boolean"),
    types.TypeName("String"),
}

codeTypeNames = {
    types.TypeName("OpenModelica.$Code.VariableName"),
    types.TypeName("OpenModelica.$Code.TypeName"),
}


@register_profileClass
class PrimitiveTypeProfile(
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
        return name in primitiveTypeNames

    @property
    def supported(
        self
    ) -> bool:
        return True


@register_profileClass
class CodeTypeProfile(
    AbstractTypeProfile
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
        return name in codeTypeNames

    @property
    def supported(
        self
    ) -> bool:
        return False


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
        return name not in primitiveTypeNames | codeTypeNames

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


class InputArgument(
    typing.NamedTuple,
):
    typeWithSizes: TypeWithSizes
    name: types.VariableName
    comment: str
    hasDefault: bool


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
            profile.supported and not sizes
            for profile, sizes in self.variableTypes
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
                "):",
                self.code___doc__,
            ]
        )

    @property
    def variableTypes(
        self,
    ) -> typing.Set[TypeWithSizes]:
        def typeWithSizes_generator(
        ) -> typing.Iterator[TypeWithSizes]:
            for argument in self.element.xpath(".//argument"):
                typeProfile = get_profile(
                    self.root,
                    types.TypeName(argument.attrib["className"])
                )
                if isinstance(typeProfile, AbstractTypeProfile):
                    yield TypeWithSizes(
                        typeProfile=typeProfile,
                        sizes=dimensions2sizes(argument.find("dimensions")),
                    )
                else:
                    raise TypeError(
                        "Profile must be AbstractTypeProfile "
                        f"got {typeProfile}"
                    )

        return set(typeWithSizes_generator())

    @property
    def inputArguments(
        self
    ) -> typing.Iterator[InputArgument]:
        for argument in self.element.xpath('.//argument[@inputOutput="input"]'):
            typeProfile = get_profile(
                self.root,
                types.TypeName(argument.attrib["className"]),
            )
            if isinstance(typeProfile, AbstractTypeProfile):
                typeWithSizes = TypeWithSizes(
                    typeProfile=typeProfile,
                    sizes=dimensions2sizes(argument.find("dimensions"))
                )

            yield InputArgument(
                typeWithSizes=typeWithSizes,
                name=types.VariableName(argument.attrib["name"]),
                comment=argument.attrib["comment"],
                hasDefault=bool(
                    eval(argument.attrib["hasDefault"].capitalize())
                ),
            )

    @property
    def code_arguments(
        self,
    ) -> code.CodeBlock:
        result = code.CodeBlock([], indent=code.INDENT)
        result.append("self,")
        for argument in sorted(
            self.inputArguments,
            key=lambda arg: 1 if arg.hasDefault else 0
        ):
            varName = to_pyVariableName(argument.name)
            if argument.hasDefault:
                default = "=None"
            else:
                default = ""
            result.append(f"{varName}{default},")

        return result

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
) -> AbstractProfile:
    for ProfileClass in __profileClasses:
        if ProfileClass.match(root, name):
            return ProfileClass(root, name)

    raise ValueError(
        f"Failed to create profile for {name}"
    )
