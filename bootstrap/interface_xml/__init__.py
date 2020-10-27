
from lxml import etree  # type: ignore
import pkg_resources
import tqdm

from omc4py.types import (
    TypeName,
)

from ..session import OMCSessionBootstrap


def generate_omc_interface_xml(
    session: OMCSessionBootstrap
) -> etree._ElementTree:

    root = generate_root_element(session)

    classNames = session.getClassNames(
        TypeName("OpenModelica.Scripting"),
        recursive=True,
    )

    for i, className in enumerate(tqdm.tqdm(classNames)):
        assert(i == 0 or className.parent in classNames[:i])
        generate_class_element(session, root, className)

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


def generate_root_element(
    session: OMCSessionBootstrap,
) -> etree._Element:
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
    return root


def generate_class_element(
    session: OMCSessionBootstrap,
    root: etree._Element,
    className: TypeName,
) -> etree._Element:
    parent_classes = find_parent_classes(
        session,
        root,
        className
    )

    if session.isPackage(className):
        return add_package_element(
            session,
            parent_classes,
            className,
        )

    element = etree.SubElement(
        parent_classes,
        "class",
        {"id": str(className)}
    )
    etree.SubElement(
        element,
        "classes",
    )

    return element


def find_parent_classes(
    session: OMCSessionBootstrap,
    root: etree._Element,
    className: TypeName,
) -> etree._Element:
    classes_optional = root.xpath(
        f'//*[@id="{className.parent}"]/classes'
    )

    if classes_optional:
        classes, = classes_optional
    else:
        classes = root.find("classes")

    return classes


def add_package_element(
    session: OMCSessionBootstrap,
    parent_classes: etree._Element,
    className: TypeName,
) -> etree._Element:
    package_element = etree.SubElement(
        parent_classes,
        "package",
        {"id": str(className)},
    )
    etree.SubElement(
        package_element,
        "classes"
    )
    return package_element
