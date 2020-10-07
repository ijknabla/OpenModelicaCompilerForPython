
__all__ = (
    "escape_py_string",
    "unescape_modelica_string",
)


from modelica_language.util import replace_all


modelica_char_escape_map = {
    "\\": r"\\",
    "\'": r"\'",
    '\"': r'\"',
    "\a": r"\a",
    "\b": r"\b",
    "\f": r"\f",
    "\n": r"\n",
    "\t": r"\t",
    "\v": r"\v",
}


def escape_py_string(
    py_string: str
) -> str:
    return replace_all(
        py_string,
        modelica_char_escape_map.items()
    )


def unescape_modelica_string(
    modelica_string: str
) -> str:
    return replace_all(
        modelica_string,
        [
            (escaped, orignal)
            for orignal, escaped in modelica_char_escape_map.items()
        ]
    )
