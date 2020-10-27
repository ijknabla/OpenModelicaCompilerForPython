
import pkg_resources
from lxml import etree as xml  # type: ignore


def load_schema(
) -> xml.XMLSchema:
    return xml.XMLSchema(
        xml.XML(
            pkg_resources.resource_string(
                __name__,
                "omc_interface.xsd",
            )
        )
    )
