
import argparse
import contextlib
import enum
import inquirer  # type: ignore
from lxml import etree  # type: ignore
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


class OutputFormat(
    enum.Enum,
):
    module = enum.auto()
    xml = enum.auto()


def generate_omc_interface(
    inputPath: Path,
    inputType: InputType,
    outputFile: typing.BinaryIO,
    outputFormat: OutputFormat,
):
    if inputType is InputType.executable:
        with omc4py.compiler.InteractiveOMC.open(inputPath) as omc:
            omc_interface_xml = interface_xml.generate_omc_interface_xml(
                session.OMCSessionBootstrap(omc)
            )
    else:  # inputType is InputType.xml:
        omc_interface_xml = etree.parse(str(inputPath))

    interface_xml.validate_omc_interface_xml(omc_interface_xml)

    if outputFormat is OutputFormat.module:
        module_code = generate.create_module(omc_interface_xml)
        module_code.bdump(outputFile)
    else:  # outputFormat is OutputFormat.xml:
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


@contextlib.contextmanager
def open_by_output_args(
    output_str: str,
    outputFormat_hint: typing.Optional[OutputFormat],
    overwrite: typing.Optional[bool],
) -> typing.Iterator[typing.Tuple[typing.BinaryIO, OutputFormat]]:
    if output_str == '-':
        if outputFormat_hint is not None:
            yield sys.stdout.buffer, outputFormat_hint
        else:  # outputFormat_hint is None
            # default outputFormat is module
            yield sys.stdout.buffer, OutputFormat.module

    else:
        output = Path(output_str).resolve()
        outputFormat: OutputFormat

        if outputFormat_hint is not None:
            outputFormat = outputFormat_hint
            if outputFormat is OutputFormat.module and output.suffix != ".py":
                raise ValueError(
                    "--outputFormat=module, but output file suffix is not .py"
                    f", got {output_str!r}"
                )
            if outputFormat is OutputFormat.xml and output.suffix != ".xml":
                raise ValueError(
                    "--outputFormat=xml, but output file suffix is not .xml"
                    f", got {output_str!r}"
                )
        else:  # outputFormat_hint is None:
            if output.suffix == ".py":
                outputFormat = OutputFormat.module
            elif output.suffix == ".xml":
                outputFormat = OutputFormat.xml
            else:
                raise ValueError(
                    "output file suffix must be .py or .xml"
                    f", got {output_str!r}"
                )

        try:
            with output.open("xb") as outputFile:
                yield outputFile, outputFormat
        except FileExistsError:
            if overwrite is None:
                answer = inquirer.prompt(
                    [
                        inquirer.Confirm(
                            "overwrite",
                            message=f"Do you want to overwrite {output_str!r}?",
                        )
                    ]
                )
                if answer:
                    overwrite = answer["overwrite"]
                else:
                    overwrite = False

            if not overwrite:
                raise
            else:
                with output.open("wb") as outputFile:
                    yield outputFile, outputFormat


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
        default='-',
    )

    # # outputFormat
    # {module, xml}
    # default is None (select by `output`)
    parser.add_argument(
        "--outputFormat",
        choices=OutputFormat.__members__,
    )

    parser.add_argument(
        "--overwrite", action="store_true",
        default=None,
    )

    args = parser.parse_args()

    inputType_hint = (
        InputType[args.inputType]
        if args.inputType is not None
        else None
    )
    outputFormat_hint = (
        OutputFormat[args.outputFormat]
        if args.outputFormat is not None
        else None
    )

    inputPath, inputType = check_input_args(
        args.input,
        inputType_hint,
    )

    with open_by_output_args(
        args.output,
        outputFormat_hint,
        args.overwrite,
    ) as (outputFile, outputFormat):
        generate_omc_interface(
            inputPath, inputType,
            outputFile, outputFormat,
        )
