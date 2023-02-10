from __future__ import annotations

import abc
import collections
import keyword
import typing
from typing import TYPE_CHECKING

from lxml import etree  # type: ignore

from omc4py.classes import REQUIRED_or_OPTIONAL, TypeName, VariableName

from .code import (
    AbstractCode,
    Code,
    CodeIgnoringIndent,
    CodeWithIndent,
    CommentOut,
    empty_line,
)

if TYPE_CHECKING:
    from omc4py.classes import Dimensions


class ClassNameAndDimensions(
    typing.NamedTuple,
):
    className: TypeName
    dimensions: Dimensions

    @classmethod
    def from_component(
        cls,
        component: etree._Element,
    ) -> "ClassNameAndDimensions":
        className = TypeName(component.attrib["className"])

        def dimension_generator() -> typing.Iterator[typing.Optional[int]]:
            for dimension in component.xpath("./dimensions/*"):
                try:
                    yield int(dimension.attrib["size"])
                except ValueError:
                    yield None

        dimensions: Dimensions = tuple(dimension_generator())

        # Convert intrinsic types
        if className.last_identifier == VariableName("TypeName"):
            className = TypeName("TypeName")
        elif className.last_identifier == VariableName("VariableName"):
            className = TypeName("VariableName")
        elif className.last_identifier == VariableName("VariableNames"):
            if dimensions:
                raise ValueError("VariableNames must be scalar")
            className = TypeName("VariableName")
            dimensions = (None,)

        return cls(className, dimensions)

    @property
    def component_literal(
        self,
    ) -> str:
        if not self.dimensions:
            s_dimensions = ""
        else:
            s_dimensions = "[{}]".format(
                ", ".join(
                    str(dimension) if dimension is not None else ":"
                    for dimension in self.dimensions
                )
            )

        return f"Component({self.className}){s_dimensions}"


def get_component_literal(
    component: etree._Element,
):
    return ClassNameAndDimensions.from_component(component).component_literal


def is_supported_element(
    element: etree._Element,
) -> bool:
    if "ref" in element.attrib:
        ref = element.attrib["ref"]
        (target,) = element.xpath(f'//*[@id="{ref}"]')
        return is_supported_element(target)

    if element.tag in {"function", "record"}:

        def valid_component(
            component: etree._Element,
        ) -> bool:
            className, _ = ClassNameAndDimensions.from_component(component)
            if className in {
                TypeName("Real"),
                TypeName("Integer"),
                TypeName("Boolean"),
                TypeName("String"),
                TypeName("VariableName"),
                TypeName("TypeName"),
            }:
                return True

            class_ = element.xpath(f'//*[@id="{className!s}"]')
            return bool(class_) and is_supported_element(class_[0])

        return all(map(valid_component, element.xpath("./components/*/*")))

    return True


class AbstractModelicaClass(
    abc.ABC,
):
    element: etree._Element
    children: typing.MutableMapping[str, "AbstractModelicaClass"]

    def __init__(self, element: etree._Element):
        self.element = element
        self.children = collections.OrderedDict()

    @property
    def className(self) -> TypeName:
        return TypeName(self.element.attrib["id"])

    def __getitem__(self, index: TypeName) -> "AbstractModelicaClass":
        if index == self.className:
            return self

        cursor = index.parts[len(self.className.parts)]
        return self.children[cursor][index]

    def add_class(
        self,
        class_: "AbstractModelicaClass",
    ):
        className = class_.className
        parent = self[className.parent]
        parent.children[str(className.last_identifier)] = class_

    def generate_class_header(self, base_class_name: str) -> Code:
        return Code(
            f"@modelica_name({str(self.className)!r})",
            f"class {self.className.last_identifier}(",
            CodeWithIndent(
                f"{base_class_name},",
            ),
            "):",
        )

    def generate___doc__(
        self,
    ) -> Code:
        code = self.element.find("code")
        if code is None:
            return Code()

        if not code.text:
            content = ""
        else:
            content = "\n".join(
                [
                    "```modelica",
                    code.text.replace("\\", r"\\"),
                    "```",
                ]
            )

        return Code(
            '"""',
            CodeIgnoringIndent(content),
            '"""',
        )

    def generate_class_codes(
        self,
    ) -> typing.Iterator[AbstractCode]:
        for child_class in self.children.values():
            yield child_class.to_code()

    @abc.abstractmethod
    def to_code(
        self,
    ) -> AbstractCode:
        return NotImplemented


class ModelicaAlias(
    AbstractModelicaClass,
):
    def to_code(
        self,
    ) -> AbstractCode:
        code = Code(
            f"@modelica_name({str(self.className)!r})",
            "@alias",
            f"def {self.className.last_identifier}(cls):",
            CodeWithIndent(f'return {self.element.attrib["ref"]}'),
        )

        if is_supported_element(self.element):
            return code
        else:
            return CommentOut(code)


class ModelicaEnumeration(
    AbstractModelicaClass,
):
    def to_code(
        self,
    ) -> AbstractCode:
        enumerators_code = Code()
        code = Code(
            self.generate_class_header("ModelicaEnumeration"),
            CodeWithIndent(
                self.generate___doc__(),
                enumerators_code,
            ),
        )

        for enumerator in self.element.xpath("./components/enumerators/*"):
            name = enumerator.attrib["name"]
            comment = enumerator.attrib["comment"]
            enumerators_code.append(
                f"{name} = enum.auto()" + (f"  # {comment}" if comment else "")
            )

        if is_supported_element(self.element):
            return code
        else:
            return CommentOut(code)


class ModelicaPackage(AbstractModelicaClass):
    def to_code(
        self,
    ) -> AbstractCode:
        code = Code(
            self.generate_class_header("ModelicaPackage"),
            CodeWithIndent(
                *self.generate_class_codes(),
                sep=empty_line,
            ),
        )

        if is_supported_element(self.element):
            return code
        else:
            return CommentOut(code)


class ModelicaRecord(
    AbstractModelicaClass,
):
    def to_code(
        self,
    ) -> AbstractCode:
        contents_code = Code(sep=empty_line)
        code = Code(
            self.generate_class_header("ModelicaRecord"),
            CodeWithIndent(
                self.generate___doc__(),
                contents_code,
            ),
        )

        for element in self.element.xpath("./components/elements/*"):
            name = element.attrib["name"]
            contents_code.append(
                Code(
                    "@element",
                    f"def {name}(cls):",
                    CodeWithIndent(f"return {get_component_literal(element)}"),
                )
            )

        contents_code.extend(self.generate_class_codes())

        if is_supported_element(self.element):
            return code
        else:
            return CommentOut(code)


class InputArgument(typing.NamedTuple):
    component_literal: str
    modelica_name: str
    required: REQUIRED_or_OPTIONAL

    @property
    def py_name(
        self,
    ) -> str:
        if not keyword.iskeyword(self.modelica_name):
            return f"{self.modelica_name}"
        else:
            return f"{self.modelica_name}_"


class ModelicaFunction(
    AbstractModelicaClass,
):
    def to_code(self) -> AbstractCode:
        external_code = Code()
        contents_code = Code(external_code, sep=empty_line)
        code = Code(
            self.generate_class_header("ModelicaFunction"),
            CodeWithIndent(
                self.generate___doc__(),
                contents_code,
            ),
        )

        inputArguments = [
            InputArgument(
                component_literal=get_component_literal(argument),
                modelica_name=argument.attrib["name"],
                required=(
                    "optional"
                    if argument.attrib["hasDefault"] == "true"
                    else "required"
                ),
            )
            for argument in self.element.xpath(
                './components/arguments/*[@inputOutput="input"]'
            )
        ]

        arguments_code = Code()
        execution_code = Code()
        external_code.extend(
            [
                "@external",
                "def _(",
                CodeWithIndent(arguments_code),
                "):",
                CodeWithIndent(execution_code),
            ]
        )

        arguments_code.append("_cls_,")
        arguments_code.append("_session_: AbstractOMCSession,")
        for argument in sorted(
            inputArguments,
            key=lambda argument: 0 if argument.required == "required" else 1,
        ):
            if argument.required == "required":
                s_default = ""
            else:
                s_default = "=None"
            arguments_code.append(f"{argument.py_name}{s_default},")

        if self.className.parent == TypeName("OpenModelica.Scripting"):
            funcName = str(self.className.last_identifier)
        else:
            funcName = str(self.className)

        execution_code.extend(
            [
                "return _session_.__omc__.call_function(",
                CodeWithIndent(
                    f"funcName={funcName!r},",
                    "inputArguments=[",
                    CodeWithIndent(
                        *(
                            "("
                            f"{argument.component_literal}, "
                            f"{argument.modelica_name!r}, "
                            f"{argument.py_name}, "
                            f"{argument.required!r}"
                            "),"
                            for argument in inputArguments
                        )
                    ),
                    "],",
                    "outputArguments=[",
                    CodeWithIndent(
                        *(
                            "("
                            f"{get_component_literal(argument)}, "
                            f'{argument.attrib["name"]!r}'
                            "),"
                            for argument in self.element.xpath(
                                './components/arguments/*[@inputOutput="output"]'  # noqa: E501
                            )
                        )
                    ),
                    "],",
                    "parser=parse_OMCValue,",
                ),
                ")",
            ]
        )

        contents_code.extend(self.generate_class_codes())

        if is_supported_element(self.element):
            return code
        else:
            return CommentOut(code)


def generate_module_py(
    omc_interface_xml: etree._ElementTree,
) -> Code:
    return Code(
        empty_line,
        generate_import_statements(),
        empty_line * 2,
        generate_nested_modelica_class(
            omc_interface_xml.xpath("//*[@id]")
        ).to_code(),
        empty_line * 2,
        generate_session_class(
            omc_interface_xml,
        ),
    )


def generate_import_statements() -> Code:
    return Code(
        "from omc4py.classes import (",
        CodeWithIndent(
            "AbstractOMCSession,",
            "Boolean,",
            "Component,",
            "Integer,",
            "ModelicaEnumeration,",
            "ModelicaFunction,",
            "ModelicaPackage,",
            "ModelicaRecord,",
            "Real,",
            "String,",
            "TypeName,",
            "VariableName,",
            "alias,",
            "element,",
            "enum,",
            "external,",
            "modelica_name,",
        ),
        ")",
        empty_line,
        "from omc4py.parser import parse_OMCValue__v_1_13 as parse_OMCValue",
        empty_line,
        "from omc4py.session import OMCSessionBase__v_1_13 as OMCSessionBase",
    )


def generate_nested_modelica_class(
    elements: typing.List[etree._Element],
) -> AbstractModelicaClass:
    if not elements:
        raise ValueError("elements are empty!")
    elements_iter = iter(elements)

    root_modelica_class = generate_modelica_class(next(elements_iter))
    for modelica_class in map(generate_modelica_class, elements_iter):
        root_modelica_class.add_class(modelica_class)

    return root_modelica_class


def generate_modelica_class(
    element: etree._Element,
) -> AbstractModelicaClass:
    if "ref" in element.attrib:
        return ModelicaAlias(element)
    elif element.tag == "type" and element.xpath("./components/enumerators"):
        return ModelicaEnumeration(element)
    elif element.tag == "package":
        return ModelicaPackage(element)
    elif element.tag == "record":
        return ModelicaRecord(element)
    elif element.tag == "function":
        return ModelicaFunction(element)
    else:
        raise NotImplementedError(
            f"code generation for <{element.tag}/> is not defined"
        )


def generate_session_class(
    omc_interface_xml: etree._ElementTree,
) -> Code:
    elements_code = Code()
    code = Code(
        "class OMCSession(",
        CodeWithIndent(
            "OMCSessionBase,",
        ),
        "):",
        CodeWithIndent(elements_code),
    )

    elements_code.append("OpenModelica = OpenModelica")
    (OpenModelica_Scripting,) = omc_interface_xml.xpath(
        '//*[@id="OpenModelica.Scripting"]'
    )
    for modelica_class in OpenModelica_Scripting.xpath("./classes/*"):
        if modelica_class.tag == "package":
            continue

        className = TypeName(modelica_class.attrib["id"])
        if is_supported_element(modelica_class):
            elements_code.append(f"{className.last_identifier} = {className}")
        else:
            elements_code.append(
                f"# {className.last_identifier} = {className}"
            )

    return code
