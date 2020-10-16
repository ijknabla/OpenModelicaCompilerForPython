
import abc
import collections
import enum
import typing


class Indentation(enum.Enum):
    no_indent = enum.auto()
    indent = enum.auto()
    ignore_indent = enum.auto()


NO_INDENT = Indentation.no_indent
INDENT = Indentation.indent
IGNORE_INDENT = Indentation.ignore_indent


class AbstractCodeBlock(
    abc.ABC
):
    indentString: typing.ClassVar[str] = " " * 4

    @abc.abstractmethod
    def append(
        self, code
    ):
        raise NotImplementedError()

    @abc.abstractmethod
    def extend(
        self, codes
    ):
        raise NotImplementedError()

    @abc.abstractmethod
    def to_lines(
        self,
        indentLevel: int = 0,
    ) -> typing.Iterator[str]:
        raise NotImplementedError()

    def dumps(
        self
    ):
        "".join(self.to_lines())

    def dump(
        self,
        file: typing.TextIO
    ) -> None:
        file.writelines(
            self.to_lines()
        )


class CodeBlock(
    AbstractCodeBlock,
    collections.UserList,
):
    indent: Indentation

    def __init__(
        self,
        items: typing.Optional[typing.Iterable] = None,
        *,
        indent: Indentation = Indentation.no_indent
    ):
        super().__init__()
        if items is not None:
            self.extend(items)
        self.indent = indent

    def append(
        self,
        item,
    ) -> None:
        if isinstance(item, AbstractCodeBlock):
            super().append(item)
        else:
            item = str(item)
            if item:
                super().extend(item.splitlines())
            else:
                super().append("")

    def extend(
        self,
        items
    ) -> None:
        if isinstance(items, str):
            self.append(items)
        else:
            for item in items:
                self.append(item)

    def __repr__(
        self
    ) -> str:
        return (
            f"{type(self).__name__}("
            f"{super().__repr__()}, indent={self.indent!r}"
            f")"
        )

    def to_lines(
        self,
        indentLevel: int = 0,
    ) -> typing.Iterator[str]:
        currentIndent: int
        if self.indent is Indentation.no_indent:
            currentIndent = indentLevel
        elif self.indent is Indentation.indent:
            indentLevel += 1
            currentIndent = indentLevel
        elif self.indent is Indentation.ignore_indent:
            currentIndent = 0

        for elem in self:
            if isinstance(elem, AbstractCodeBlock):
                yield from elem.to_lines(indentLevel)
            else:
                line = self.indentString * currentIndent + elem
                yield (line if line and not line.isspace() else "") + "\n"
