
import abc
import argparse
import collections
import enum
from lxml import etree as xml  # type: ignore
from pathlib import Path
import re
import typing

from . import (
    load_schema,
)

from .. import types


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


class Indentation(enum.Enum):
    no_indent = enum.auto()
    indent = enum.auto()
    ignore_indent = enum.auto()


NO_INDENT = Indentation.no_indent
INDENT = Indentation.indent
IGNORE_INDENT = Indentation.ignore_indent


class CodeBlock(collections.UserList):
    indentString: typing.ClassVar[str] = " " * 4
    indent: Indentation

    def __init__(
        self,
        items: typing.Optional[typing.Iterable] = None,
        *,
        indent: Indentation = Indentation.no_indent
    ):
        super().__init__()
        if items is not None:
            self.extend(items)
        self.indent = indent

    def append(
        self,
        item,
    ) -> None:
        if isinstance(item, CodeBlock):
            super().append(item)
        else:
            item = str(item)
            if item:
                super().extend(item.splitlines())
            else:
                super().append("")

    def extend(
        self,
        items
    ) -> None:
        if isinstance(items, str):
            self.append(items)
        else:
            for item in items:
                self.append(item)

    def __repr__(
        self
    ) -> str:
        return (
            f"{type(self).__name__}("
            f"{super().__repr__()}, indent={self.indent!r}"
            f")"
        )

    def to_lines(
        self,
        indentLevel: int = 0,
    ) -> typing.Iterator[str]:
        currentIndent: int
        if self.indent is Indentation.no_indent:
            currentIndent = indentLevel
        elif self.indent is Indentation.indent:
            indentLevel += 1
            currentIndent = indentLevel
        elif self.indent is Indentation.ignore_indent:
            currentIndent = 0

        for elem in self:
            if isinstance(elem, CodeBlock):
                yield from elem.to_lines(indentLevel)
            else:
                yield self.indentString * currentIndent + elem + "\n"

    def dumps(
        self
    ):
        "".join(self.to_lines())

    def dump(
        self,
        file: typing.TextIO
    ) -> None:
        file.writelines(
            self.to_lines()
        )


def export_function_names(
    root: xml._Element,
) -> typing.Iterator[types.TypeName]:
    for element in root.xpath(
        '//package[@id="OpenModelica.Scripting"]/classes/function'
    ):
        yield types.TypeName(element.attrib["id"])


ProfileFactory = typing.Callable[[types.TypeName], "AbstractProfile"]


class AbstractProfile(
    abc.ABC
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


profile_classes: typing.List[typing.Type[AbstractProfile]] \
    = []


def register_profile(
    klass: typing.Type[AbstractProfile]
) -> typing.Type[AbstractProfile]:
    profile_classes.append(klass)
    return klass


def get_profile_factory(
    root: xml._Element,
    cache: typing.Dict[types.TypeName, AbstractProfile],
) -> ProfileFactory:
    def factory(
        className: types.TypeName
    ) -> AbstractProfile:
        if className not in cache:
            element, = root.xpath(f'//*[@id="{className!s}"]')
            for ProfileClass in profile_classes:
                if ProfileClass.check_element(element):
                    profile = ProfileClass(element, factory)
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
        for dimension in dimensions.xpath("//dimension"):
            size = dimension.attrib["size"]
            if size == ":":
                yield 0
            else:
                yield int(size)
    return tuple(size_generator())


class InputArgument(
    typing.NamedTuple,
):
    class_: types.TypeName
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


@register_profile
class FunctionProfile(
    AbstractProfile,
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
            for argument in self.element.xpath(".//argument")
        )

    @property
    def supported(
        self,
    ) -> bool:
        return self.variableTypes <= supportedTypes

    def to_codeBlock(
        self,
    ) -> CodeBlock:
        py_funcName = str(self.name.parts[-1])
        assert(py_funcName.isidentifier())
        return CodeBlock(
            [
                f"def {py_funcName}(",
                CodeBlock(
                    [
                        "self,"
                    ],
                    indent=INDENT
                ),
                "):",
                CodeBlock(
                    [
                        "..."
                    ],
                    indent=INDENT
                )
            ]
        )


@register_profile
class FunctionAliasProfile(
    AbstractProfile
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
from omc4py.session import OMCSessionBase as __OMCSessionBase\
""")

    code_class = CodeBlock(
        [
            "class OMCSession(",
            CodeBlock(
                [
                    "__OMCSessionBase,"
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
        ]
    )

    cache: typing.Dict[types.TypeName, AbstractProfile] = {}
    profile_factory = get_profile_factory(root, cache)

    function_profiles = [
        profile_factory(functionName)
        for functionName in export_function_names(root)
    ]

    for profile in function_profiles:
        if not isinstance(profile, FunctionProfile):
            continue
        if profile.supported:
            code_class_element.extend(
                [
                    profile.to_codeBlock(),
                    "",
                ]
            )

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
