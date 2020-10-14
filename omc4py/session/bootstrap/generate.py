
import argparse
from lxml import etree as xml
from pathlib import Path

from . import (
    load_schema
)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path)
    args = parser.parse_args()

    interface_parser = xml.XMLParser(schema=load_schema())
    xml.fromstring(args.input.read_bytes(), interface_parser)


if __name__ == "__main__":
    main()
