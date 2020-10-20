
import enum
from lxml import etree as xml  # type: ignore
import typing

from omc4py.session.bootstrap.code import (
    IGNORE_INDENT,
    INDENT,
    CodeBlock,
)

from omc4py.session import (
    types,
)

from .base import (
    AbstractFunctionProfile,
    AbstractTypeProfile,
    AbstractExtrinsicProfile,
    get_profile,
    register_profileClass,
)
from .argument import (
    InputArgument,
    OutputArgument,
)


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


class TypeWithSizes(
    typing.NamedTuple,
):
    typeProfile: AbstractTypeProfile
    sizes: Sizes


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


class PrimitiveTypes(
    types.TypeName, enum.Enum
):
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


class CodeTypes(
    types.TypeName, enum.Enum
):
    VariableName = types.TypeName("OpenModelica.$Code.VariableName")
    TypeName = types.TypeName("OpenModelica.$Code.TypeName")

    @property
    def pyTypeName(
        self
    ) -> str:
        if self is self.VariableName:
            return "types__.VariableName"
        elif self is self.TypeName:
            return "types__.TypeName"
        else:
            raise NotImplementedError()


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
        return name not in primitiveTypeNames | codeTypeNames

    @property
    def supported(
        self
    ) -> bool:
        return False


@register_profileClass
class TypeDeclarationProfile(
    AbstractTypeProfile,
    AbstractExtrinsicProfile,
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
    AbstractExtrinsicProfile,
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
    AbstractExtrinsicProfile,
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
            for profile, sizes in self.variableTypes
        ):
            return False
        return True

    def generate_method_code(
        self
    ) -> CodeBlock:
        return CodeBlock(
            f"def {self.funcName}(",
            CodeBlock(
                self.code_arguments,
                indent=INDENT,
            ),
            "):",
            self.code___doc__,
            self.code_execution,
        )

    @property
    def variableTypes(
        self,
    ) -> typing.Set[TypeWithSizes]:
        return (
            set(
                TypeWithSizes(
                    typeProfile=argument.typeProfile,
                    sizes=argument.sizes
                )
                for argument in self.inputArguments
            )
            | set(
                TypeWithSizes(
                    typeProfile=argument.typeProfile,
                    sizes=argument.sizes
                )
                for argument in self.outputArguments
            )
        )

    @property
    def inputArguments(
        self
    ) -> typing.Iterator[InputArgument]:
        for argument in self.element.xpath(
            './/argument[@inputOutput="input"]'
        ):
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

            yield InputArgument(
                typeProfile=typeProfile,
                sizes=dimensions2sizes(argument.find("dimensions")),
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
        for argument in self.element.xpath(
            './/argument[@inputOutput="output"]'
        ):
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
        code = CodeBlock()
        code.append("self,")
        for argument in sorted(
            self.inputArguments,
            key=lambda arg: 1 if arg.hasDefault else 0
        ):
            code.append(f"{argument.py_argument},")
        return code

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
            result.append(
                argument.check_code
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
            argument_items.append(
                f"{argument.py_checked_argument},"
            )

        return CodeBlock(
            "# Pack positional arguments",
            "__args = [",
            argument_items,
            "]",
            "",
            "# Call function",
            "__result = OMCSession__call__(",
            CodeBlock(
                "self,",
                f"{str(self.name)!r},",
                "args=__args",
                indent=INDENT,
            ),
            ")",
        )

    @property
    def code_call_by_keyword(
        self,
    ) -> CodeBlock:
        argument_items = CodeBlock(indent=INDENT)

        for argument in self.inputArguments:
            argument_items.append(
                f"{str(argument.name)!r}: {argument.py_checked_argument},"
            )

        return CodeBlock(
            "# Pack keyword arguments",
            "__kwrds = {",
            argument_items,
            "}",
            "",
            "# Call function",
            "__result = OMCSession__call__(",
            CodeBlock(
                "self,",
                f"{str(self.name)!r},",
                "kwrds=__kwrds",
                indent=INDENT,
            ),
            ")",
        )


@register_profileClass
class FunctionAliasProfile(
    AbstractFunctionProfile,
    AbstractExtrinsicProfile,
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
