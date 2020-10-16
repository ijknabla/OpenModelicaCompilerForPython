
import argparse
from lxml import etree as xml  # type: ignore
from pathlib import Path
import re
import typing

from . import (
    load_schema,
    profile,
)

from .code import (
    INDENT,
    CodeBlock,
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


def export_function_names(
    root: xml._Element,
) -> typing.Iterator[types.TypeName]:
    for element in root.xpath(
        '//package[@id="OpenModelica.Scripting"]/classes/function'
    ):
        yield types.TypeName(element.attrib["id"])


def write_module(
    file: typing.TextIO,
    root: xml._Element,
) -> None:
    code_import = CodeBlock("""\
import builtins as builtins__
import functools as functools__
from omc4py.session import OMCSessionBase as OMCSessionBase__
from omc4py.session import OMCSession__open as OMCSession__open__
from omc4py.session import OMCSession__call as OMCSession__call__
from omc4py.session import OMCSession__close as close_session
from omc4py.session import types as types__
""")

    code_class = CodeBlock(
        "class OMCSession(",
        CodeBlock(
            "OMCSessionBase__,",
            indent=INDENT,
        ),
        "):"
    )

    code_class_element = CodeBlock(
        indent=INDENT,
    )
    code_class.append(code_class_element)

    code = CodeBlock(
        "\n" * 1,
        code_import,
        "\n" * 2,
        code_class,
        "\n" * 1,
        (
            "open_session = functools__.partial"
            "(OMCSession__open__, OMCSession)"
        ),
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
