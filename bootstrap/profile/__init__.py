
import enum
import itertools
from lxml import etree as xml  # type: ignore
import operator
import typing

from ..code import (
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
from .component import (
    InputArgument,
    OutputArgument,
    Sizes,
)

from . import type_declaration


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
            f"def {self.py_method_name}(",
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
                sizes=InputArgument.dimensions2sizes(
                    argument.find("dimensions")),
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
                sizes=OutputArgument.dimensions2sizes(
                    argument.find("dimensions")),
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
        result.append("\n")
        result.append(self.code_call)
        result.append("\n")
        result.append("return __result")

        return result

    @property
    def code_call(
        self,
    ) -> CodeBlock:
        args_list = []
        kwrds_list = []

        to_args = True
        for argument in self.inputArguments:
            to_args &= not argument.optional
            if to_args:
                args_list.append(
                    f"{argument.py_checked_variable},"
                )
            else:
                kwrds_list.append(
                    f"{str(argument.name)!r}: {argument.py_checked_variable},"
                )

        return CodeBlock(
            "# Pack positional arguments",
            "__args = [",
            CodeBlock(
                *args_list,
                indent=INDENT,
            ),
            "]",
            "__kwrds = {",
            CodeBlock(
                *kwrds_list,
                indent=INDENT,
            ),
            "}",
            "",
            "# Call function",
            "__result = OMCSession__call__(",
            CodeBlock(
                "self,",
                f"{self.omc_func_name!r},",
                "args=__args,",
                "kwrds=__kwrds,",
                indent=INDENT,
            ),
            ")",
        )

    @property
    def py_method_name(
        self,
    ) -> str:
        return str(self.name.last_identifier)

    @property
    def omc_func_name(
        self,
    ) -> str:
        return str(self.name.last_identifier)


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
            f"{self.py_method_name} = {self.target.py_method_name}",
        )

    @property
    def target(
        self
    ) -> FunctionDeclarationProfile:
        profile = get_profile_from_xml(
            self.root,
            TypeName(self.element.attrib["ref"]),
        )
        assert(isinstance(profile, FunctionDeclarationProfile))
        return profile

    @property
    def py_method_name(
        self,
    ) -> str:
        return str(self.name.last_identifier)
