
import argparse
import collections
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


class CodeBlock(collections.UserList):
    indentString: typing.ClassVar[str] = " " * 4
    indentLevel: typing.Optional[int]

    def __init__(
        self,
        items,
        *,
        indentLevel: typing.Optional[int] = 0,
    ):
        super().__init__()
        self.extend(items)
        self.indentLevel = indentLevel

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
        for item in items:
            self.append(item)

    def __repr__(
        self
    ) -> str:
        return (
            f"{type(self).__name__}("
            f"{super().__repr__()}, indent={self.indentLevel!r}"
            f")"
        )

    def to_lines(
        self,
        indentLevel: int = 0,
    ) -> typing.Iterator[str]:
        if self.indentLevel is None:
            currentIndent = 0
        else:
            indentLevel += self.indentLevel
            currentIndent = indentLevel

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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path)
    args = parser.parse_args()

    interface_parser = xml.XMLParser(schema=load_schema())
    xml.fromstring(args.input.read_bytes(), interface_parser)


if __name__ == "__main__":
    main()
