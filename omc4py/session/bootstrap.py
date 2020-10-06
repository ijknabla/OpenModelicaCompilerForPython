
from .. import parsers

import arpeggio
import collections
import enum
import functools
import operator
import typing
import modelica_language.parsers.syntax

from . import (
    StrOrPathLike,
    InteractiveOMC,
)


class __DefaultFlag(enum.Flag):
    no_default = enum.auto()


def getitem_with_default(
    sequence: typing.Sequence,
    index: typing.Any,
    *,
    default=__DefaultFlag.no_default,
):
    try:
        return operator.getitem(sequence, index)
    except IndexError:
        if default is not __DefaultFlag.no_default:
            return default
        else:
            raise


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


def to_omc_literal(
    obj: typing.Any
) -> str:
    if hasattr(obj, "__to_omc_literal__"):
        return obj.__to_omc_literal__()
    if isinstance(obj, bool):
        if obj:
            return 'true'
        else:
            return 'false'
    if isinstance(obj, str):
        return f'"{parsers.visitor.escape_py_string(obj)}"'
    return str(obj)


class Identifier(
    str
):
    def __to_omc_literal__(
        self
    ) -> str:
        return str(self)


IdentifierTuple = typing.Tuple[Identifier, ...]


class TypeName(
):
    __slots__ = (
        "__parts",
    )

    __parts: IdentifierTuple

    @property
    def parts(self) -> IdentifierTuple:
        return self.__parts

    @staticmethod
    def to_identifiers(
        name: typing.Union[str, Identifier, "TypeName"]
    ) -> IdentifierTuple:
        if isinstance(name, str):
            return parse_type_specifier(name)
        elif isinstance(name, Identifier):
            return name,
        elif isinstance(name, TypeName):
            return name.parts
        else:
            raise TypeError()

    def __new__(cls, *parts):
        self = object.__new__(cls)
        self.__parts = sum(
            map(cls.to_identifiers, parts),
            (),
        )
        return self

    def __str__(
        self
    ) -> str:
        return ".".join(
            map(to_omc_literal, self.parts)
        )

    __to_omc_literal__ = __str__

    def __truediv__(
        self,
        other: typing.Union[str, Identifier, "TypeName"]
    ):
        return type(self)(self, other)


class IdentifierVisitor(
    arpeggio.PTNodeVisitor,
):
    def visit_IDENT(self, node, *_):
        return Identifier(node.value)


class TypeSpecifierVisitor(
    IdentifierVisitor,
):
    def visit_name(
        self,
        node,
        children
    ) -> IdentifierTuple:
        return tuple(children.IDENT)

    def visit_type_specifier(
        self,
        node,
        children,
    ) -> IdentifierTuple:
        name = children.name[0]
        if node[0].value == ".":
            return (Identifier(), *name)
        else:
            return name


def type_specifier_withEOF():
    return (
        modelica_language.parsers.syntax.type_specifier,
        arpeggio.EOF
    )


with parsers.omc_dialect_context:
    type_specifier_parser = arpeggio.ParserPython(type_specifier_withEOF)


def parse_type_specifier(
    literal: str
) -> IdentifierTuple:
    return tuple(
        arpeggio.visit_parse_tree(
            type_specifier_parser.parse(literal),
            TypeSpecifierVisitor(),
        )
    )


class OMCRecord(
    collections.UserDict,
):
    __typeName: TypeName

    def __init__(
        self,
        *args,
        typeName: TypeName,
        **kwrds,
    ):
        super().__init__(*args, **kwrds)
        self.__typeName = typeName

    @property
    def typeName(
        self
    ) -> TypeName:
        return self.__typeName

    def __repr__(
        self
    ):
        return f"{self.typeName}({super().__repr__()})"


class OMCValueVisitor(
    parsers.visitor.NumberVisitor,
    parsers.visitor.BooleanVisitor,
    parsers.visitor.StringVisitor,
    IdentifierVisitor,
    parsers.visitor.SequenceVisitor,
):
    def visit_name(
        self,
        node,
        children,
    ):
        return children.IDENT

    def visit_type_specifier(
        self,
        node,
        children
    ):
        name = children.name[0]
        if node[0].value == ".":
            return TypeName(Identifier(), *name)
        else:
            return TypeName(*name)

    def visit_omc_record_literal(
        self,
        node,
        children
    ):
        typeName = children.type_specifier[0]
        elements = children.omc_record_element_list[0]
        return OMCRecord(elements, typeName=typeName)

    def visit_omc_record_element(
        self,
        node,
        children,
    ):
        IDENT = children.IDENT[0]
        value = children.omc_value[0]
        return IDENT, value

    def visit_omc_record_element_list(
        self,
        node,
        children
    ):
        return children.omc_record_element


def parse_omc_value(
    literal: str
):
    return arpeggio.visit_parse_tree(
        parsers.omc_value_parser.parse(literal),
        OMCValueVisitor()
    )


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
    dimensions: typing.Tuple[str]


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
) -> IdentifierTuple:
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
    ) -> IdentifierTuple:
        return getClassNames(self.omc, self.name)


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


class ModelicaFunctionInfo(
    ModelicaClassInfo
):
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


def bootstrap(
    omc_command: StrOrPathLike
):
    with InteractiveOMC.open(omc_command) as omc:
        ModelicaPackageInfo(
            omc=omc,
            name=TypeName("OpenModelica.Scripting")
        )


if __name__ == "__main__":
    bootstrap("omc")
