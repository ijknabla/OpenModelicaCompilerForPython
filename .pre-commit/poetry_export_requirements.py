from subprocess import run
from typing import Iterable, Optional

import click


@click.command()
@click.argument("group", nargs=-1)
@click.option(
    "-o", "--output", type=click.types.Path(file_okay=True, dir_okay=False)
)
def main(group: Iterable[str], output: Optional[str]) -> None:
    groups = {"main"}
    groups.update(group)

    cmd = ["poetry", "export", "--without-hashes"]
    if output is not None:
        cmd += [f"--output={output}"]
    cmd.append("--only=" + ",".join(sorted(groups)))

    run(cmd, check=True)


if __name__ == "__main__":
    main()
