
import pkg_resources
from lxml import etree  # type: ignore

from ..session import OMCSessionBootstrap


def generate_omc_interface_xml(
    session: OMCSessionBootstrap
) -> etree._ElementTree:
    root = etree.Element(
        "omcInterface",
        {
            "omcVersion": session.getVersion()
        }
    )
    etree.SubElement(
        root,
        "classes"
    )

    return etree.ElementTree(root)


def load_schema(
) -> etree.XMLSchema:
    return etree.XMLSchema(
        etree.XML(
            pkg_resources.resource_string(
                __name__,
                "omc_interface.xsd",
            )
        )
    )
