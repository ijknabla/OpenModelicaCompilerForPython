
import pkg_resources
from lxml import etree  # type: ignore

from ..session import OMCSessionBootstrap


def generate_interface_xml(
    session: OMCSessionBootstrap
) -> etree._ElementTree:
    pass


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
