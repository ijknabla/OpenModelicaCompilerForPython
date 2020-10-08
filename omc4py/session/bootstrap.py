
import arpeggio  # type: ignore
import functools
import typing

from . import (
    StrOrPathLike,
    InteractiveOMC,
)

from . import (
    parse_omc_value,
)
from .string import (
    to_omc_literal,
)
from .types import (
    Identifier,
    TypeName,
)
from . import (
    parser,
    visitor,
)


def parse_defaultValueInfoDict(
    interface: str
) -> typing.Dict[Identifier, typing.Optional[str]]:
    return dict(
        arpeggio.visit_parse_tree(
            parser.stored_definition_parser.parse(interface),
            visitor.DefaultValueInfoVisitor(),
        )
    )


class OMCError(
    Exception
):
    ...


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


@with_errorcheck
def evaluate(
    omc: InteractiveOMC,
    expression: str
):
    return parse_omc_value(omc.execute(expression))


def call(
    omc: InteractiveOMC,
    funcName: typing.Union[str, TypeName],
    *,
    args: typing.Optional[typing.Sequence] = None,
    kwrds: typing.Optional[typing.Mapping[str, typing.Any]] = None,
):
    arguments: typing.List[str] = []

    if args is not None:
        arguments.extend(map(to_omc_literal, args))
    if kwrds is not None:
        for key, value in kwrds.items():
            arguments.append(
                f"{key}={to_omc_literal(value)}"
            )

    return evaluate(
        omc,
        "{0}({1})".format(
            to_omc_literal(TypeName(funcName)),
            ",".join(arguments)
        ),
    )


def getComponentsTest(
    omc: InteractiveOMC,
    class_: TypeName,
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
    class_: TypeName
) -> typing.Tuple[Identifier, ...]:
    return tuple(
        map(
            Identifier,
            call(
                omc,
                "getClassNames",
                kwrds={"class_": class_}
            )
        )
    )


def isType(
    omc: InteractiveOMC,
    cl: TypeName,
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
    cl: TypeName,
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
    cl: TypeName,
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
    cl: TypeName,
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
    class_: TypeName,
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
    name: TypeName

    children: typing.Dict[
        Identifier,
        "ModelicaClassInfo"
    ]

    def __init__(
        self,
        omc: InteractiveOMC,
        name: TypeName,
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
    ) -> typing.Tuple[Identifier, ...]:
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
    className: TypeName
    dimensions: typing.List[str]
    name: Identifier
    comment: str
    hasDefault: bool


class OutputArgumentInfo(
    typing.NamedTuple
):
    className: TypeName
    dimensions: typing.List[str]
    name: Identifier
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
                        className=TypeName(component.className),
                        dimensions=component.dimensions,
                        name=Identifier(component.name),
                        comment=component.comment,
                        hasDefault=defaultInfo[Identifier(component.name)]
                    )
                )
            elif component.inputOutput == "output":
                self.outputs.append(
                    OutputArgumentInfo(
                        className=TypeName(component.className),
                        dimensions=component.dimensions,
                        name=Identifier(component.name),
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
            name=TypeName("OpenModelica.Scripting")
        )

    typeNames: typing.Set[TypeName] = set()

    for package, _, contents in OpenModelica_Scripting.walk():
        for content in contents:
            if isinstance(content, ModelicaFunctionInfo):
                for argument in content.inputs + content.outputs:
                    typeNames.add(argument.className)

    for typeName in sorted(typeNames):
        print(typeName)


if __name__ == "__main__":
    bootstrap("omc")
