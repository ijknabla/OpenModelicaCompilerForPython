
import abc
import argparse
import arpeggio  # type: ignore
import enum
import functools
from lxml import etree as xml  # type: ignore
import os
from pathlib import Path
import pkg_resources
import shutil
import sys
import typing

from omc4py import parser

from .. import (
    OMCSession__call,
    OMCSession__close,
    OMCSession__open,
    OMCSessionBase,
    types,
)


def parse_defaultValueInfoDict(
    interface: str
) -> typing.Dict[types.VariableName, typing.Optional[str]]:
    return dict(
        arpeggio.visit_parse_tree(
            parser.stored_definition_parser.parse(interface),
            parser.visitor.DefaultValueInfoVisitor(),
        )
    )


def parse_enumerator(
    code: str
) -> typing.Tuple[types.VariableName]:
    return arpeggio.visit_parse_tree(
        parser.stored_definition_parser.parse(code),
        parser.visitor.EnumeratorVisitor(),
    )


def parse_alias(
    code: str
) -> typing.Optional[parser.visitor.AliasInfo]:
    return arpeggio.visit_parse_tree(
        parser.stored_definition_parser.parse(code),
        parser.visitor.AliasVisitor(),
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
        return parser.parseComponents(result_literal)


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

            assert(self.name.last_identifier == variableName)
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

            for component in session.getComponents(self.name):
                if component.protected == "protected":
                    continue
                hasDefault = defaultValueInfoDict[
                    component.name
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


class InputType(
    enum.Enum,
):
    executable = enum.auto()
    xml = enum.auto()


class OutputType(
    enum.Enum,
):
    module = enum.auto()
    xml = enum.auto()


from . import generate  # TODO: organize package structure


def generate_omc_interface(
    inputPath: Path,
    inputType: InputType,
    outputFile: typing.BinaryIO,
    outputType: OutputType,
):
    if inputType is InputType.executable:
        with open_session(inputPath) as session:
            omc_interface_xml = generate_omc_interface_xml(
                session
            )
    else:  # inputType is InputType.xml:
        omc_interface_xml = xml.parse(str(inputPath))

    schema = load_schema()
    schema.assertValid(omc_interface_xml)

    if outputType is OutputType.module:
        module_code = generate.create_module(omc_interface_xml)
        module_code.bdump(outputFile)
    else:  # outputType is OutputType.xml:
        omc_interface_xml.write(
            outputFile,
            pretty_print=True,
            xml_declaration=True,
            encoding="utf-8",
        )


def check_input_args(
    input_str: str,
    inputType_hint: typing.Optional[InputType]
) -> typing.Tuple[Path, InputType]:
    if inputType_hint is None:
        if Path(input_str).suffix == ".xml":
            return check_input_args(input_str, InputType.xml)
        else:
            return check_input_args(input_str, InputType.executable)

    elif inputType_hint is InputType.executable:
        executable = shutil.which(input_str)
        if executable is None:
            raise ValueError(
                f"Can't find executable for {input_str!r}"
            )
        return Path(executable), InputType.executable

    elif inputType_hint is InputType.xml:
        absPath = Path(input_str).resolve()
        if not absPath.exists():
            raise FileNotFoundError(
                f"{input_str!r} does not exists!"
            )
        if absPath.suffix != ".xml":
            raise ValueError(
                f"input must be xml, got {input_str!r}"
            )
        return absPath, InputType.xml


def check_output_args(
    output_optional: typing.Optional[typing.BinaryIO],
    outputType_hint: typing.Optional[OutputType],
) -> typing.Tuple[typing.BinaryIO, OutputType]:
    if output_optional is None:
        binary_stdout = sys.stdout.buffer
        if outputType_hint is None:
            return binary_stdout, OutputType.module
        else:
            return binary_stdout, outputType_hint

    output: typing.BinaryIO = output_optional
    path = Path(output.name)

    def close_output():
        output.close()
        os.remove(path)

    if outputType_hint is None:
        if path.suffix == ".py":
            return output, OutputType.module
        elif path.suffix == ".xml":
            return output, OutputType.xml
        else:
            close_output()
            raise ValueError(
                "output file suffix must be .py or .xml"
                f", got {output.name!r}"
            )

    outputType: OutputType = outputType_hint

    if outputType is OutputType.module and path.suffix != ".py":
        close_output()
        raise ValueError(
            "--outputType=module, but output file suffix is not .py"
            f", got {output.name!r}"
        )
    if outputType is OutputType.xml and path.suffix != ".xml":
        close_output()
        raise ValueError(
            "--outputType=xml, but output file suffix is not .xml"
            f", got {output.name!r}"
        )

    return output, outputType


def main():
    """\
Refactored main
    """
    parser = argparse.ArgumentParser(
        prog="omc4py bootstrap",
    )

    # # input
    # omc executable or omc interface xml
    parser.add_argument(
        "input",
    )

    # # inputType
    # {executable, xml}
    # default is None (selected by `input`)
    parser.add_argument(
        "--inputType",
        choices=InputType.__members__,
    )

    # # output
    # default is stdout, (generate python module)
    parser.add_argument(
        "-o", "--output",
        type=argparse.FileType("xb"),
    )

    # # outputType
    # {module, xml}
    # default is None (select by `output`)
    parser.add_argument(
        "--outputType",
        choices=OutputType.__members__,
    )

    args = parser.parse_args()

    inputPath, inputType = check_input_args(
        args.input,
        None if args.inputType is None else InputType[args.inputType],
    )
    outputFile, outputType = check_output_args(
        args.output,
        None if args.outputType is None else OutputType[args.outputType],
    )

    generate_omc_interface(
        inputPath, inputType,
        outputFile, outputType,
    )
