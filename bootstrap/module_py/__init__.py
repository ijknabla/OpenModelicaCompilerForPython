
import abc
import collections
from lxml import etree  # type: ignore
import typing

from .code import (
    AbstractCode,
    Code,
    CodeWithIndent,
    CommentOut,
    empty_line,
)

from omc4py.classes import (
    Dimensions,
    TypeName,
    VariableName,
)


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

        def dimension_generator(
        ) -> typing.Iterator[typing.Optional[int]]:
            for dimension in component.xpath('./dimensions/*'):
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
                raise ValueError(
                    "VariableNames must be scalar"
                )
            className = TypeName("VariableName")
            dimensions = (None,)

        return cls(className, dimensions)


def is_supported_element(
    element: etree._Element,
) -> bool:
    if "ref" in element.attrib:
        ref = element.attrib["ref"]
        target, = element.xpath(f'//*[@id="{ref}"]')
        return is_supported_element(target)
    elif element.tag == "function":
        for classNameAndDimensions in map(
            ClassNameAndDimensions.from_component,
            element.xpath('./components/arguments/*'),
        ):
            if "$" in str(classNameAndDimensions.className):
                return False
        else:
            return True
    else:
        return True


class AbstractModelicaClass(
    abc.ABC,
):
    element: etree._Element
    children: typing.MutableMapping[str, "AbstractModelicaClass"]

    def __init__(
        self,
        element: etree._Element
    ):
        self.element = element
        self.children = collections.OrderedDict()

    @property
    def className(
        self
    ) -> TypeName:
        return TypeName(self.element.attrib["id"])

    def __getitem__(
        self,
        index: TypeName
    ) -> "AbstractModelicaClass":
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


class GenericModelicaClass(
    AbstractModelicaClass,
):
    def to_code(
        self
    ) -> AbstractCode:
        code = Code(
            f"class {self.className.last_identifier}(",
            "):",
            CodeWithIndent(
                "...",
                *self.generate_class_codes(),
                sep=empty_line,
            ),
        )
        if is_supported_element(self.element):
            return code
        else:
            return CommentOut(code)


def generate_module_py(
    omc_interface_xml: etree._ElementTree,
) -> Code:
    return Code(
        empty_line,
        generate_nested_modelica_class(
            omc_interface_xml.xpath('//*[@id]')
        ).to_code(),
    )


def generate_nested_modelica_class(
    elements: typing.List[etree._Element],
) -> AbstractModelicaClass:
    if not elements:
        raise ValueError(
            "elements are empty!"
        )
    elements_iter = iter(elements)

    root_modelica_class = generate_modelica_class(next(elements_iter))
    for modelica_class in map(generate_modelica_class, elements_iter):
        root_modelica_class.add_class(modelica_class)

    return root_modelica_class


def generate_modelica_class(
    element: etree._Element,
) -> AbstractModelicaClass:
    return GenericModelicaClass(element)
