from __future__ import annotations

__all__ = ("Component", "TypeName", "VariableName")

from typing import List, NamedTuple

from typing_extensions import Literal

from omc4py import TypeName, VariableName


class Component(NamedTuple):
    className: TypeName
    name: VariableName
    comment: str
    protected: Literal["protected", "public"]
    isFinal: bool
    isFlow: bool
    isStream: bool
    isReplaceable: bool
    variability: Literal["constant", "parameter", "discrete", "unspecified"]
    innerOuter: Literal["inner", "outer", "none"]
    inputOutput: Literal["input", "output", "unspecified"]
    dimensions: List[str]
