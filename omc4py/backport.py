__all__ = (
    "Iterable",
    "Sequence",
)

import sys
from collections import defaultdict
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable, Sequence
else:
    if sys.version_info >= (3, 9):  # pragma: no cover
        from collections.abc import Iterable, Sequence
    else:  # pragma: no cover
        from collections.abc import Iterable as _Iterable
        from collections.abc import Sequence as _Sequence

        Iterable = defaultdict(lambda: _Iterable)
        Sequence = defaultdict(lambda: _Sequence)
