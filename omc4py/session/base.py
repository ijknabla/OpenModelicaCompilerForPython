
import typing

from .. import (
    classes,
    parser,
    types,
)


class OMCSessionBase(
    classes.AbstractOMCSession,
):
    def getComponents(
        self,
        name: types.TypeName
    ) -> typing.List[types.Component]:
        return self.__omc_call__(
            "getComponents",
            args=(
                types.TypeName(name),
            ),
            parser=parser.parse_components,
        )
