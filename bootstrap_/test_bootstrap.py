import sys
from contextlib import ExitStack
from pathlib import Path
from subprocess import run
from tempfile import TemporaryDirectory

import pytest
from pkg_resources import resource_filename

from bootstrap_ import OutputFormat


@pytest.mark.parametrize(
    "output_format, output_suffix",
    [
        (OutputFormat.module, ".py"),
        (OutputFormat.xml, ".xml"),
    ],
)
@pytest.mark.parametrize("overwrite", [True, False])
def test_bootstrap(
    output_format: OutputFormat,
    output_suffix: str,
    overwrite: bool,
) -> None:
    xml = Path(
        resource_filename(__name__, "interface_xml/omc_interface.v_1_13_0.xml")
    )
    assert xml.exists()
    with ExitStack() as stack:
        enter = stack.enter_context
        directory = Path(enter(TemporaryDirectory()))
        run(
            [
                sys.executable,
                "-m",
                "bootstrap_",
                f"{xml}",  # input
                *("--input-type", "xml"),
                *("--output", f"{directory / f'output{output_suffix}'}"),
                *("--output-format", output_format.name),
                *(["--overwrite"] if overwrite else []),
            ],
            check=True,
        )


def test_array_stub() -> None:
    with ExitStack() as stack:
        enter = stack.enter_context
        directory = Path(enter(TemporaryDirectory()))
        array_pyi = directory / "array.pyi"

        bootstrap_cmd = [
            sys.executable,
            "-m",
            "bootstrap_.array",
            f"--output={array_pyi}",
        ]
        run(bootstrap_cmd, check=True)

        mypy_cmd = [
            sys.executable,
            "-m",
            "mypy",
            "--strict",
            "--ignore-missing-imports",
            f"{array_pyi.name}",
        ]
        run(mypy_cmd, check=True, cwd=directory)
