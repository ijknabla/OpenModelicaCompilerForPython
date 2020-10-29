
import argparse
import enum
from lxml import etree  # type: ignore
import os
from pathlib import Path
import shutil
import sys
import typing

import omc4py.compiler

from . import (
    interface_xml,
    generate,
    session,
)


class InputType(
    enum.Enum,
):
    executable = enum.auto()
    xml = enum.auto()


class OutputType(
    enum.Enum,
):
    module = enum.auto()
    xml = enum.auto()


def generate_omc_interface(
    inputPath: Path,
    inputType: InputType,
    outputFile: typing.BinaryIO,
    outputType: OutputType,
):
    if inputType is InputType.executable:
        with omc4py.compiler.InteractiveOMC.open(inputPath) as omc:
            omc_interface_xml = interface_xml.generate_omc_interface_xml(
                session.OMCSessionBootstrap(omc)
            )
    else:  # inputType is InputType.xml:
        omc_interface_xml = etree.parse(str(inputPath))

    schema = interface_xml.load_schema()
    schema.assertValid(omc_interface_xml)

    if outputType is OutputType.module:
        module_code = generate.create_module(omc_interface_xml)
        module_code.bdump(outputFile)
    else:  # outputType is OutputType.xml:
        omc_interface_xml.write(
            outputFile,
            pretty_print=True,
            xml_declaration=True,
            encoding="utf-8",
        )


def check_input_args(
    input_str: str,
    inputType_hint: typing.Optional[InputType]
) -> typing.Tuple[Path, InputType]:
    if inputType_hint is None:
        if Path(input_str).suffix == ".xml":
            return check_input_args(input_str, InputType.xml)
        else:
            return check_input_args(input_str, InputType.executable)

    elif inputType_hint is InputType.executable:
        executable = shutil.which(input_str)
        if executable is None:
            raise ValueError(
                f"Can't find executable for {input_str!r}"
            )
        return Path(executable), InputType.executable

    elif inputType_hint is InputType.xml:
        absPath = Path(input_str).resolve()
        if not absPath.exists():
            raise FileNotFoundError(
                f"{input_str!r} does not exists!"
            )
        if absPath.suffix != ".xml":
            raise ValueError(
                f"input must be xml, got {input_str!r}"
            )
        return absPath, InputType.xml


def check_output_args(
    output_optional: typing.Optional[typing.BinaryIO],
    outputType_hint: typing.Optional[OutputType],
) -> typing.Tuple[typing.BinaryIO, OutputType]:
    if output_optional is None:
        binary_stdout = sys.stdout.buffer
        if outputType_hint is None:
            return binary_stdout, OutputType.module
        else:
            return binary_stdout, outputType_hint

    output: typing.BinaryIO = output_optional
    path = Path(output.name)

    def close_output():
        output.close()
        os.remove(path)

    if outputType_hint is None:
        if path.suffix == ".py":
            return output, OutputType.module
        elif path.suffix == ".xml":
            return output, OutputType.xml
        else:
            close_output()
            raise ValueError(
                "output file suffix must be .py or .xml"
                f", got {output.name!r}"
            )

    outputType: OutputType = outputType_hint

    if outputType is OutputType.module and path.suffix != ".py":
        close_output()
        raise ValueError(
            "--outputType=module, but output file suffix is not .py"
            f", got {output.name!r}"
        )
    if outputType is OutputType.xml and path.suffix != ".xml":
        close_output()
        raise ValueError(
            "--outputType=xml, but output file suffix is not .xml"
            f", got {output.name!r}"
        )

    return output, outputType


def main():
    """\
Refactored main
    """
    parser = argparse.ArgumentParser(
        prog="omc4py bootstrap",
    )

    # # input
    # omc executable or omc interface xml
    parser.add_argument(
        "input",
    )

    # # inputType
    # {executable, xml}
    # default is None (selected by `input`)
    parser.add_argument(
        "--inputType",
        choices=InputType.__members__,
    )

    # # output
    # default is stdout, (generate python module)
    parser.add_argument(
        "-o", "--output",
        type=argparse.FileType("xb"),
    )

    # # outputType
    # {module, xml}
    # default is None (select by `output`)
    parser.add_argument(
        "--outputType",
        choices=OutputType.__members__,
    )

    args = parser.parse_args()

    inputPath, inputType = check_input_args(
        args.input,
        None if args.inputType is None else InputType[args.inputType],
    )
    outputFile, outputType = check_output_args(
        args.output,
        None if args.outputType is None else OutputType[args.outputType],
    )

    generate_omc_interface(
        inputPath, inputType,
        outputFile, outputType,
    )
