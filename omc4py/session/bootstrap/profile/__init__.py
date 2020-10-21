
import enum
import itertools
from lxml import etree as xml  # type: ignore
import operator
import typing

from omc4py.session.bootstrap.code import (
    IGNORE_INDENT,
    INDENT,
    CodeBlock,
)

from omc4py.session.types import (
    TypeName,
    VariableName,
)

from .base import (
    AbstractFunctionProfile,
    AbstractTypeProfile,
    AbstractExtrinsicProfile,
    get_profile_from_xml,
)
from .argument import (
    InputArgument,
    OutputArgument,
    Sizes,
)

from . import type_declaration


def dimensions2sizes(
    dimensions: xml._Element,
) -> Sizes:
    def size_generator(
    ) -> typing.Iterator[typing.Optional[int]]:
        assert(dimensions.tag == "dimensions")
        for dimension in dimensions.xpath("./dimension"):
            try:
                yield int(dimension.attrib["size"])
            except ValueError:
                yield None

    return tuple(size_generator())


@AbstractTypeProfile.register_concrete_class
class TypeDeclarationProfile(
    AbstractTypeProfile,
    AbstractExtrinsicProfile,
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
        return element.tag == "type"

    @property
    def supported(self) -> bool: return False

    @property
    def primitive(self) -> bool: return False

    @property
    def py_cast_type_expression(
        self,
    ) -> str:
        return super().py_cast_type_expression


@AbstractTypeProfile.register_concrete_class
class RecordDeclarationProfile(
    AbstractTypeProfile,
    AbstractExtrinsicProfile,
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
        return element.tag == "record"

    @property
    def supported(self) -> bool: return False

    @property
    def primitive(self) -> bool: return False

    @property
    def py_cast_type_expression(
        self,
    ) -> str:
        return super().py_cast_type_expression


@AbstractFunctionProfile.register_concrete_class
class FunctionDeclarationProfile(
    AbstractFunctionProfile,
    AbstractExtrinsicProfile,
):
    @classmethod
    def match(
        cls,
        root: xml.Element,
        name: TypeName
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
        return all(
            typeProfile.supported
            for typeProfile in self.variableTypes
        )

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
    ) -> typing.Set[AbstractTypeProfile]:
        return set(
            map(
                operator.attrgetter("typeProfile"),
                itertools.chain(
                    self.inputArguments,
                    self.outputArguments
                )
            )
        )

    @property
    def inputArguments(
        self
    ) -> typing.Iterator[InputArgument]:
        for argument in self.element.xpath(
            './/argument[@inputOutput="input"]'
        ):
            anyProfile = get_profile_from_xml(
                self.root,
                TypeName(argument.attrib["className"]),
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
                name=VariableName(argument.attrib["name"]),
                comment=argument.attrib["comment"],
                optional=bool(
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
            anyProfile = get_profile_from_xml(
                self.root,
                TypeName(argument.attrib["className"]),
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
                name=VariableName(argument.attrib["name"]),
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
            key=lambda arg: 1 if arg.optional else 0
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
            not argument.optional
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


@AbstractFunctionProfile.register_concrete_class
class FunctionAliasProfile(
    AbstractFunctionProfile,
    AbstractExtrinsicProfile,
):
    @classmethod
    def match(
        cls,
        root: xml.Element,
        name: TypeName,
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
        profile = get_profile_from_xml(
            self.root,
            TypeName(self.element.attrib["ref"]),
        )
        assert(isinstance(profile, AbstractFunctionProfile))
        return profile
