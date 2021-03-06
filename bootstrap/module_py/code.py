
import abc
import itertools
import typing


class AbstractCode(
    abc.ABC
):
    indentString: typing.ClassVar[str] = " " * 4

    @abc.abstractmethod
    def append(
        self, code
    ) -> None:
        raise NotImplementedError()

    def extend(
        self, codes
    ) -> None:
        for code in codes:
            self.append(code)

    @abc.abstractmethod
    def to_lines(
        self,
        indentLevel: int = 0,
    ) -> typing.Iterator[str]:
        raise NotImplementedError()

    def dumps(
        self,
    ) -> str:
        return "".join(self.to_lines())

    def bdump(
        self,
        file: typing.BinaryIO,
        encoding="utf-8",
    ):
        file.writelines(
            (
                line.encode(encoding)
                for line in self.to_lines()
            )
        )

    def dump(
        self,
        file: typing.TextIO
    ) -> None:
        file.writelines(
            self.to_lines()
        )


class EmptyLines(
    AbstractCode,
):
    __size: int

    def __init__(
        self,
        size: int,
    ):
        self.__size = size

    def append(self, item):
        raise TypeError(
            f"Can't append item to {type(self)}"
        )

    def to_lines(
        self,
        indentLevel: int = 0
    ) -> typing.Iterator[str]:
        yield from ["\n"] * self.__size

    def __mul__(
        self, n: int,
    ):
        if not isinstance(n, int):
            raise TypeError(
                f"n must be int, got {n}: {type(n)}"
            )
        return type(self)(self.__size * n)


empty_line = EmptyLines(1)


class Code(
    AbstractCode,
):
    __items: typing.List[typing.Union[str, AbstractCode]]
    __sep: typing.Optional[AbstractCode]

    def __init__(
        self,
        *codes,
        sep=None,
    ):
        if not(sep is None or isinstance(sep, AbstractCode)):
            raise TypeError(
                "sep must be AbstractCode or None, "
                f"got {sep}: {type(sep)}"
            )

        self.__items = []
        self.__sep = sep
        self.extend(codes)

    def append(
        self, item
    ):
        if isinstance(item, str):
            self.__items.extend(item.splitlines())
        elif isinstance(item, AbstractCode):
            self.__items.append(item)
        else:
            raise TypeError(
                f"item must be Code or str, got {item}: {type(item)}"
            )

    def items(
        self,
    ) -> typing.Iterator[typing.Union[str, AbstractCode]]:
        items_iter = iter(self.__items)
        for sep in itertools.repeat(
            self.__sep,
            len(self.__items)-1
        ):
            yield next(items_iter)
            if sep is None:
                continue
            else:
                yield sep
        yield from items_iter

    def to_lines(
        self,
        indentLevel: int = 0,
    ) -> typing.Iterator[str]:
        currentIndent = indentLevel
        for item in self.items():
            if isinstance(item, AbstractCode):
                yield from item.to_lines(currentIndent)
            elif isinstance(item, str):
                line = self.indentString * currentIndent + item
                yield (line if line and not line.isspace() else "") + "\n"


class CodeWithIndent(
    Code,
):
    def to_lines(
        self,
        indentLevel: int = 0,
    ) -> typing.Iterator[str]:
        currentIndent = indentLevel + 1
        for item in self.items():
            if isinstance(item, AbstractCode):
                yield from item.to_lines(currentIndent)
            elif isinstance(item, str):
                line = self.indentString * currentIndent + item
                yield (line if line and not line.isspace() else "") + "\n"


class CodeIgnoringIndent(
    Code,
):
    def to_lines(
        self,
        indentLevel: int = 0,
    ) -> typing.Iterator[str]:
        currentIndent = 0
        for item in self.items():
            if isinstance(item, AbstractCode):
                yield from item.to_lines(currentIndent)
            elif isinstance(item, str):
                line = self.indentString * currentIndent + item
                yield (line if line and not line.isspace() else "") + "\n"


class CommentOut(
    Code,
):
    def to_lines(
        self,
        indentLevel: int = 0,
    ) -> typing.Iterator[str]:
        comment_base = self.indentString * indentLevel + "#"

        def lines(
        ) -> typing.Iterator[str]:
            for item in self.items():
                if isinstance(item, AbstractCode):
                    yield from item.to_lines(0)
                elif isinstance(item, str):
                    yield item

        for line in lines():
            if not line or line.isspace():
                yield f"{comment_base}"
            else:
                yield f"{comment_base} {line}"
