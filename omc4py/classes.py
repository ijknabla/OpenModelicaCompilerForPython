
import abc
import typing
import typing_extensions


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

    @abc.abstractmethod
    def __omc_check__(self) -> None: ...
