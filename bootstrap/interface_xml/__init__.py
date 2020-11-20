
__all__ = (
    "generate_omc_interface_xml",
    "validate_omc_interface_xml",
)

import functools
from lxml import etree  # type: ignore
import pkg_resources
import tqdm  # type: ignore
import typing

from omc4py.classes import (
    TypeName,
)

from ..session import (
    OMCSessionBootstrap,
)
from ..parser import (
    parse_alias,
    parse_enumerators,
    parse_variableHasDefault,
)


def generate_omc_interface_xml(
    session: OMCSessionBootstrap
) -> etree._ElementTree:

    root = generate_root_element(session)

    # Add <package id="OpenModelica"/> to root.classes
    package_OpenModelica = etree.SubElement(
        root.find("classes"),
        "package",
        {"id": "OpenModelica"},
    )
    etree.SubElement(
        package_OpenModelica,
        "classes"
    )

    classNames = session.getClassNames(
        TypeName("OpenModelica.Scripting"),
        recursive=True,
    )

    for className in tqdm.tqdm(classNames):
        assert(root.xpath(f'//*[@id="{className.parent!s}"]'))
        generate_class_element(session, package_OpenModelica, className)

    return etree.ElementTree(root)


def validate_omc_interface_xml(
    omc_interface: etree._ElementTree,
) -> None:
    load_omc_interface_schema().assertValid(
        omc_interface
    )


@functools.lru_cache(maxsize=1)
def load_omc_interface_schema(
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

    restriction = session.getClassRestrictionEnum(className)
    alias_optional = parse_alias(session.list(className, shortOnly=True))

    if alias_optional is not None:
        _, target = alias_optional
        return add_alias_element(
            session,
            parent_classes,
            className,
            restriction,
            target,
        )
    elif restriction is OMCSessionBootstrap.RestrictionEnum.type:
        return add_type_element(
            session,
            parent_classes,
            className,
        )
    elif restriction is OMCSessionBootstrap.RestrictionEnum.package:
        return add_package_element(
            session,
            parent_classes,
            className,
        )
    elif restriction is OMCSessionBootstrap.RestrictionEnum.record:
        return add_record_element(
            session,
            parent_classes,
            className,
        )
    elif restriction is OMCSessionBootstrap.RestrictionEnum.function:
        return add_function_element(
            session,
            parent_classes,
            className,
        )

    raise ValueError(
        f'Failed to find generate element function for {className}'
    )


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


def to_xml_boolean(
    value: bool,
) -> str:
    return "true" if value else "false"


def add_code_element(
    session: OMCSessionBootstrap,
    parent: etree._Element,
    className: TypeName,
    interfaceOnly: bool
) -> etree._Element:
    code_element = etree.SubElement(
        parent,
        "code",
        {
            "interfaceOnly": to_xml_boolean(interfaceOnly)
        }
    )
    code_element.text = session.list(
        className,
        interfaceOnly=interfaceOnly
    )

    return code_element


def add_dimensions_element(
    parent: etree._Element,
    dimensions: typing.Sequence[str]
) -> etree._Element:
    dimensions_element = etree.SubElement(
        parent,
        "dimensions",
    )
    for dimension in dimensions:
        etree.SubElement(
            dimensions_element,
            "dimension",
            {
                "size": dimension,
            },
        )

    return dimensions_element


def add_alias_element(
    session: OMCSessionBootstrap,
    parent_classes: etree._Element,
    className: TypeName,
    restriction: OMCSessionBootstrap.RestrictionEnum,
    rel_target: TypeName,
) -> etree._Element:
    for parent in className.parents:
        try:
            target = parent/rel_target
            if session.getClassRestrictionEnum(target) == restriction:
                break
        except ValueError:
            continue
    else:
        raise ValueError(
            "Can't resolve absolute className "
            f"of {rel_target} from {className}"
        )

    return etree.SubElement(
        parent_classes,
        restriction.name,
        {
            "id": str(className),
            "ref": str(target)
        },
    )


def add_type_element(
    session: OMCSessionBootstrap,
    parent_classes: etree._Element,
    className: TypeName,
) -> etree._Element:
    type_element = etree.SubElement(
        parent_classes,
        "type",
        {
            "id": str(className),
        },
    )

    etree.SubElement(
        type_element,
        "classes",
    )

    code_element = add_code_element(
        session,
        type_element,
        className,
        interfaceOnly=False,
    )

    enumerators = parse_enumerators(code_element.text)
    if not enumerators:
        raise ValueError(
            f"Modelica type {className} has no enumeration"
        )

    enumerators_element = etree.SubElement(
        etree.SubElement(
            type_element,
            "components",
        ),
        "enumerators",
    )
    for name, comment in enumerators:
        etree.SubElement(
            enumerators_element,
            "enumerator",
            {
                "name": str(name),
                "comment": comment,
            },
        )

    return type_element


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


def add_record_element(
    session: OMCSessionBootstrap,
    parent_classes: etree._Element,
    className: TypeName,
) -> etree._Element:
    record_element = etree.SubElement(
        parent_classes,
        "record",
        {
            "id": str(className),
        }
    )

    etree.SubElement(
        record_element,
        "classes"
    )

    add_code_element(
        session,
        record_element,
        className,
        interfaceOnly=False,
    )

    elements_element = etree.SubElement(
        etree.SubElement(
            record_element,
            "components",
        ),
        "elements",
    )
    for component in session.getComponents(className):
        element_element = etree.SubElement(
            elements_element,
            "element",
            {
                "className": str(component.className),
                "name": str(component.name),
                "comment": component.comment,
            }
        )
        add_dimensions_element(
            element_element,
            component.dimensions,
        )

    return record_element


def add_function_element(
    session: OMCSessionBootstrap,
    parent_classes: etree._Element,
    className: TypeName,
) -> etree._Element:
    function_element = etree.SubElement(
        parent_classes,
        "function",
        {
            "id": str(className),
        },
    )

    etree.SubElement(
        function_element,
        "classes",
    )

    code_element = add_code_element(
        session,
        function_element,
        className,
        interfaceOnly=True,
    )

    defaultValueDict = parse_variableHasDefault(
        code_element.text,
    )

    arguments_element = etree.SubElement(
        etree.SubElement(
            function_element,
            "components",
        ),
        "arguments",
    )
    for component in session.getComponents(className):
        if component.protected == "protected":
            continue

        hasDefault = defaultValueDict[component.name]

        argument_element = etree.SubElement(
            arguments_element,
            "argument",
            {
                "inputOutput": component.inputOutput,
                "className": str(component.className),
                "name": str(component.name),
                "hasDefault": to_xml_boolean(hasDefault),
                "comment": component.comment,
            }
        )
        add_dimensions_element(
            argument_element,
            component.dimensions,
        )

    return function_element
