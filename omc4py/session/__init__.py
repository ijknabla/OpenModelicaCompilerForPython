
import numpy  # type: ignore
import typing
import warnings

from omc4py import (
    compiler,
    parser,
    string,
)


class OMCSessionBase(
):
    _omc: compiler.InteractiveOMC

    def __init__(
        self,
        omc: compiler.InteractiveOMC
    ):
        self._omc = omc

    def __enter__(
        self,
    ):
        return self

    def __exit__(
        self,
        exc_type,
        exc_value,
        traceback,
    ):
        OMCSession__close(self)
        return False


def OMCSession__open(
    OMCSessionType: typing.Type[OMCSessionBase],
    omc_command: typing.Optional[compiler.StrOrPathLike] = None,
) -> OMCSessionBase:
    omc = compiler.InteractiveOMC.open(
        omc_command=omc_command,
    )
    return OMCSessionType(omc)


def OMCSession__close(
    self: OMCSessionBase
):
    self._omc.close()


PositionalArguments = typing.List[typing.Any]
KeywordArguments = typing.Dict[str, typing.Any]


def OMCSession__call(
    self: OMCSessionBase,
    funcName: str,
    *,
    parse: bool = True,
    args: typing.Optional[PositionalArguments] = None,
    kwrds: typing.Optional[KeywordArguments] = None,
) -> typing.Any:
    argument_literals: typing.List[str] = []
    if args is not None:
        for arg in args:
            argument_literals.append(
                string.to_omc_literal(arg)
            )
    if kwrds is not None:
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

    result_literal = self._omc.evaluate(
        f"{funcName}({arguments_literal})"
    )

    error = self._omc.find_error()

    if error is not None:
        if isinstance(error, Warning):
            warnings.warn(error)
        else:
            raise error

    if parse:
        return parser.parse_OMCValue(result_literal)
    else:
        return result_literal


def cast_scalar_value(
    name: str,
    value: typing.Any,
    class_: typing.Type,
    class_restrictions: typing.Tuple[typing.Type, ...],
) -> typing.Any:
    if class_restrictions:
        if not isinstance(value, class_restrictions):
            raise TypeError(
                f"{name!r} must be an instance of {class_restrictions}"
                f", got {value!r}: {type(value)!r}"
            )
    return class_(value)


def sizes_to_str(
    sizes: typing.Tuple[typing.Optional[int], ...]
) -> str:
    return (
        "{"
        + ", ".join(
            str(size) if size is not None else ":"
            for size in sizes
        )
        + "}"
    )


def cast_array_value(
    name: str,
    value: typing.Any,
    class_: typing.Type,
    class_restrictions: typing.Tuple[typing.Type, ...],
    sizes: typing.Tuple[typing.Optional[int], ...],
) -> numpy.ndarray:
    object_array = numpy.array(value, dtype=object)

    same_n_dimensions = (len(sizes) == object_array.ndim)
    dimensions_are_correct = [
        True if expected is None else expected == actual
        for expected, actual in zip(sizes, object_array.shape)
    ]

    if not(same_n_dimensions and all(dimensions_are_correct)):
        raise ValueError(
            f"Shape of the array must be {sizes_to_str(sizes)}, "
            f"got {sizes_to_str(object_array.shape)}"
        )

    if class_restrictions:
        isinstance_vectorized = numpy.vectorize(
            lambda cls: isinstance(cls, class_restrictions),
            otypes=[numpy.dtype(bool)],
        )
        isinstance_mask = isinstance_vectorized(
            object_array
        )
        if not numpy.all(isinstance_mask):
            raise TypeError(
                f"All items of the array {name!r} "
                f"must be instances of {class_restrictions}"
            )

    class_vectorized = numpy.vectorize(
        class_, otypes=[numpy.dtype(class_)])
    return class_vectorized(object_array)


def cast_value(
    name: str,
    value: typing.Any,
    optional: bool,
    class_: typing.Type,
    class_restrictions: typing.Tuple[typing.Type, ...],
    sizes: typing.Tuple[typing.Optional[int], ...],
) -> typing.Any:
    if value is None:
        if optional:
            return None
        else:
            raise ValueError(
                f"{name!r} must not be None"
            )

    if not sizes:  # scalar
        return cast_scalar_value(
            name=name,
            value=value,
            class_=class_,
            class_restrictions=class_restrictions,
        )
    else:  # array
        return cast_array_value(
            name=name,
            value=value,
            class_=class_,
            class_restrictions=class_restrictions,
            sizes=sizes,
        )
