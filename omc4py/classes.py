
import abc
import typing
import typing_extensions

from . import (
    string,
    types,
)


Dimensions = typing.Tuple[typing.Optional[int], ...]

REQUIRED = typing_extensions.Literal["required"]
OPTIONAL = typing_extensions.Literal["optional"]
REQUIRED_or_OPTIONAL = typing.Union[REQUIRED, OPTIONAL]

InputArgument = typing.Tuple[
    "Component", str,
    typing.Any, REQUIRED_or_OPTIONAL
]
OutputArgument = typing.Tuple[
    "Component", str
]


class Component(
):
    class_: typing.Type
    dimensions: Dimensions

    def __init__(
        self,
        class_: typing.Type,
        dimensions: typing.Optional[Dimensions] = None,
    ):
        self.class_ = class_
        if dimensions is None:
            self.dimensions = ()
        else:
            self.dimensions = dimensions

    def __getitem__(
        self, index,
    ) -> "Component":
        if not isinstance(index, tuple):
            return self[(index,)]

        def dimensions_generator(
        ) -> typing.Iterator[typing.Optional[int]]:
            for idim, dimension in enumerate(index):
                if isinstance(dimension, int):
                    if dimension < 0:
                        raise ValueError(
                            f'dimension #{idim}: int must be positive, '
                            f'got {dimension!r}'
                        )
                    else:
                        yield dimension
                elif isinstance(dimension, slice):
                    start = dimension.start
                    stop = dimension.stop
                    step = dimension.step
                    if not (start is None and stop is None and step is None):
                        raise ValueError(
                            f"dimension #{idim}: slice must be ':', "
                            f'got {start!s}:{stop!s}:{step!s}'
                        )
                    else:
                        yield None
                else:
                    raise TypeError(
                        f"dimension #{idim} must be int or slice, "
                        f"got {dimension!r}: {type(dimension)}"
                    )

        return Component(self.class_, tuple(dimensions_generator()))


class AbstractOMCInteractive(
    abc.ABC
):
    @abc.abstractmethod
    def close(self) -> None: ...

    @abc.abstractmethod
    def evaluate(
        self,
        expression: str,
    ) -> str:
        ...

    @abc.abstractmethod
    def call_function(
        self,
        funcName: str,
        inputArguments: typing.Sequence[InputArgument],
        outputArguments: typing.Sequence[OutputArgument],
    ):
        ...

    def __enter__(
        self,
    ) -> "AbstractOMCInteractive":
        return self

    def __exit__(
        self,
        exc_type,
        exc_value,
        traceback,
    ) -> typing_extensions.Literal[False]:
        self.close()
        return False


PositionalArguments = typing.Sequence[typing.Any]
KeywordArguments = typing.Mapping[types.VariableName, typing.Any]
Parser = typing.Callable[[str], typing.Any]


class AbstractOMCSession(
    abc.ABC,
):
    __omc: AbstractOMCInteractive

    def __init__(
        self,
        omc: AbstractOMCInteractive,
    ):
        self.__omc = omc

    @property
    def __omc__(self) -> AbstractOMCInteractive:
        return self.__omc

    def __omc_call__(
        self,
        funcName: str,
        *,
        args: typing.Optional[PositionalArguments] = None,
        kwrds: typing.Optional[KeywordArguments] = None,
        parser: typing.Optional[Parser] = None,
        check: bool = True,
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

        result_literal = self.__omc__.evaluate(
            "{}({})".format(
                funcName,
                ", ".join(argument_literals)
            )
        )

        if check:
            self.__omc_check__()

        if parser is None:
            return result_literal
        else:
            return parser(result_literal)

    @abc.abstractmethod
    def __omc_check__(self) -> None: ...
