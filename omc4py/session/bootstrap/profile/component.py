
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
    def py_variable(
        self,
    ) -> str:
        name = str(self.name)
        if keyword.iskeyword(name):
            return name + "_"
        else:
            return name

    @property
    def py_internal_variable(
        self,
    ) -> str:
        return f"{self.py_variable}__internal__"

    @property
    def py_argument(
        self,
    ) -> str:
        if self.optional:
            return f"{self.py_variable}=None"
        else:
            return f"{self.py_variable}"

    @property
    def py_checked_argument(
        self,
    ) -> str:
        if self.needs_check:
            return self.py_variable
        else:
            return self.py_internal_variable

    @property
    def is_scalar(
        self
    ) -> bool:
        return not self.sizes

    @property
    def needs_check(
        self,
    ) -> bool:
        return self.typeProfile.primitive and self.is_scalar

    @property
    def check_code(
        self,
    ) -> CodeBlock:
        if self.needs_check:
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
        else:
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


class OutputArgument(
    typing.NamedTuple,
):
    typeProfile: AbstractTypeProfile
    sizes: Sizes
    name: VariableName
    comment: str
