
__all__ = (
    "Boolean",
    "Integer",
    "Real",
    "String",
    "TypeName",
    "VariableName",
)

import typing

from . import (
    string,
)

from ..primitive_types import (
    Real,
    Integer,
    Boolean,
    String,
    VariableName,
    TypeName,
)


RecordFields = typing.Dict[
    str,
    typing.Callable[[typing.Any], typing.Any],
]


class OMCRecord(
    dict,
):
    __recordName__: typing.ClassVar[TypeName]
    __fields__: typing.ClassVar[RecordFields]

    def __init__(
        self,
        *args,
        **kwrds,
    ):
        _dict = dict(*args, **kwrds)
        expected_keys = self.__fields__.keys()
        actual_keys = _dict.keys()

        if actual_keys != expected_keys:
            raise KeyError(
                f"{type(self)} keys must be {expected_keys}, "
                f"got {actual_keys}"
            )

        self.update(_dict)

    def keys(
        self,
    ) -> typing.KeysView[str]:
        return self.__fields__.keys()

    def __setitem__(
        self,
        key, value
    ) -> None:
        if key not in self.keys():
            raise KeyError(
                f"Key must be one of the {self.keys()}, "
                f"got {key!r}"
            )
        value__internal__ = self.__fields__[key](value)
        super().__setitem__(
            key,
            value__internal__,
        )

    def __to_omc_literal__(
        self,
    ) -> str:
        def lines():
            recordNameLiteral = string.to_omc_literal(self.__recordName__)
            yield f"record {recordNameLiteral} "
            if self:
                elements = [
                    f"{variableName}={string.to_omc_literal(value)}"
                    for variableName, value in self.items()
                ]
                yield ", ".join(elements) + " "
            yield f"end {recordNameLiteral};"

        return "".join(lines())
