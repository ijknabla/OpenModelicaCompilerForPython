import sys
from ast import Module
from typing import IO

import click

from .backport import unparse


@click.command
@click.option("-o", "--output", type=click.File("w"), default=sys.stdout)
def main(output: IO[str]) -> None:
    module = Module(
        body=[],
        type_ignores=[],
    )
    output.write(unparse(module))


if __name__ == "__main__":
    main()
