
import abc
import argparse
import keyword
from lxml import etree as xml  # type: ignore
from pathlib import Path
import re
import typing

from . import (
    load_schema,
    profile,
)

from .code import (
    IGNORE_INDENT,
    INDENT,
    CodeBlock,
)

from .. import types


def avoid_keyword(
    variableName: types.VariableName,
) -> str:
    result = str(variableName)
    while keyword.iskeyword(result):
        result += "_"
    return result


def encode_specifier(
    specifier: typing.Union[types.VariableName, types.TypeName]
) -> str:
    pattern = re.compile(r"[0-9A-Za-z]")

    def characters(
    ) -> typing.Iterator[str]:
        for char in str(specifier):
            if pattern.match(char):
                yield char
            else:
                code_point = ord(char)
                yield f"_{code_point:x}_"

    return "".join(characters())


def export_function_names(
    root: xml._Element,
) -> typing.Iterator[types.TypeName]:
    for element in root.xpath(
        '//package[@id="OpenModelica.Scripting"]/classes/function'
    ):
        yield types.TypeName(element.attrib["id"])


ProfileFactory = typing.Callable[[types.TypeName], "AbstractProfile"]


class AbstractProfile(
    abc.ABC,
):
    @property
    @abc.abstractmethod
    def name(
        self
    ) -> types.TypeName:
        raise NotImplementedError


class AbstractIntrinsicProfile(
    AbstractProfile,
):
    className: types.TypeName

    def __init__(
        self,
        className: types.TypeName,
    ):
        self.className = className

    @classmethod
    @abc.abstractmethod
    def check_className(
        cls,
        className: types.TypeName,
    ) -> bool:
        return False

    @property
    def name(
        self
    ) -> types.TypeName:
        return self.className


class AbstractExtrinsicProfile(
    AbstractProfile
):
    element: xml._Element
    factory: ProfileFactory

    def __init__(
        self,
        element: xml._Element,
        factory: ProfileFactory,
    ):
        self.element = element
        self.factory = factory

    @classmethod
    @abc.abstractmethod
    def check_element(
        cls,
        element: xml._Element,
    ) -> bool:
        return False

    @property
    def name(
        self
    ) -> types.TypeName:
        return types.TypeName(self.element.attrib["id"])

    @property
    def code(
        self
    ) -> str:
        code_optional = self.element.xpath(".//code")
        if code_optional:
            return code_optional[0].text
        else:
            return ""


extrinsicProfileClasses: typing.List[typing.Type[AbstractExtrinsicProfile]] \
    = []
intrinsicProfileClasses: typing.List[typing.Type[AbstractIntrinsicProfile]] \
    = []


def register_extrinsicProfileClass(
    klass: typing.Type[AbstractExtrinsicProfile]
) -> typing.Type[AbstractExtrinsicProfile]:
    extrinsicProfileClasses.append(klass)
    return klass


def register_intrinsicProfileClass(
    klass: typing.Type[AbstractIntrinsicProfile]
) -> typing.Type[AbstractIntrinsicProfile]:
    intrinsicProfileClasses.append(klass)
    return klass


def get_profile_factory(
    root: xml._Element,
    cache: typing.Dict[types.TypeName, AbstractProfile],
) -> ProfileFactory:
    def factory(
        className: types.TypeName
    ) -> AbstractProfile:
        if className not in cache:
            element_optional = root.xpath(f'//*[@id="{className!s}"]')
            if element_optional:
                element, = element_optional
                profile: AbstractProfile
                for ExtrinsicProfileClass in extrinsicProfileClasses:
                    if ExtrinsicProfileClass.check_element(element):
                        profile = ExtrinsicProfileClass(element, factory)
                        break
                else:
                    raise ValueError(
                        f"Failed to create profile for {className}"
                    )
            else:
                for IntrinsicProfileClass in intrinsicProfileClasses:
                    if IntrinsicProfileClass.check_className(className):
                        profile = IntrinsicProfileClass(className)
                        break
                else:
                    raise ValueError(
                        f"Failed to create profile for {className}"
                    )
            cache[className] = profile
        return cache[className]

    return factory


def dimensions2sizes(
    dimensions: xml._Element
) -> typing.Tuple[int, ...]:
    def size_generator(
    ) -> typing.Iterator[int]:
        assert(dimensions.tag == "dimensions")
        for dimension in dimensions.xpath(".//dimension"):
            size = dimension.attrib["size"]
            if size == ":":
                yield 0
            else:
                yield int(size)
    return tuple(size_generator())


class InputArgument(
    typing.NamedTuple,
):
    className: types.TypeName
    name: types.VariableName
    sizes: typing.Tuple[int, ...]
    comment: str
    hasDefault: bool


supportedTypes = {
    types.TypeName("Real"),
    types.TypeName("Integer"),
    types.TypeName("Boolean"),
    types.TypeName("String"),
}


@register_extrinsicProfileClass
class FunctionProfile(
    AbstractExtrinsicProfile,
):
    @classmethod
    def check_element(
        cls,
        element: xml._Element,
    ) -> bool:
        return element.tag == "function" and "ref" not in element.attrib

    @property
    def variableTypes(
        self
    ) -> typing.Set[types.TypeName]:
        return set(
            types.TypeName(argument.attrib["className"])
            for argument in self.element.xpath('.//argument')
        )

    @property
    def inputArguments(
        self
    ) -> typing.Iterator[InputArgument]:
        for element in self.element.xpath('.//argument[@inputOutput="input"]'):
            yield InputArgument(
                className=types.TypeName(element.attrib["className"]),
                name=types.VariableName(element.attrib["name"]),
                sizes=dimensions2sizes(element.find("dimensions")),
                comment=element.attrib["comment"],
                hasDefault=bool(
                    eval(element.attrib["hasDefault"].capitalize())
                ),
            )

    @property
    def outputArguments(
        self
    ) -> typing.List[xml._Element]:
        return self.element.xpath('.//argument[@inputOutput="output"]')

    @property
    def supported(
        self,
    ) -> bool:
        if not self.variableTypes <= supportedTypes:
            return False

        outputs = self.outputArguments
        if not len(outputs) <= 1:
            return False
        if not all(
            len(dimensions2sizes(output.xpath('.//dimensions')[0])) == 0
            for output in outputs
        ):
            return False

        return True

    @property
    def __code__arguments(
        self,
    ) -> CodeBlock:
        code = CodeBlock([], indent=INDENT)
        code.append("self,")
        for argument in self.inputArguments:
            varName = avoid_keyword(argument.name)
            if argument.hasDefault:
                default = " = None"
            else:
                default = ""
            code.append(f"{varName}{default},")

        return code

    @property
    def __code__doc__(
        self,
    ) -> CodeBlock:
        return CodeBlock(
            [
                '"""',
                CodeBlock(
                    [
                        "```modelica",
                        self.code,
                        "```"
                    ],
                    indent=IGNORE_INDENT,
                ),
                '"""',
            ],
            indent=INDENT
        )

    def to_codeBlock(
        self,
    ) -> CodeBlock:
        py_funcName = str(self.name.parts[-1])
        assert(py_funcName.isidentifier())
        return CodeBlock(
            [
                f"def {py_funcName}(",
                self.__code__arguments,
                "):",
                self.__code__doc__
            ]
        )


@register_extrinsicProfileClass
class FunctionAliasProfile(
    AbstractExtrinsicProfile
):
    @classmethod
    def check_element(
        cls,
        element: xml._Element,
    ) -> bool:
        return element.tag == "function" and "ref" in element.attrib


def write_module(
    file: typing.TextIO,
    root: xml._Element,
) -> None:
    code_import = CodeBlock("""\
import builtins as builtins__
import functools as functools__
from omc4py.session import OMCSessionBase as OMCSessionBase__
from omc4py.session import OMCSession__open as OMCSession__open__
from omc4py.session import OMCSession__close as close_session
""")

    code_class = CodeBlock(
        [
            "class OMCSession(",
            CodeBlock(
                [
                    "OMCSessionBase__,"
                ],
                indent=INDENT,
            ),
            "):"
        ]
    )

    code_class_element = CodeBlock(
        [],
        indent=INDENT,
    )
    code_class.append(code_class_element)

    code = CodeBlock(
        [
            "\n" * 1,
            code_import,
            "\n" * 2,
            code_class,
            "\n" * 1,
            (
                "open_session = functools__.partial"
                "(OMCSession__open__, OMCSession)"
            ),
        ]
    )

    variableTypes: typing.Set[profile.TypeWithSizes] = set()

    function_profiles = [
        profile.get_profile(root, functionName)
        for functionName in export_function_names(root)
    ]

    for function_profile in function_profiles:
        if (
            isinstance(function_profile, profile.AbstractFunctionProfile)
            and function_profile.supported
        ):
            code_class_element.extend(
                [
                    function_profile.generate_method_code(),
                    "",
                ]
            )
            if isinstance(
                function_profile,
                profile.FunctionDeclarationProfile
            ):
                variableTypes |= function_profile.variableTypes
        else:
            print(f"Skip {function_profile.name}")

    for typeProfile, sizes in variableTypes:
        print(typeProfile.name, sizes)

    code.dump(file)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    interface_parser = xml.XMLParser(schema=load_schema())
    root = xml.fromstring(args.input.read_bytes(), interface_parser)

    with args.output.open("w", encoding="utf-8") as file:
        write_module(file, root)


if __name__ == "__main__":
    main()
