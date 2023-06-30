import enum
from pathlib import Path
from typing import Optional, Type

import click

from . import (
    InputType,
    OutputFormat,
    check_input_args,
    generate_omc_interface,
    open_by_output_args,
)


class EnumChoice(click.Choice):
    enum_type: Type[enum.Enum]

    def __init__(self, enum_type: Type[enum.Enum]):
        super().__init__([e.name for e in enum_type])
        self.enum_type = enum_type

    def convert(
        self,
        value: str,
        param: Optional[click.Parameter],
        ctx: Optional[click.Context],
    ) -> enum.Enum:
        return self.enum_type[super().convert(value, param, ctx)]


@click.command()
@click.argument(
    "input_path",
    metavar="INPUT",
    type=click.Path(exists=True, dir_okay=False, path_type=Path),
)
@click.option(
    "--input-type",
    type=EnumChoice(InputType),
    help="""\
if not specified, selected by INPUT
""",
)
@click.option(
    "--output",
    "output_path",
    type=click.Path(dir_okay=False, path_type=Path),
    help="""\
if not specified, output is stdout
""",
)
@click.option(
    "--output-format",
    type=EnumChoice(OutputFormat),
    help="""\
if not specified, selected by --output
""",
)
@click.option(
    "--overwrite",
    is_flag=True,
    show_default=True,
    default=False,
    help="""\
""",
)
def main(
    input_path: Path,
    input_type: Optional[InputType],
    output_path: Optional[Path],
    output_format: Optional[OutputFormat],
    overwrite: bool,
) -> None:
    """\
omc4py code generator

INPUT: omc executable or omc interface xml
    """
    inputPath, inputType = check_input_args(
        input_path,
        input_type,
    )

    with open_by_output_args(
        output_path,
        output_format,
        overwrite,
    ) as (outputFile, outputFormat):
        generate_omc_interface(
            inputPath,
            inputType,
            outputFile,
            outputFormat,
        )


if __name__ == "__main__":
    main()
