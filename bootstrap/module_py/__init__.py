
from lxml import etree  # type: ignore

from ..code import CodeBlock


def generate_module_py(
    omc_interface_xml: etree._ElementTree,
) -> CodeBlock:
    return CodeBlock()
