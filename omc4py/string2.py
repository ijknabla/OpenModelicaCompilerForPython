from typing import Any, Tuple, Type, Union

from .modelica import enumeration, record
from .openmodelica import Component, TypeName, VariableName

_Primitive = Union[float, int, bool, str, TypeName, VariableName, Component]
_Defined = Union[record, enumeration, Tuple[Any, ...]]
_StringableType = Union[Type[Union[_Primitive, _Defined]], None]
