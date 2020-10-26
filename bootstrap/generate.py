
import argparse
import itertools
from lxml import etree as xml  # type: ignore
from pathlib import Path
import re
import typing

from . import (
    load_schema,
    profile,
)

from .code import (
    INDENT,
    CodeBlock,
)

from omc4py.session import types


def encode_specifier(
    specifier: typing.Union[types.VariableName, types.TypeName]
) -> str:
    pattern = re.compile(r"[0-9A-Za-z]")

    def characters(
    ) -> typing.Iterator[str]:
        for char in str(specifier):
            if pattern.match(char):
                yield char
            else:
                code_point = ord(char)
                yield f"_{code_point:x}_"

    return "".join(characters())


def export_function_names(
    root: xml._Element,
) -> typing.Iterator[types.TypeName]:
    for element in root.xpath(
        '//package[@id="OpenModelica.Scripting"]/classes/function'
    ):
        yield types.TypeName(element.attrib["id"])


def defined_type_names(
    root: xml._Element,
) -> typing.Iterator[types.TypeName]:
    for element in itertools.chain(
        root.xpath('//record'),
        root.xpath('//type')
    ):
        yield types.TypeName(element.attrib["id"])


def ensure_defined_type_names_are_unique(
    root: xml._Element,
) -> None:
    typeNames = list(defined_type_names(root))
    variableNameDict: typing.DefaultDict[
        types.VariableName,
        typing.List[types.TypeName]
    ] = typing.DefaultDict(lambda: [])

    for typeName in typeNames:
        identifier = typeName.last_identifier
        must_unique = variableNameDict[identifier]
        must_unique.append(typeName)
        if 1 < len(must_unique):
            raise ValueError(
                f"Find duplicate VariableName in {must_unique}"
            )

    conflictedVariableNames = (
        variableNameDict.keys()
        & {
            types.VariableName("Real"),
            types.VariableName("Integer"),
            types.VariableName("Boolean"),
            types.VariableName("String"),
            types.VariableName("VariableName"),
            types.VariableName("VariableNames"),
            types.VariableName("TypeName"),
        }
    )

    if conflictedVariableNames:
        raise ValueError(
            "Last identifier in defined type name conflicts builtin type name"
        )


def create_module(
    root: xml._Element,
) -> CodeBlock:
    ensure_defined_type_names_are_unique(root)

    code_import = CodeBlock("""\

# type: ignore
# flake8: noqa

import functools as functools__
import numpy as numpy__
from omc4py.primitive_types import (
    TypeName,
    VariableName,
)
from omc4py.types import OMCEnumeration as OMCEnumeration__
from omc4py.session import OMCSessionBase as OMCSessionBase__
from omc4py.session import OMCSession__open as OMCSession__open__
from omc4py.session import OMCSession__call as OMCSession__call__
from omc4py.session import cast_value as cast_value__
from omc4py.session import OMCSession__close as close_session
from omc4py.session.types import OMCRecord as OMCRecord__
""")

    code_class = CodeBlock(
        "class OMCSession(",
        CodeBlock(
            "OMCSessionBase__,",
            indent=INDENT,
        ),
        "):"
    )

    code_types = CodeBlock()

    code_class_element = CodeBlock(
        indent=INDENT,
    )
    code_class.append(code_class_element)

    code = CodeBlock(
        "\n" * 1,
        code_import,
        "\n" * 2,
        code_types,
        "\n" * 1,
        code_class,
        "\n" * 1,
        (
            "open_session = functools__.partial"
            "(OMCSession__open__, OMCSession)"
        ),
    )

    type_profiles = [
        profile.get_profile_from_xml(root, typeName)
        for typeName in defined_type_names(root)
    ]

    def type_priority(
        typeProfile: profile.base.AbstractTypeProfile,
    ) -> int:
        if isinstance(
            typeProfile,
            profile.type_declaration.EnumerationDeclarationProfile,
        ):
            return 2
        elif isinstance(
            typeProfile,
            profile.type_declaration.RecordDeclarationProfile,
        ):
            return 1
        else:
            return 0

    for type_profile in sorted(
        type_profiles, key=type_priority, reverse=True
    ):
        if isinstance(
            type_profile,
            profile.base.AbstractExtrinsicTypeProfile,
        ):
            code_types.extend(
                [
                    type_profile.generate_class_definition(),
                    "\n" * 2,
                ]
            )

    function_profiles = [
        profile.get_profile_from_xml(root, functionName)
        for functionName in export_function_names(root)
    ]

    for function_profile in function_profiles:
        if (
            isinstance(function_profile, profile.AbstractFunctionProfile)
            and function_profile.supported
        ):
            code_class_element.extend(
                [
                    function_profile.generate_method_code(),
                    "\n" * 1,
                ]
            )
        else:
            print(f"Skip {function_profile.name}")

    return code
