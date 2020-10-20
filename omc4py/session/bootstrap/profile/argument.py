
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


# TODO: move implementation to TypeProfile
def TypeProfile__is_primitive(
    typeProfile: AbstractTypeProfile,
) -> bool:
    return typeProfile.name in {
        TypeName("Real"),
        TypeName("Integer"),
        TypeName("Boolean"),
        TypeName("String"),
    }


# TODO: move implementation to TypeProfile
def TypeProfile__py_type_reference(
    typeProfile: AbstractTypeProfile
) -> str:
    if typeProfile.name == TypeName("Real"):
        return "(numpy__.float_, numpy__.double)"
    elif typeProfile.name == TypeName("Integer"):
        return "(numpy__.int, numpy__.uint)"
    elif typeProfile.name == TypeName("Boolean"):
        return "(numpy__.bool, numpy__.bool_)"
    elif typeProfile.name == TypeName("String"):
        return "(numpy__.str, numpy__.str_)"
    else:
        raise NotImplementedError(typeProfile)


def TypeProfile__py_dtype_reference(
    typeProfile: AbstractTypeProfile
) -> str:
    if typeProfile.name == TypeName("Real"):
        return "numpy__.double"
    elif typeProfile.name == TypeName("Integer"):
        return "numpy__.uint"
    elif typeProfile.name == TypeName("Boolean"):
        return "numpy__.bool_"
    elif typeProfile.name == TypeName("String"):
        return "numpy__.str_"
    elif typeProfile.name == TypeName("OpenModelica.$Code.VariableName"):
        return "types__.VariableName"
    elif typeProfile.name == TypeName("OpenModelica.$Code.TypeName"):
        return "types__.TypeName"
    else:
        raise NotImplementedError(typeProfile)


class InputArgument(
    typing.NamedTuple,
):
    typeProfile: AbstractTypeProfile
    sizes: Sizes
    name: VariableName
    comment: str
    hasDefault: bool

    @property
    def py_variable(
        self,
    ) -> str:
        if keyword.iskeyword(str(self.name)):
            return f"{self.name}_"
        else:
            return f"{self.name}"

    @property
    def py_internal_variable(
        self,
    ) -> str:
        return f"{self.py_variable}__internal__"

    @property
    def py_argument(
        self,
    ) -> str:
        if self.hasDefault:
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
        return (
            TypeProfile__is_primitive(self.typeProfile)
            and self.is_scalar
        )

    @property
    def check_code(
        self,
    ) -> CodeBlock:
        if self.needs_check:
            py_type = TypeProfile__py_type_reference(
                self.typeProfile,
            )
            return CodeBlock(
                "check_value__(",
                CodeBlock(
                    (
                        f"name={self.py_variable!r}, "
                        f"value={self.py_variable},"
                    ),
                    f"class_or_tuple={py_type},",
                    f"optional={self.hasDefault},",

                    indent=INDENT,
                ),
                ")",
            )
        else:
            py_type = TypeProfile__py_dtype_reference(
                self.typeProfile,
            )
            return CodeBlock(
                f"{self.py_internal_variable} = cast_value__(",
                CodeBlock(
                    (
                        f"name={self.py_variable!r}, "
                        f"value={self.py_variable},"
                    ),
                    f"class_={py_type},",
                    f"sizes={self.sizes},",
                    f"optional={self.hasDefault},",
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
