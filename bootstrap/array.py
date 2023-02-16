import sys
from typing import IO

import click

from .ast_generator import array_stub_module
from .backport import unparse
from .util import countup

MAX_TYPE = 2
MAX_DIM = 2
MAX_SIZE = 8


@click.command
@click.option("-o", "--output", type=click.File("w"), default=sys.stdout)
@click.option("--max-type", type=int, default=MAX_TYPE)
@click.option("--max-dim", type=int, default=MAX_DIM)
@click.option("--max-size", type=int, default=MAX_SIZE)
def main(output: IO[str], max_dim: int, max_size: int, max_type: int) -> None:
    module = array_stub_module(
        types=countup(1, max_type),
        dims=countup(1, max_dim),
        sizes=countup(1, max_size),
    )
    output.write(unparse(module))


if __name__ == "__main__":
    main()
