from __future__ import annotations

from ast import ImportFrom, alias
from collections.abc import Iterable, Iterator


def iter_import_froms(
    module_and_names: Iterable[tuple[str, Iterable[str]]],
) -> Iterator[ImportFrom]:
    for module, names in module_and_names:
        yield _import_from(module=module, names=names)


def _import_from(module: str, names: Iterable[str]) -> ImportFrom:
    return ImportFrom(
        module=module,
        names=[alias(name=name, asname=None) for name in names],
        level=0,
    )
