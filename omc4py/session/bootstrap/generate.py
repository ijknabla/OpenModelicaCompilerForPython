
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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path)
    args = parser.parse_args()

    interface_parser = xml.XMLParser(schema=load_schema())
    xml.fromstring(args.input.read_bytes(), interface_parser)


if __name__ == "__main__":
    main()
