__all__ = (
    "escape_py_string",
    "unescape_modelica_string",
    "to_omc_literal",
)


import typing
from functools import reduce

import numpy  # type: ignore

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


def to_omc_literal(obj: typing.Any) -> str:
    if hasattr(obj, "__to_omc_literal__"):
        return obj.__to_omc_literal__()
    elif isinstance(obj, (classes.Boolean, bool)):
        return "true" if obj else "false"
    elif isinstance(obj, (classes.String, str)):
        return '"' + escape_py_string(obj) + '"'
    elif isinstance(obj, (typing.Sequence, numpy.ndarray)):
        return "{" + ", ".join(map(to_omc_literal, obj)) + "}"
    else:
        return str(obj)


def _replace_all(
    s: str, old_and_new: typing.Iterable[typing.Tuple[str, str]]
) -> str:
    return reduce(lambda x, y: x.replace(y[0], y[1]), old_and_new, s)


from . import classes  # noqa: E402
