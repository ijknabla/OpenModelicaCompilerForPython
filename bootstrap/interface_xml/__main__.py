
import argparse
import sys

from omc4py.compiler import InteractiveOMC

from ..session import OMCSessionBootstrap

from . import (
    generate_omc_interface_xml,
)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "input"
    )
    parser.add_argument(
        "--output",
    )

    args = parser.parse_args()

    with InteractiveOMC.open(args.input) as omc:
        omc_interface_xml = generate_omc_interface_xml(
            OMCSessionBootstrap(omc)
        )

    omc_interface_xml.write(
        sys.stdout.buffer,
        pretty_print=True,
        xml_declaration=True,
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
