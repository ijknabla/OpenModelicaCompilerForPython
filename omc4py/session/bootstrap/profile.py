
import abc
import enum
import keyword
from lxml import etree as xml  # type: ignore
import typing

from .code import (
    IGNORE_INDENT,
    INDENT,
    CodeBlock,
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
    ) -> CodeBlock:
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


class PrimitiveTypes(types.TypeName, enum.Enum):
    Real = types.TypeName("Real"),
    Integer = types.TypeName("Integer"),
    Boolean = types.TypeName("Boolean"),
    String = types.TypeName("String"),

    @property
    def pyTypeName(
        self
    ) -> str:
        if self is self.Real:
            return "builtins__.float"
        elif self is self.Integer:
            return "builtins__.int"
        elif self is self.Boolean:
            return "builtins__.bool"
        elif self is self.String:
            return "builtins__.str"
        else:
            raise NotImplementedError()

    @property
    def pyTypeNameShort(
        self
    ) -> str:
        if self is self.Real:
            return "float"
        elif self is self.Integer:
            return "int"
        elif self is self.Boolean:
            return "bool"
        elif self is self.String:
            return "str"
        else:
            raise NotImplementedError()


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

    def generate_argument_check_code(
        self,
        variableName: types.VariableName,
        sizes: "Sizes",
        hasDefault: bool
    ) -> CodeBlock:
        pyVariableName = to_pyVariableName(variableName)
        primitiveType = PrimitiveTypes(self.name)
        pyTypeName = primitiveType.pyTypeName
        pyTypeNameShort = primitiveType.pyTypeNameShort

        if sizes:
            raise NotImplementedError(f"{sizes}")

        if hasDefault:
            if_statement = CodeBlock(
                "if not(",
                CodeBlock(
                    f"isinstance({pyVariableName}, {pyTypeName})",
                    f"or {pyVariableName} is None",
                    indent=INDENT,
                ),
                "):",
            )
            typeError_message = CodeBlock(
                f'f"Argument {pyVariableName} must be {pyTypeNameShort} or None '
                f'got {{{pyVariableName}!r}}: {{type({pyVariableName}).__name__}}"',
            )
        else:
            if_statement = CodeBlock(
                f"if not isinstance({pyVariableName}, {pyTypeName}):",
            )
            typeError_message = CodeBlock(
                f'f"Argument {pyVariableName} must be {pyTypeNameShort} '
                f'got {{{pyVariableName}!r}}: {{type({pyVariableName}).__name__}}"',
            )

        return CodeBlock(
            if_statement,
            CodeBlock(
                "raise TypeError(",
                CodeBlock(
                    typeError_message,
                    indent=INDENT,
                ),
                ")",
                indent=INDENT
            ),
        )

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


class OutputArgument(
    typing.NamedTuple,
):
    typeProfile: AbstractTypeProfile
    sizes: Sizes
    name: types.VariableName
    comment: str


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
    ) -> CodeBlock:
        return CodeBlock(
            f"def {self.funcName}(",
            self.code_arguments,
            "):",
            self.code___doc__,
            self.code_execution,
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
    def outputArguments(
        self
    ) -> typing.Iterator[OutputArgument]:
        for argument in self.element.xpath('.//argument[@inputOutput="output"]'):
            anyProfile = get_profile(
                self.root,
                types.TypeName(argument.attrib["className"]),
            )

            typeProfile: AbstractTypeProfile
            if not isinstance(anyProfile, AbstractTypeProfile):
                raise TypeError(
                    "Argument class profile must be AbstractTypeProfile "
                    f"got {anyProfile!r}: {type(anyProfile).__name__}"
                )
            else:
                typeProfile = anyProfile

            yield OutputArgument(
                typeProfile=typeProfile,
                sizes=dimensions2sizes(argument.find("dimensions")),
                name=types.VariableName(argument.attrib["name"]),
                comment=argument.attrib["comment"],
            )

    @property
    def code_arguments(
        self,
    ) -> CodeBlock:
        result = CodeBlock(indent=INDENT)
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
    ) -> CodeBlock:
        return CodeBlock(
            '"""',
            CodeBlock(
                '```modelica',
                self.code,
                '```',
                indent=IGNORE_INDENT,
            ),
            '"""',
            indent=INDENT,
        )

    @property
    def code_execution(
        self
    ) -> CodeBlock:
        result = CodeBlock(indent=INDENT)

        result.append("# Argument check")
        for argument in self.inputArguments:
            typeProfile, sizes = argument.typeWithSizes
            result.append(
                typeProfile.generate_argument_check_code(
                    argument.name, sizes, argument.hasDefault
                )
            )
        result.append("")

        if self.use_positional_argument:
            result.append(self.code_call_by_positional)
        else:
            result.append(self.code_call_by_keyword)
        result.append("")

        result.append("return __result")

        return result

    @property
    def use_positional_argument(
        self,
    ) -> bool:
        return all(
            not argument.hasDefault
            for argument in self.inputArguments
        )

    @property
    def code_call_by_positional(
        self,
    ) -> CodeBlock:
        argument_items = CodeBlock(indent=INDENT)

        for argument in self.inputArguments:
            pyVariableName = to_pyVariableName(argument.name)
            argument_items.append(
                f"{pyVariableName},"
            )

        return CodeBlock(
            "# Pack positional arguments",
            "__args = [",
            argument_items,
            "]",
            "",
            "# Call function",
            f"__result = OMCSession__call__(self, {str(self.name)!r}, args=__args)",
        )

    @property
    def code_call_by_keyword(
        self,
    ) -> CodeBlock:
        argument_items = CodeBlock(indent=INDENT)

        for argument in self.inputArguments:
            omcVariableName = str(argument.name)
            pyVariableName = to_pyVariableName(argument.name)
            argument_items.append(
                f"{omcVariableName!r}: {pyVariableName},"
            )

        return CodeBlock(
            "# Pack keyword arguments",
            "__kwrds = {",
            argument_items,
            "}",
            "",
            "# Call function",
            f"__result = OMCSession__call__(self, {str(self.name)!r}, kwrds=__kwrds)",
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
    ) -> CodeBlock:
        return CodeBlock(
            f"{self.funcName} = {self.target.funcName}",
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
