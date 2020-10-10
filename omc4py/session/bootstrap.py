
import arpeggio  # type: ignore
import enum
import functools
from lxml import etree as xml
import sys
import typing

from . import (
    StrOrPathLike,
    InteractiveOMC,
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


def call_optional(
    func: typing.Callable,
    obj: typing.Optional[typing.Any],
):
    if obj is None:
        return None
    else:
        return func(obj)


class OMCError(
    Exception
):
    ...


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
        if check:
            errorString_literal = self._omc.execute("getErrorString()").rstrip()
            errorString = parse_omc_value(errorString_literal).rstrip()
            if errorString:
                raise OMCError(errorString)

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


def generate_class_xml(
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

    for ident in session.getClassNames(className):
        subClassName = className / ident
        generate_class_xml(
            session,
            class_tag,
            subClassName,
        )
    return parent


def generate_omc_interface_xml(
    session: OMCSession,
) -> xml.ElementTree:
    root = xml.Element(
        "OMCInterface"
    )
    version_tag = xml.SubElement(
        root, "version",
    )
    version_string = session.getVersion()
    version_tag.text = version_string

    generate_class_xml(
        session,
        root,
        types.TypeName("OpenModelica.Scripting")
    )

    return xml.ElementTree(root)


def new_bootstrap(
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


def with_errorcheck(
    func: typing.Callable
) -> typing.Callable:
    @functools.wraps(func)
    def wrapped(
        omc: InteractiveOMC,
        *args,
        check: bool = True,
        **kwrds,
    ):
        result = func(omc, *args, **kwrds)
        errorstring = omc.execute("getErrorString").rstrip()
        if errorstring:
            raise OMCError(errorstring)
        return result

    return wrapped


@with_errorcheck
def execute(
    omc: InteractiveOMC,
    expression: str,
):
    return omc.execute(expression)


@with_errorcheck
def evaluate(
    omc: InteractiveOMC,
    expression: str
):
    return parse_omc_value(omc.execute(expression))


def call(
    omc: InteractiveOMC,
    funcName: typing.Union[str, types.TypeName],
    *,
    args: typing.Optional[typing.Sequence] = None,
    kwrds: typing.Optional[typing.Mapping[str, typing.Any]] = None,
):
    arguments: typing.List[str] = []

    if args is not None:
        arguments.extend(map(string.to_omc_literal, args))
    if kwrds is not None:
        for key, value in kwrds.items():
            arguments.append(
                f"{key}={string.to_omc_literal(value)}"
            )

    return evaluate(
        omc,
        "{0}({1})".format(
            string.to_omc_literal(types.TypeName(funcName)),
            ",".join(arguments)
        ),
    )


def getComponentsTest(
    omc: InteractiveOMC,
    class_: types.TypeName,
) -> typing.Tuple[Component, ...]:
    return tuple(
        Component(**component)
        for component in call(
            omc,
            "getComponentsTest",
            args=[class_]
        )
    )


def getClassNames(
    omc: InteractiveOMC,
    class_: types.TypeName
) -> typing.Tuple[types.Identifier, ...]:
    return tuple(
        map(
            types.Identifier,
            call(
                omc,
                "getClassNames",
                kwrds={"class_": class_}
            )
        )
    )


def isType(
    omc: InteractiveOMC,
    cl: types.TypeName,
) -> bool:
    return bool(
        call(
            omc,
            "isType",
            args=[cl]
        )
    )


def isRecord(
    omc: InteractiveOMC,
    cl: types.TypeName,
) -> bool:
    return bool(
        call(
            omc,
            "isRecord",
            args=[cl]
        )
    )


def isFunction(
    omc: InteractiveOMC,
    cl: types.TypeName,
) -> bool:
    return bool(
        call(
            omc,
            "isFunction",
            args=[cl]
        )
    )


def isPackage(
    omc: InteractiveOMC,
    cl: types.TypeName,
) -> bool:
    return bool(
        call(
            omc,
            "isPackage",
            args=[cl]
        )
    )


def list_(
    omc: InteractiveOMC,
    class_: types.TypeName,
    interfaceOnly: typing.Optional[bool] = None,
    shortOnly: typing.Optional[bool] = None,
) -> str:
    kwrds: typing.Dict[str, typing.Any] = {
        "class_": class_
    }
    if interfaceOnly is not None:
        kwrds["interfaceOnly"] = interfaceOnly
    if shortOnly is not None:
        kwrds["shortOnly"] = shortOnly

    return str(
        call(
            omc,
            "list",
            kwrds=kwrds,
        )
    )


class ModelicaClassInfo():
    omc: InteractiveOMC
    name: types.TypeName

    children: typing.Dict[
        types.Identifier,
        "ModelicaClassInfo"
    ]

    def __init__(
        self,
        omc: InteractiveOMC,
        name: types.TypeName,
    ):
        self.omc = omc
        self.name = name

        self.children = {}

        for childName in self.getClassNames():
            className = self.name / childName
            info: ModelicaClassInfo
            if isType(self.omc, className):
                info = ModelicaTypeInfo(
                    self.omc, className
                )
            elif isRecord(self.omc, className):
                info = ModelicaRecordInfo(
                    self.omc, className
                )
            elif isFunction(self.omc, className):
                info = ModelicaFunctionInfo(
                    self.omc, className
                )
            elif isPackage(self.omc, className):
                info = ModelicaPackageInfo(
                    self.omc, className
                )
            else:
                print(f"missing {className}")
                continue

            self.children[childName] = info

    def getClassNames(
        self
    ) -> typing.Tuple[types.Identifier, ...]:
        return getClassNames(self.omc, self.name)

    def getComponentsTest(
        self
    ) -> typing.Tuple[Component, ...]:
        return getComponentsTest(self.omc, self.name)

    def list_(
        self,
        interfaceOnly: typing.Optional[bool] = None,
        shortOnly: typing.Optional[bool] = None,
    ) -> str:
        return list_(
            self.omc,
            self.name,
            interfaceOnly=interfaceOnly,
            shortOnly=shortOnly,
        )


class ModelicaTypeInfo(
    ModelicaClassInfo
):
    def __init__(
        self,
        *args,
        **kwrds,
    ):
        super().__init__(*args, **kwrds)
        if not isType(self.omc, self.name):
            raise ValueError(
                f"{self} must be type got {self.name}"
            )


class ModelicaRecordInfo(
    ModelicaClassInfo
):
    def __init__(
        self,
        *args,
        **kwrds,
    ):
        super().__init__(*args, **kwrds)
        if not isRecord(self.omc, self.name):
            raise ValueError(
                f"{self} must be record got {self.name}"
            )

        for component in self.getComponentsTest():
            # Record の要素は、下記のものに限定されている。
            # - className
            # - name
            # - comment
            # - dimensions

            assert(not component.isProtected)
            assert(not component.isFinal)
            assert(not component.isFlow)
            assert(not component.isStream)
            assert(not component.isReplaceable)
            assert(not component.variability)
            assert(not component.innerOuter)
            assert(not component.inputOutput)


class InputArgumentInfo(
    typing.NamedTuple
):
    className: types.TypeName
    dimensions: typing.List[str]
    name: types.Identifier
    comment: str
    hasDefault: bool


class OutputArgumentInfo(
    typing.NamedTuple
):
    className: types.TypeName
    dimensions: typing.List[str]
    name: types.Identifier
    comment: str


class ModelicaFunctionInfo(
    ModelicaClassInfo
):
    inputs: typing.List[InputArgumentInfo]
    outputs: typing.List[OutputArgumentInfo]

    def __init__(
        self,
        *args,
        **kwrds,
    ):
        super().__init__(*args, **kwrds)
        if not isFunction(self.omc, self.name):
            raise ValueError(
                f"{self} must be function got {self.name}"
            )

        self.inputs = []
        self.outputs = []

        defaultInfo = parse_defaultValueInfoDict(
            self.list_(interfaceOnly=True)
        )

        for component in self.getComponentsTest():
            if component.isProtected:
                continue
            if component.inputOutput == "input":
                self.inputs.append(
                    InputArgumentInfo(
                        className=types.TypeName(component.className),
                        dimensions=component.dimensions,
                        name=types.Identifier(component.name),
                        comment=component.comment,
                        hasDefault=defaultInfo[types.Identifier(component.name)]
                    )
                )
            elif component.inputOutput == "output":
                self.outputs.append(
                    OutputArgumentInfo(
                        className=types.TypeName(component.className),
                        dimensions=component.dimensions,
                        name=types.Identifier(component.name),
                        comment=component.comment,
                    )
                )
            else:
                raise ValueError(
                    f"Unexpected Component.inputOutput got "
                    f"{component.inputOutput!r}"
                )


class ModelicaPackageInfo(
    ModelicaClassInfo
):
    def __init__(
        self,
        *args,
        **kwrds,
    ):
        super().__init__(*args, **kwrds)
        if not isPackage(self.omc, self.name):
            raise ValueError(
                f"{self} must be package got {self.name}"
            )

    def walk(
        self
    ) -> typing.Iterator[
        typing.Tuple[
            "ModelicaPackageInfo",  # package
            typing.List["ModelicaPackageInfo"],  # sub_packages
            typing.List[ModelicaClassInfo],  # contents
        ]
    ]:
        sub_packages: typing.List[ModelicaPackageInfo] = []
        contents: typing.List[ModelicaClassInfo] = []

        for child in self.children.values():
            if isinstance(child, ModelicaPackageInfo):
                sub_packages.append(child)
            else:
                contents.append(child)

        yield (self, sub_packages, contents)

        for sub_package in sub_packages:
            yield from sub_package.walk()


def bootstrap(
    omc_command: StrOrPathLike
):
    with InteractiveOMC.open(omc_command) as omc:
        OpenModelica_Scripting = ModelicaPackageInfo(
            omc=omc,
            name=types.TypeName("OpenModelica.Scripting")
        )

    typeNames: typing.Set[types.TypeName] = set()

    for package, _, contents in OpenModelica_Scripting.walk():
        for content in contents:
            if isinstance(content, ModelicaFunctionInfo):
                for argument in content.inputs + content.outputs:
                    typeNames.add(argument.className)

    for typeName in sorted(typeNames):
        print(typeName)


if __name__ == "__main__":
    new_bootstrap("omc")
    # bootstrap("omc")
