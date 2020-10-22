
import abc
import argparse
import arpeggio  # type: ignore
import enum
import functools
from lxml import etree as xml  # type: ignore
import pkg_resources
import sys
import typing

from .. import (
    OMCSession__call,
    OMCSession__close,
    OMCSession__open,
    OMCSessionBase,
    StrOrPathLike,
    parser,
    types,
    visitor,
)


class DimensionsVisitor(
    arpeggio.PTNodeVisitor,
):
    def visit_omc_dimensions(self, node, children):
        if children.subscript_list:
            return tuple(children.subscript_list[0])
        else:
            return tuple()

    def visit_subscript_list(
        self, node, children,
    ):
        return children.subscript

    def visit_subscript(self, node, children):
        return node.flat_str()


class Component2(
    typing.NamedTuple,
):
    className: types.TypeName
    name: types.VariableName
    comment: str
    protected: str
    isFinal: bool
    isFlow: bool
    isStream: bool
    isReplaceable: bool
    variability: str
    innerOuter: str
    inputOutput: str
    dimensions: typing.Tuple[str, ...]


class ComponentsVisitor(
    visitor.BooleanVisitor,
    visitor.StringVisitor,
    visitor.TypeSpecifierVisitor,
    DimensionsVisitor,
):
    def visit_omc_component(self, node, children):
        className, = children.type_specifier
        name, = children.IDENT
        (
            comment, protected, variability, innerOuter, inputOutput,
        ) = children.STRING
        isFinal, isFlow, isStream, isReplaceable, = children.boolean
        dimensions, = children.omc_dimensions

        return Component2(
            className=className,
            name=name,
            comment=comment,
            protected=protected,
            isFinal=isFinal,
            isFlow=isFlow,
            isStream=isStream,
            isReplaceable=isReplaceable,
            variability=variability,
            innerOuter=innerOuter,
            inputOutput=inputOutput,
            dimensions=dimensions,
        )

    def visit_omc_component_list(self, node, children):
        return children.omc_component

    def visit_omc_component_array(self, node, children):
        if children.omc_component_list:
            return children.omc_component_list[0]
        else:
            return []


def parseComponents(
    omc_record_array: str
):
    tree = parser.omc_record_array_parser.parse(omc_record_array)
    return arpeggio.visit_parse_tree(
        tree, ComponentsVisitor(),
    )


def parse_defaultValueInfoDict(
    interface: str
) -> typing.Dict[types.VariableName, typing.Optional[str]]:
    return dict(
        arpeggio.visit_parse_tree(
            parser.stored_definition_parser.parse(interface),
            visitor.DefaultValueInfoVisitor(),
        )
    )


def parse_enumerator(
    code: str
) -> typing.Tuple[types.VariableName]:
    return arpeggio.visit_parse_tree(
        parser.stored_definition_parser.parse(code),
        visitor.EnumeratorVisitor(),
    )


def parse_alias(
    code: str
) -> typing.Optional[visitor.AliasInfo]:
    return arpeggio.visit_parse_tree(
        parser.stored_definition_parser.parse(code),
        visitor.AliasVisitor(),
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


class OMCSession(
    OMCSessionBase,
):
    def getVersion(
        self,
        cl: typing.Optional[types.TypeName] = None,
    ) -> str:
        return OMCSession__call(
            self,
            "getVersion",
            kwrds={
                "cl": call_optional(types.TypeName, cl),
            },
        )

    def getClassRestriction(
        self,
        cl: types.TypeName,
    ) -> str:
        return OMCSession__call(
            self,
            "getClassRestriction",
            kwrds={
                "cl": types.TypeName(cl),
            },
        )

    def list(
        self,
        class_: typing.Optional[types.TypeName] = None,
        interfaceOnly: typing.Optional[bool] = None,
        shortOnly: typing.Optional[bool] = None,
    ) -> str:
        return OMCSession__call(
            self,
            "list",
            kwrds={
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
        result = OMCSession__call(
            self,
            "getClassNames",
            kwrds={
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
        result = OMCSession__call(
            self,
            "getComponentsTest",
            args=[
                types.TypeName(name)
            ],
        )
        return [
            Component(**record_literal)
            for record_literal in result
        ]

    def getComponents(
        self,
        name: types.TypeName,
    ):
        result_literal = OMCSession__call(
            self,
            "getComponents",
            parse=False,
            args=[
                types.TypeName(name)
            ],
        )
        return parseComponents(result_literal)


open_session = functools.partial(OMCSession__open, OMCSession)
close_session = OMCSession__close


class ClassRestriction(
    enum.Enum,
):
    package = "package"
    type = "type"
    record = "record"
    function = "function"


def generate_omc_interface_xml(
    session: OMCSession,
) -> xml.ElementTree:

    def restriction_from_typeName(
        typeName: types.TypeName
    ) -> ClassRestriction:
        raw_restriction = session.getClassRestriction(typeName)
        if not raw_restriction:
            raise ValueError(
                f"getClassRestriction({typeName}) returns empty string"
            )
        return ClassRestriction(
            raw_restriction.split()[-1]
        )

    class ModelicaClass(
        abc.ABC
    ):
        restriction: typing.ClassVar[ClassRestriction]
        element: xml.Element

        def __init__(
            self,
            typeName: types.TypeName,
        ):
            self.element = xml.Element(
                self.restriction.value,
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

        def generate_ref_attribute(
            self,
        ) -> bool:
            variableName_className = parse_alias(
                session.list(self.name, shortOnly=True)
            )

            if variableName_className is None:
                return False

            variableName, className = variableName_className

            for parent in self.name.parents:
                candidate = parent/className
                try:
                    restriction = restriction_from_typeName(candidate)
                except ValueError:
                    continue
                if restriction is self.restriction:
                    break
            else:
                raise ValueError(f"Can't resolve {className} from {self.name}")

            assert(self.name.parts[-1] == variableName)
            self.element.attrib["ref"] = str(candidate)
            return True

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
        restriction = ClassRestriction.package

        def generate_element(
            self
        ) -> None:
            if self.generate_ref_attribute():
                return
            self.generate_classes_element()

    class ModelicaType(ModelicaClass):
        restriction = ClassRestriction.type

        def generate_element(
            self
        ) -> None:
            if self.generate_ref_attribute():
                return
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
        restriction = ClassRestriction.record

        def generate_element(
            self
        ) -> None:
            if self.generate_ref_attribute():
                return
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

            for component in session.getComponents(self.name):
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
        restriction = ClassRestriction.function

        def generate_element(
            self
        ) -> None:
            if self.generate_ref_attribute():
                return
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

            componentsTest = session.getComponentsTest(self.name)
            components = session.getComponents(self.name)
            for componentTest in componentsTest:
                if componentTest.isProtected:
                    continue
                hasDefault = defaultValueInfoDict[
                    types.VariableName(componentTest.name)
                ]
                argument_element = xml.SubElement(
                    arguments_element,
                    "argument",
                    {
                        "inputOutput": componentTest.inputOutput,
                        "className": str(componentTest.className),
                        "name": str(componentTest.name),
                        "hasDefault": "true" if hasDefault else "false",
                        "comment": componentTest.comment,
                    }
                )
                self.generate_dimensions_element(
                    argument_element,
                    componentTest.dimensions,
                )

    def modelica_class(
        className: types.TypeName
    ) -> ModelicaClass:
        restriction = restriction_from_typeName(className)
        for klass in [
            ModelicaPackage,
            ModelicaType,
            ModelicaRecord,
            ModelicaFunction,
        ]:
            if klass.restriction is restriction:
                return klass(className)
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

    xml.SubElement(
        omcInterface_elem,
        "classes"
    )

    generate_recursive(
        omcInterface_elem,
        [types.TypeName("OpenModelica.Scripting")]
    )

    return xml.ElementTree(omcInterface_elem)


def bootstrap(
    binary_output: typing.BinaryIO,
    omc_command: StrOrPathLike,
):
    with open_session(omc_command) as session:
        omc_interface_xml = generate_omc_interface_xml(
            session
        )

    omc_interface_xml.write(
        binary_output,
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
                "../interface/omc_interface.xsd",
            )
        )
    )


def main():
    parser = argparse.ArgumentParser(
        prog="omc4py.session.bootstrap debug script",
    )
    parser.add_argument(
        "--omc",
        help="omc executable",
        default=None,
    ),
    parser.add_argument(
        "--output",
        type=argparse.FileType("wb"),
        default=sys.stdout.buffer
    )
    args = parser.parse_args()

    bootstrap(
        args.output,
        args.omc
    )
