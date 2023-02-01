import sys
from pathlib import Path
from subprocess import run

from pkg_resources import resource_filename


def test_bootstrap() -> None:
    xml = Path(
        resource_filename(__name__, "interface_xml/omc_interface.v_1_13_0.xml")
    )
    assert xml.exists()
    run([sys.executable, "-m", "bootstrap", f"{xml}"], check=True)
