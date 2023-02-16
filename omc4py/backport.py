__all__ = ("Sequence",)

import sys
from typing import TYPE_CHECKING, Generic, TypeVar

T = TypeVar("T")

if TYPE_CHECKING:
    from collections.abc import Sequence
else:
    if sys.version_info >= (3, 9):  # pragma: no cover
        from collections.abc import Sequence
    else:  # pragma: no cover
        from collections.abc import Sequence as _Sequence

        class Sequence(_Sequence, Generic[T]):
            ...
