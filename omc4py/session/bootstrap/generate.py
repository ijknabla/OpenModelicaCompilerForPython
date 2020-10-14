
import argparse
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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path)
    args = parser.parse_args()

    interface_parser = xml.XMLParser(schema=load_schema())
    xml.fromstring(args.input.read_bytes(), interface_parser)


if __name__ == "__main__":
    main()
