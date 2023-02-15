import sys
from ast import Module
from typing import IO

import click

from .ast_generator import iter_import_froms, iter_ndarray_type_vars
from .backport import unparse
from .util import countup


@click.command
@click.option("-o", "--output", type=click.File("w"), default=sys.stdout)
@click.option("--max-dim", type=int, required=True)
@click.option("--max-size", type=int, required=True)
def main(output: IO[str], max_dim: int, max_size: int) -> None:
    dims = countup(1, max_dim)
    sizes = countup(1, max_size)
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
            *iter_ndarray_type_vars(dims=dims, sizes=sizes),
        ],
        type_ignores=[],
    )
    output.write(unparse(module))


if __name__ == "__main__":
    main()
