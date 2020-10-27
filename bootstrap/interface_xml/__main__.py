
import argparse

from omc4py.compiler import InteractiveOMC

from ..session import OMCSessionBootstrap

from . import (
    generate_interface_xml,
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
        interface_xml = generate_interface_xml(
            OMCSessionBootstrap(omc)
        )


if __name__ == "__main__":
    main()
