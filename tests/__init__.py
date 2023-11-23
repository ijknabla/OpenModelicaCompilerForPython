from __future__ import annotations

from collections.abc import Callable
from typing import TYPE_CHECKING

from omc4py import Session

if TYPE_CHECKING:
    OpenSession = Callable[[], Session]
else:
    OpenSession = ...
