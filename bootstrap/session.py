
import enum
import typing

from omc4py.classes import (
    Component,
)
from omc4py.parser import (
    parse_OMCValue,
)
from omc4py.session import (
    OMCSessionMinimal,
    cast_value,
)
from omc4py.types import (
    Boolean,
    String,
    TypeName,
    VariableName,
)


class OMCSessionBootstrap(
    OMCSessionMinimal,
):
    def list(
        self,
        class_: typing.Optional[TypeName] = None,
        interfaceOnly: typing.Optional[bool] = None,
        shortOnly: typing.Optional[bool] = None,
    ) -> str:
        __result = self.__omc__.call_function(
            funcName="list",
            inputArguments=[
                (Component(TypeName), "class_", class_, "optional"),
                (Component(Boolean), "interfaceOnly", interfaceOnly, "optional"),
                (Component(Boolean), "shortOnly", shortOnly, "optional"),
            ],
            outputArguments=[
                (Component(String), "contents"),
            ]
        )
        self.__omc_check__()
        return str(__result)

    def getClassNames(
        self,
        class_: typing.Optional[TypeName] = None,
        recursive: typing.Optional[bool] = None,
        qualified: typing.Optional[bool] = None,
    ) -> typing.List[TypeName]:
        __result = self.__omc__.call_function(
            funcName="getClassNames",
            inputArguments=[
                (Component(TypeName), "class_", class_, "optional"),
                (Component(Boolean), "recursive", recursive, "optional"),
                (Component(Boolean), "qualified", qualified, "optional"),
            ],
            outputArguments=[
                (Component(TypeName)[:], "classNames"),
            ],
        )
        self.__omc_check__()
        return list(__result)

    def getClassRestriction(
        self,
        cl: TypeName,
    ) -> str:
        __result = self.__omc__.call_function(
            funcName="getClassRestriction",
            inputArguments=[
                (Component(TypeName), "cl", cl, "required"),
            ],
            outputArguments=[
                (Component(String), "restriction"),
            ],
        )
        self.__omc_check__()
        return str(__result)

    class RestrictionEnum(
        enum.Enum,
    ):
        type = enum.auto()
        package = enum.auto()
        record = enum.auto()
        function = enum.auto()

    def getClassRestrictionEnum(
        self,
        cl: TypeName,
    ) -> "RestrictionEnum":
        keywords_to_ignore = {
            "impure",
        }
        return self.RestrictionEnum[
            " ".join(
                word
                for word in self.getClassRestriction(cl).split(' ')
                if word not in keywords_to_ignore
            )
        ]
