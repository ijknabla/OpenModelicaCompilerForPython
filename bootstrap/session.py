
import enum
import typing

from omc4py.parser import (
    parse_OMCValue,
)
from omc4py.session import (
    OMCSessionMinimal,
    cast_value,
)
from omc4py.types import (
    Boolean,
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
    ):
        # Check arguments
        class___internal__ = cast_value(
            "class_", class_,
            optional=True,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        interfaceOnly__internal__ = cast_value(
            "interfaceOnly", interfaceOnly,
            optional=True,
            class_=Boolean,
            class_restrictions=(),
            sizes=(),
        )
        shortOnly__internal__ = cast_value(
            "shortOnly", shortOnly,
            optional=True,
            class_=Boolean,
            class_restrictions=(),
            sizes=(),
        )

        # Call function
        return self.__omc_call__(
            "list",
            kwrds={
                VariableName("class_"): class___internal__,
                VariableName("interfaceOnly"): interfaceOnly__internal__,
                VariableName("shortOnly"): shortOnly__internal__,
            },
            parser=parse_OMCValue,
        )

    def getClassNames(
        self,
        class_: typing.Optional[TypeName] = None,
        recursive: typing.Optional[bool] = None,
        qualified: typing.Optional[bool] = None,
    ) -> typing.List[TypeName]:
        # Check arguments
        class___internal__ = cast_value(
            "class_", class_,
            optional=True,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        recursive__internal__ = cast_value(
            "recursive", recursive,
            optional=True,
            class_=Boolean,
            class_restrictions=(Boolean,),
            sizes=(),
        )
        qualified__internal__ = cast_value(
            "qualified", qualified,
            optional=True,
            class_=Boolean,
            class_restrictions=(Boolean,),
            sizes=(),
        )

        # Call function
        return self.__omc_call__(
            "getClassNames",
            kwrds={
                VariableName("class_"): class___internal__,
                VariableName("recursive"): recursive__internal__,
                VariableName("qualified"): qualified__internal__,
            },
            parser=parse_OMCValue,
        )

    def getClassRestriction(
        self,
        cl: TypeName,
    ) -> str:
        # Check arguments
        cl__internal = cast_value(
            "cl", cl,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Call function
        return self.__omc_call__(
            "getClassRestriction",
            args=(
                cl__internal,
            ),
            parser=parse_OMCValue,
        )

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
    ) -> RestrictionEnum:
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
