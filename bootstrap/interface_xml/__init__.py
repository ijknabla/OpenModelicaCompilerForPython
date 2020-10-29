
import enum
from lxml import etree  # type: ignore
import pkg_resources
import tqdm
import typing

from omc4py.types import (
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


class Restriction(
    enum.Enum,
):
    type = enum.auto()
    package = enum.auto()
    record = enum.auto()
    function = enum.auto()


def getRestriction(
    session: OMCSessionBootstrap,
    className: TypeName,
) -> Restriction:
    if session.isType(className):
        return Restriction.type
    elif session.isPackage(className):
        return Restriction.package
    elif session.isRecord(className):
        return Restriction.record
    elif session.isFunction(className):
        return Restriction.function
    else:
        raise ValueError(
            f"Can't determine restriction of {className}"
        )


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

    restriction = getRestriction(session, className)
    full_code = session.list(className)
    alias_optional = parse_alias(full_code)

    if alias_optional is not None:
        _, target = alias_optional
        return add_alias_element(
            session,
            parent_classes,
            className,
            restriction,
            target,
        )
    elif restriction is Restriction.type:
        return add_type_element(
            session,
            parent_classes,
            className,
            full_code,
        )
    elif restriction is Restriction.package:
        return add_package_element(
            session,
            parent_classes,
            className,
        )
    elif restriction is Restriction.record:
        return add_record_element(
            session,
            parent_classes,
            className,
            full_code,
        )
    elif restriction is Restriction.function:
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


def add_alias_element(
    session: OMCSessionBootstrap,
    parent_classes: etree._Element,
    className: TypeName,
    restriction: Restriction,
    rel_target: TypeName,
) -> etree._Element:
    for parent in className.parents:
        try:
            target = parent/rel_target
            if getRestriction(session, target) == restriction:
                break
        except ValueError:
            continue
    else:
        raise RuntimeError(
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
    full_code: str,
) -> etree._Element:
    enumerators = parse_enumerators(full_code)
    if not enumerators:
        raise ValueError(
            f"Modelica type {className} has no enumeration"
        )

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

    code_element = etree.SubElement(
        type_element,
        "code",
        {
            "interfaceOnly": "false"
        }
    )
    code_element.text = full_code

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


def add_dimensions_element(
    parent: etree._Element,
    dimensions: typing.Sequence[str]
):
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


def add_record_element(
    session: OMCSessionBootstrap,
    parent_classes: etree._Element,
    className: TypeName,
    full_code: str,
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

    code_element = etree.SubElement(
        record_element,
        "code",
        {
            "interfaceOnly": "false",
        }
    )
    code_element.text = full_code

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

    code_interfaceOnly = session.list(
        className,
        interfaceOnly=True,
    )
    defaultValueDict = parse_variableHasDefault(
        code_interfaceOnly,
    )

    code_element = etree.SubElement(
        function_element,
        "code",
        {
            "interfaceOnly": "true",
        }
    )
    code_element.text = code_interfaceOnly

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


def to_xml_boolean(
    value: bool,
) -> str:
    return "true" if value else "false"
