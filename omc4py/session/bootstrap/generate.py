
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


def encode_typeName(
    typeName: types.TypeName,
    encoding: str = "utf-8",
) -> str:
    pattern = re.compile(r"[0-9A-Za-z]")

    def characters(
    ) -> typing.Iterator[str]:
        for char in str(typeName):
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
IGNORE_INDENT = Indentation.no_indent


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
    @classmethod
    @abc.abstractmethod
    def create(
        cls,
        element: xml._Element,
        factory: ProfileFactory,
    ) -> "AbstractProfile":
        raise NotImplementedError()


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
                try:
                    profile = ProfileClass.create(element, factory)
                    break
                except ValueError:
                    continue
            else:
                raise ValueError(
                    f"Failed to create profile for {className}"
                )
            cache[className] = profile
        return cache[className]

    return factory


@register_profile
class FunctionProfile(
    AbstractProfile,
):
    @classmethod
    def create(
        cls,
        element: xml._Element,
        factory: ProfileFactory
    ) -> AbstractProfile:
        if not(
            element.tag == "function"
            and "ref" not in element.attrib
        ):
            raise ValueError()

        return FunctionProfile()


@register_profile
class FunctionAliasProfile(
    AbstractProfile
):
    @classmethod
    def create(
        cls,
        element: xml._Element,
        factory: ProfileFactory
    ) -> AbstractProfile:
        if not(
            element.tag == "function"
            and "ref" in element.attrib
        ):
            raise ValueError()

        return FunctionAliasProfile()


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

    code_class_element.append("...")

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
