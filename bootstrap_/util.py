from __future__ import annotations


def countup(start: int, length: int, stride: int = 1) -> range:
    return range(
        start,
        start + stride * (length - 1) + (+1 if stride >= 0 else -1),
        stride,
    )
