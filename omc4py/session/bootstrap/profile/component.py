
import keyword
import typing

from omc4py.session.types import (
    VariableName,
    TypeName,
)

from .base import (
    AbstractTypeProfile,
)

from omc4py.session.bootstrap.code import (
    INDENT,
    CodeBlock,
)


Size = typing.Optional[int]
Sizes = typing.Tuple[Size, ...]


def py_identifier(
    variableName: VariableName
) -> str:
    identifier = str(variableName)
    if keyword.iskeyword(identifier):
        return identifier + "_"
    else:
        return identifier


_common_attributes = (
    "typeProfile",
    "sizes",
    "name",
    "comment",
)


class Component(
):
    __slots__ = _common_attributes

    typeProfile: AbstractTypeProfile
    sizes: Sizes
    name: VariableName
    comment: str

    def __init__(
        self,
        typeProfile: AbstractTypeProfile,
        sizes: Sizes,
        name: VariableName,
        comment: str,
    ):
        if typeProfile.name == TypeName(
            "OpenModelica.$Code.VariableNames"
        ):
            variableNameProfile = typeProfile.get_profile(
                TypeName("OpenModelica.$Code.VariableName")
            )
            if sizes:
                raise ValueError(
                    f"VariableNames must be scalar, got sizes={sizes}"
                )

            assert(isinstance(variableNameProfile, AbstractTypeProfile))
            typeProfile = variableNameProfile
            sizes = (None,)

        self.typeProfile = typeProfile
        self.sizes = sizes
        self.name = name
        self.comment = comment

    @property
    def is_array(
        self,
    ) -> bool:
        return bool(self.sizes)

    @property
    def is_forced_to_cast(
        self,
    ) -> bool:
        return self.is_array or not self.typeProfile.primitive

    @property
    def py_variable(
        self,
    ) -> str:
        return py_identifier(self.name)

    @property
    def py_internal_variable(
        self,
    ) -> str:
        return f"{self.py_variable}__internal__"

    @property
    def py_checked_variable(
        self,
    ) -> str:
        if self.is_forced_to_cast:
            return self.py_internal_variable
        else:
            return self.py_variable


class InputArgument(
    Component,
):
    __slots__ = (
        *_common_attributes,
        "optional",
    )

    optional: bool

    def __init__(
        self,
        typeProfile: AbstractTypeProfile,
        sizes: Sizes,
        name: VariableName,
        comment: str,
        optional: bool,
    ):
        super().__init__(typeProfile, sizes, name, comment)
        self.optional = optional

    @property
    def py_argument(
        self,
    ) -> str:
        if self.optional:
            return f"{self.py_variable}=None"
        else:
            return f"{self.py_variable}"

    @property
    def check_code(
        self,
    ) -> CodeBlock:
        if self.is_forced_to_cast:
            py_cast_type = self.typeProfile.py_cast_type_expression
            return CodeBlock(
                f"{self.py_internal_variable} = cast_value__(",
                CodeBlock(
                    (
                        f"name={self.py_variable!r}, "
                        f"value={self.py_variable},"
                    ),
                    f"class_={py_cast_type},",
                    f"sizes={self.sizes},",
                    f"optional={self.optional},",
                    indent=INDENT
                ),
                ")",
            )
        else:
            py_check_type = self.typeProfile.py_check_type_expression
            return CodeBlock(
                "check_value__(",
                CodeBlock(
                    (
                        f"name={self.py_variable!r}, "
                        f"value={self.py_variable},"
                    ),
                    f"class_or_tuple={py_check_type},",
                    f"optional={self.optional},",
                    indent=INDENT,
                ),
                ")",
            )


class OutputArgument(
    typing.NamedTuple,
):
    typeProfile: AbstractTypeProfile
    sizes: Sizes
    name: VariableName
    comment: str
