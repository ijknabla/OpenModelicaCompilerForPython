import sys
from ast import Module
from typing import IO

import click

from .ast_generator import iter_import_froms
from .backport import unparse
from .util import countup


@click.command
@click.option("-o", "--output", type=click.File("w"), default=sys.stdout)
@click.option("--max-dim", type=int, required=True)
@click.option("--max-size", type=int, required=True)
def main(output: IO[str], max_dim: int, max_size: int) -> None:
    countup(1, max_dim)
    countup(1, max_size)
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
