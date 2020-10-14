
import abc
import argparse
import arpeggio  # type: ignore
import enum
from lxml import etree as xml
from pathlib import Path
import pkg_resources
import sys
import typing
import warnings

from . import (
    StrOrPathLike,
    InteractiveOMC,
    exception,
    parse_omc_value,
    parser,
    string,
    types,
    visitor,
)


def parse_defaultValueInfoDict(
    interface: str
) -> typing.Dict[types.Identifier, typing.Optional[str]]:
    return dict(
        arpeggio.visit_parse_tree(
            parser.stored_definition_parser.parse(interface),
            visitor.DefaultValueInfoVisitor(),
        )
    )


def parse_enumerator(
    code: str
) -> typing.Tuple[types.Identifier]:
    return arpeggio.visit_parse_tree(
        parser.stored_definition_parser.parse(code),
        visitor.EnumeratorVisitor(),
    )


def call_optional(
    func: typing.Callable,
    obj: typing.Optional[typing.Any],
):
    if obj is None:
        return None
    else:
        return func(obj)


class Component(
    typing.NamedTuple
):
    """
OpenModelica.Scripting.getComponentsTest.Component
"""
    className: str
    name: str
    comment: str
    isProtected: bool
    isFinal: bool
    isFlow: bool
    isStream: bool
    isReplaceable: bool
    variability: str
    innerOuter: str
    inputOutput: str
    dimensions: typing.List[str]


def open_omc_session(
    omc_command: typing.Optional[StrOrPathLike] = None,
) -> "OMCSession":
    self = OMCSession()
    self._omc = InteractiveOMC.open(
        omc_command=omc_command,
    )
    return self


def close_omc_session(
    session: "OMCSession"
):
    session._omc.close()


class OMCSession(
):
    _omc: InteractiveOMC

    def __enter__(
        self
    ):
        return self

    def __exit__(
        self,
        exc_type,
        exc_value,
        traceback,
    ):
        close_omc_session(self)
        return False

    def _call(
        self,
        funcName: str,
        args: typing.List[typing.Any],
        kwrds: typing.Dict[str, typing.Optional[typing.Any]],
        check: bool = True
    ) -> typing.Any:
        argument_literals: typing.List[str] = []
        for arg in args:
            argument_literals.append(
                string.to_omc_literal(arg)
            )
        for ident, value in kwrds.items():
            if value is None:
                continue
            value_literal = string.to_omc_literal(
                value
            )
            argument_literals.append(
                f"{ident}={value_literal}"
            )

        arguments_literal = ", ".join(argument_literals)

        result_literal = self._omc.execute(
            f"{funcName}({arguments_literal})"
        )

        error = exception.find_omc_error(self._omc)

        if check and error is not None:
            if isinstance(error, exception.OMCWarning):
                warnings.warn(error)
            else:
                raise error

        return parse_omc_value(result_literal)

    def getVersion(
        self,
        cl: typing.Optional[types.TypeName] = None,
    ) -> str:
        return self._call(
            "getVersion",
            [],
            {
                "cl": call_optional(types.TypeName, cl),
            },
        )

    def getClassRestriction(
        self,
        cl: types.TypeName,
    ) -> str:
        return self._call(
            "getClassRestriction",
            [],
            {
                "cl": types.TypeName(cl),
            },
        )

    def list(
        self,
        class_: typing.Optional[types.TypeName] = None,
        interfaceOnly: typing.Optional[bool] = None,
        shortOnly: typing.Optional[bool] = None,
    ) -> str:
        return self._call(
            "list",
            [],
            {
                "class_": call_optional(types.TypeName, class_),
                "interfaceOnly": call_optional(bool, interfaceOnly),
                "shortOnly": call_optional(bool, shortOnly),
            },
        )

    def getClassNames(
        self,
        class_: typing.Optional[types.TypeName] = None,
        recursive: typing.Optional[bool] = None,
        qualified: typing.Optional[bool] = None,
        sort: typing.Optional[bool] = None,
        builtin: typing.Optional[bool] = None,
        showProtected: typing.Optional[bool] = None,
        includeConstants: typing.Optional[bool] = None,
    ) -> typing.List[types.TypeName]:
        result = self._call(
            "getClassNames",
            [],
            {
                "class_": call_optional(types.TypeName, class_),
                "recursive": call_optional(bool, recursive),
                "qualified": call_optional(bool, qualified),
                "sort": call_optional(bool, sort),
                "builtin": call_optional(bool, builtin),
                "showProtected": call_optional(bool, showProtected),
                "includeConstants": call_optional(bool, includeConstants),
            },
        )

        return list(map(types.TypeName, result))

    def getComponentsTest(
        self,
        name: types.TypeName,
    ) -> typing.List[Component]:
        result = self._call(
            "getComponentsTest",
            [
                types.TypeName(name)
            ],
            {},
        )
        return [
            Component(**record_literal)
            for record_literal in result
        ]


class ClassRestriction(
    enum.Enum,
):
    package = "package"
    type = "type"
    record = "record"
    function = "function"

    @classmethod
    def from_typeName(
        cls,
        session: OMCSession,
        typeName: types.TypeName,
    ) -> "ClassRestriction":
        raw_restriction = session.getClassRestriction(
            typeName
        )
        return cls(
            raw_restriction.split()[-1]
        )


def generate_class_elem(
    session: OMCSession,
    parent: xml.Element,
    className: types.TypeName,
) -> None:
    restriction = ClassRestriction.from_typeName(
        session, className
    )

    class_tag = xml.SubElement(
        parent,
        restriction.value,
        {
            "id": str(className),
        },
    )

    def generate_code_tag(
    ) -> typing.Optional[xml.Element]:
        if restriction is ClassRestriction.package:
            return None

        interfaceOnly: bool
        if restriction is ClassRestriction.function:
            interfaceOnly = True
        else:
            interfaceOnly = False

        code_tag = xml.SubElement(
            class_tag,
            "code",
            {
                "interfaceOnly":
                    "true" if interfaceOnly else "false"
            },
        )
        code_tag.text = session.list(className, interfaceOnly=interfaceOnly)

        return code_tag

    def generate_type_components_tag(
    ) -> xml.Element:
        components_tag = xml.SubElement(
            class_tag,
            "components",
        )

        enumeration_tag = xml.SubElement(
            components_tag,
            "enumerators",
        )

        enumeration = parse_enumerator(
            session.list(className)
        )

        for name, comment in enumeration:
            xml.SubElement(
                enumeration_tag,
                "enumerator",
                {
                    "name": str(name),
                    "comment": comment,
                }
            )

        return components_tag

    def generate_record_elem(
    ) -> xml.Element:
        components_elem = xml.SubElement(
            class_tag,
            "components",
        )

        elements_elem = xml.SubElement(
            components_elem,
            "elements",
        )

        for component in session.getComponentsTest(className):
            element_elem = xml.SubElement(
                elements_elem,
                "element",
                {
                    "className": str(component.className),
                    "name": str(component.name),
                    "comment": component.comment
                }
            )
            dimensions_elem = xml.SubElement(
                element_elem,
                "dimensions"
            )
            for dimension in component.dimensions:
                xml.SubElement(
                    dimensions_elem,
                    "dimension",
                    {
                        "size": dimension,
                    }
                )

        return components_elem

    def generate_function_components_tag(
    ) -> xml.Element:
        components_elem = xml.SubElement(
            class_tag,
            "components",
        )

        arguments_elem = xml.SubElement(
            components_elem,
            "arguments"
        )

        defaultValueInfoDict = parse_defaultValueInfoDict(
            session.list(className, interfaceOnly=True),
        )

        for component in session.getComponentsTest(className):
            if component.isProtected:
                continue
            hasDefault = defaultValueInfoDict[
                types.Identifier(component.name)
            ]
            argument_elem = xml.SubElement(
                arguments_elem,
                "argument",
                {
                    "inputOutput": component.inputOutput,
                    "className": str(component.className),
                    "name": str(component.name),
                    "hasDefault": "true" if hasDefault else "false",
                    "comment": component.comment,
                }
            )
            dimensions_elem = xml.SubElement(
                argument_elem,
                "dimensions"
            )
            for dimension in component.dimensions:
                xml.SubElement(
                    dimensions_elem,
                    "dimension",
                    {
                        "size": dimension
                    }
                )

        return components_elem

    def generate_classes_tag(
    ) -> xml.Element:
        classes_tag = xml.SubElement(
            class_tag,
            "classes",
        )

        for ident in session.getClassNames(className):
            subClassName = className / ident
            generate_class_elem(
                session,
                classes_tag,
                subClassName,
            )
        return classes_tag

    generate_classes_tag()
    generate_code_tag()
    if restriction is ClassRestriction.type:
        generate_type_components_tag()
    elif restriction is ClassRestriction.record:
        generate_record_elem()
    elif restriction is ClassRestriction.function:
        generate_function_components_tag()

    return parent


def generate_omc_interface_xml(
    session: OMCSession,
) -> xml.ElementTree:
    class ModelicaClass(
        abc.ABC
    ):
        restriction: typing.ClassVar[str]
        element: xml.Element

        def __init__(
            self,
            typeName: types.TypeName,
        ):
            self.element = xml.Element(
                self.restriction,
                {"id": str(typeName)}
            )

        @abc.abstractclassmethod
        def generate_element(
            self
        ) -> None:
            ...

        @property
        def name(
            self,
        ) -> types.TypeName:
            return types.TypeName(
                self.element.attrib["id"]
            )

        @property
        def code(
            self
        ) -> str:
            code_element = self.element.find("code")
            if code_element is not None:
                return code_element.text
            else:
                return session.list(self.name)

        def generate_classes_element(
            self,
        ) -> None:
            xml.SubElement(self.element, "classes")

        def generate_code_element(
            self,
            interfaceOnly: bool,
        ) -> None:
            code_element = xml.SubElement(
                self.element,
                "code",
                {
                    "interfaceOnly": "true" if interfaceOnly else "false",
                },
            )
            code_element.text = session.list(
                self.name, interfaceOnly=interfaceOnly,
            )

        def generate_dimensions_element(
            self,
            parent: xml.Element,
            dimensions: typing.Sequence[str],
        ) -> None:
            dimensions_element = xml.SubElement(
                parent,
                "dimensions"
            )
            for dimension in dimensions:
                xml.SubElement(
                    dimensions_element,
                    "dimension",
                    {
                        "size": dimension,
                    }
                )

    class ModelicaPackage(ModelicaClass):
        restriction = "package"

        def generate_element(
            self
        ) -> None:
            self.generate_classes_element()

    class ModelicaType(ModelicaClass):
        restriction = "type"

        def generate_element(
            self
        ) -> None:
            self.generate_classes_element()
            self.generate_code_element(interfaceOnly=False)
            self.generate_components_element()

        def generate_components_element(
            self,
        ) -> None:
            enumerators_element = xml.SubElement(
                xml.SubElement(
                    self.element,
                    "components",
                ),
                "enumerators",
            )

            for name, comment in parse_enumerator(self.code):
                xml.SubElement(
                    enumerators_element,
                    "enumerator",
                    {
                        "name": str(name),
                        "comment": comment,
                    }
                )

    class ModelicaRecord(ModelicaClass):
        restriction = "record"

        def generate_element(
            self
        ) -> None:
            self.generate_classes_element()
            self.generate_code_element(interfaceOnly=False)
            self.generate_components_element()

        def generate_components_element(
            self,
        ) -> None:
            elements_element = xml.SubElement(
                xml.SubElement(
                    self.element,
                    "components",
                ),
                "elements",
            )

            for component in session.getComponentsTest(self.name):
                element_element = xml.SubElement(
                    elements_element,
                    "element",
                    {
                        "className": str(component.className),
                        "name": str(component.name),
                        "comment": component.comment
                    }
                )
                self.generate_dimensions_element(
                    element_element,
                    component.dimensions,
                )

    class ModelicaFunction(ModelicaClass):
        restriction = "function"

        def generate_element(
            self
        ) -> None:
            self.generate_classes_element()
            self.generate_code_element(interfaceOnly=True)
            self.generate_components_element()

        def generate_components_element(
            self,
        ) -> None:
            defaultValueInfoDict = parse_defaultValueInfoDict(
                self.code
            )

            arguments_element = xml.SubElement(
                xml.SubElement(
                    self.element,
                    "components",
                ),
                "arguments"
            )
            for component in session.getComponentsTest(self.name):
                if component.isProtected:
                    continue
                hasDefault = defaultValueInfoDict[
                    types.Identifier(component.name)
                ]
                argument_element = xml.SubElement(
                    arguments_element,
                    "argument",
                    {
                        "inputOutput": component.inputOutput,
                        "className": str(component.className),
                        "name": str(component.name),
                        "hasDefault": "true" if hasDefault else "false",
                        "comment": component.comment,
                    }
                )
                self.generate_dimensions_element(
                    argument_element,
                    component.dimensions,
                )

    def modelica_class(
        className: types.TypeName
    ) -> ModelicaClass:
        restriction = ClassRestriction.from_typeName(session, className)

        if restriction is ClassRestriction.package:
            return ModelicaPackage(className)
        elif restriction is ClassRestriction.type:
            return ModelicaType(className)
        elif restriction is ClassRestriction.record:
            return ModelicaRecord(className)
        elif restriction is ClassRestriction.function:
            return ModelicaFunction(className)
        else:
            raise NotImplementedError(restriction)

    def generate_recursive(
        parent: xml.Element,
        classNames: typing.Sequence[types.TypeName],
    ):
        if not classNames:
            return

        classes_element, = parent.findall("classes")
        for className in classNames:
            classInfo = modelica_class(className)
            classInfo.generate_element()
            classes_element.append(classInfo.element)
            generate_recursive(
                classInfo.element,
                session.getClassNames(className, qualified=True),
            )

    omcInterface_elem = xml.Element(
        "omcInterface",
        {
            "omcVersion": session.getVersion()
        }
    )

    classes_elem = xml.SubElement(
        omcInterface_elem,
        "classes"
    )

    generate_recursive(
        omcInterface_elem,
        [types.TypeName("OpenModelica.Scripting")]
    )

    return xml.ElementTree(omcInterface_elem)


def bootstrap(
    omc_command: StrOrPathLike
):
    with open_omc_session(omc_command) as session:
        omc_interface_xml = generate_omc_interface_xml(
            session
        )

    omc_interface_xml.write(
        sys.stdout.buffer,
        pretty_print=True,
        xml_declaration=True,
        encoding="utf-8",
    )


def load_schema(
) -> xml.XMLSchema:
    return xml.XMLSchema(
        xml.XML(
            pkg_resources.resource_string(
                __name__,
                "interface/omc_interface.xsd",
            )
        )
    )


def validate(
    interface_xml_path: Path,
):
    schema = load_schema()
    parser = xml.XMLParser(schema=schema)
    xml.fromstring(interface_xml_path.read_bytes(), parser)


def main():
    parser = argparse.ArgumentParser(
        prog="omc4py.session.bootstrap debug script",
    )
    parser.add_argument(
        "--omc",
        help="omc executable",
        default=None,
    )
    args = parser.parse_args()
    bootstrap(args.omc)


if __name__ == "__main__":
    main()
