import sys
from ast import Module
from typing import IO

import click

from .ast_generator import iter_import_froms
from .backport import unparse


@click.command
@click.option("-o", "--output", type=click.File("w"), default=sys.stdout)
def main(output: IO[str]) -> None:
    module = Module(
        body=[
            *iter_import_froms(
                [
                    ("__future__", ["annotations"]),
                    ("collections.abc", ["Sequence"]),
                    ("typing", ["Generic", "TypeVar", "Union", "overload"]),
                    ("typing_extensions", ["Literal"]),
                ]
            ),
        ],
        type_ignores=[],
    )
    output.write(unparse(module))


if __name__ == "__main__":
    main()
