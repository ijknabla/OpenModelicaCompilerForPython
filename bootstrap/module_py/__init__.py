
from lxml import etree  # type: ignore

from .code import Code


def generate_module_py(
    omc_interface_xml: etree._ElementTree,
) -> Code:
    return Code()
