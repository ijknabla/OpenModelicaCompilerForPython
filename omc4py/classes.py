
import abc
import typing
import typing_extensions

from . import (
    string,
    types,
)


class AbstractOMCInteractive(
    abc.ABC
):
    @abc.abstractmethod
    def close(self) -> None: ...

    @abc.abstractmethod
    def evaluate(
        self,
        expression: str,
    ) -> str: ...

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
