from __future__ import annotations

__all__ = (
    "escape_py_string",
    "unescape_modelica_string",
    "to_omc_literal",
)


from collections.abc import Iterable, Sequence
from contextlib import suppress
from functools import lru_cache, reduce
from typing import TYPE_CHECKING, Any

from .protocol import SupportsToOMCLiteral

if TYPE_CHECKING:
    from builtins import _ClassInfo

modelica_char_escape_map = {
    "\\": r"\\",
    "'": r"\'",
    '"': r"\"",
    "\a": r"\a",
    "\b": r"\b",
    "\f": r"\f",
    "\n": r"\n",
    "\t": r"\t",
    "\v": r"\v",
}


def escape_py_string(py_string: str) -> str:
    return _replace_all(py_string, modelica_char_escape_map.items())


def unescape_modelica_string(modelica_string: str) -> str:
    return _replace_all(
        modelica_string,
        [
            (escaped, orignal)
            for orignal, escaped in modelica_char_escape_map.items()
        ],
    )


def quote_py_string(py_string: str) -> str:
    return '"' + escape_py_string(py_string) + '"'


def unquote_modelica_string(modelica_string: str) -> str:
    if not modelica_string.startswith('"'):
        raise ValueError(
            f"modelica_string must starts with '\"' got {modelica_string!r}"
        )
    if not modelica_string.endswith('"'):
        raise ValueError(
            f"modelica_string must ends with '\"' got {modelica_string!r}"
        )
    return unescape_modelica_string(modelica_string[1:-1])


def to_omc_literal(obj: Any) -> str:
    if isinstance(obj, SupportsToOMCLiteral):
        return obj.__to_omc_literal__()
    elif isinstance(obj, bool):
        return "true" if obj else "false"
    elif isinstance(obj, str):
        return '"' + escape_py_string(obj) + '"'
    elif isinstance(obj, _sequence_types()):
        return "{" + ", ".join(map(to_omc_literal, obj)) + "}"
    else:
        return str(obj)


@lru_cache(1)
def _sequence_types() -> _ClassInfo:
    result = [Sequence]
    with suppress(ImportError):
        import numpy

        result.append(numpy.ndarray)
    return tuple(result)


def _replace_all(s: str, old_and_new: Iterable[tuple[str, str]]) -> str:
    return reduce(lambda x, y: x.replace(y[0], y[1]), old_and_new, s)
