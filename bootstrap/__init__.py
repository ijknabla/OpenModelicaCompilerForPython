import contextlib
import enum
import shutil
import sys
import typing
from pathlib import Path
from typing import Optional

import inquirer  # type: ignore
from lxml import etree  # type: ignore

from omc4py.session import open_session

from . import interface_xml, module_py
from .session import OMCSessionBootstrap


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
) -> None:
    if inputType is InputType.executable:
        with open_session(
            inputPath,
            session_type=OMCSessionBootstrap,
        ) as session:
            omc_interface_xml = interface_xml.generate_omc_interface_xml(
                typing.cast(OMCSessionBootstrap, session)
            )
    else:  # inputType is InputType.xml:
        omc_interface_xml = etree.parse(str(inputPath))

    interface_xml.validate_omc_interface_xml(omc_interface_xml)

    if outputFormat is OutputFormat.module:
        module_code = module_py.generate_module_py(omc_interface_xml)
        module_code.bdump(outputFile)
    else:  # outputFormat is OutputFormat.xml:
        omc_interface_xml.write(
            outputFile,
            pretty_print=True,
            xml_declaration=True,
            encoding="utf-8",
        )


def check_input_args(
    input_path: Path, inputType_hint: typing.Optional[InputType]
) -> typing.Tuple[Path, InputType]:
    if inputType_hint is None:
        if input_path.suffix == ".xml":
            return check_input_args(input_path, InputType.xml)
        else:
            return check_input_args(input_path, InputType.executable)

    elif inputType_hint is InputType.executable:
        executable = shutil.which(input_path)
        if executable is None:
            raise ValueError(f"Can't find executable for {input_path!r}")
        return Path(executable), InputType.executable

    elif inputType_hint is InputType.xml:
        absPath = input_path.resolve()
        if not absPath.exists():
            raise FileNotFoundError(f"{input_path!r} does not exists!")
        if absPath.suffix != ".xml":
            raise ValueError(f"input must be xml, got {input_path!r}")
        return absPath, InputType.xml


@contextlib.contextmanager
def open_by_output_args(
    output_path: Optional[Path],
    outputFormat_hint: typing.Optional[OutputFormat],
    overwrite: typing.Optional[bool],
) -> typing.Iterator[typing.Tuple[typing.BinaryIO, OutputFormat]]:
    if output_path is None:
        if outputFormat_hint is not None:
            yield sys.stdout.buffer, outputFormat_hint
        else:  # outputFormat_hint is None
            # default outputFormat is module
            yield sys.stdout.buffer, OutputFormat.module

    else:
        output = Path(output_path).resolve()
        outputFormat: OutputFormat

        if outputFormat_hint is not None:
            outputFormat = outputFormat_hint
            if outputFormat is OutputFormat.module and output.suffix != ".py":
                raise ValueError(
                    "--outputFormat=module, but output file suffix is not .py"
                    f", got {output_path!r}"
                )
            if outputFormat is OutputFormat.xml and output.suffix != ".xml":
                raise ValueError(
                    "--outputFormat=xml, but output file suffix is not .xml"
                    f", got {output_path!r}"
                )
        else:  # outputFormat_hint is None:
            if output.suffix == ".py":
                outputFormat = OutputFormat.module
            elif output.suffix == ".xml":
                outputFormat = OutputFormat.xml
            else:
                raise ValueError(
                    "output file suffix must be .py or .xml"
                    f", got {output_path!r}"
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
                            message=(
                                f"Do you want to overwrite {output_path!r}?"
                            ),
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
