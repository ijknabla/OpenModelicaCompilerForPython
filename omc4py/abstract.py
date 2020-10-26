
import abc


class AbstractInteractiveOMC(
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
    ) -> "AbstractInteractiveOMC":
        return self

    def __exit__(
        self,
        exc_type,
        exc_value,
        traceback,
    ):
        self.close()
        return False
