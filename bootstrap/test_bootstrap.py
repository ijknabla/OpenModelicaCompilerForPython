import sys
from contextlib import ExitStack
from pathlib import Path
from subprocess import run
from tempfile import TemporaryDirectory

from pkg_resources import resource_filename


def test_bootstrap() -> None:
    xml = Path(
        resource_filename(__name__, "interface_xml/omc_interface.v_1_13_0.xml")
    )
    assert xml.exists()
    run([sys.executable, "-m", "bootstrap", f"{xml}"], check=True)


def test_array_stub() -> None:
    with ExitStack() as stack:
        enter = stack.enter_context
        directory = Path(enter(TemporaryDirectory()))
        array_pyi = directory / "array.pyi"

        bootstrap_cmd = [
            sys.executable,
            "-m",
            "bootstrap.array",
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
