from __future__ import annotations

from ast import (
    Assign,
    Call,
    ImportFrom,
    Index,
    Load,
    Name,
    Num,
    Store,
    Str,
    Subscript,
    alias,
    keyword,
)
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


def iter_ndarray_type_vars(
    dims: Iterable[int], sizes: Iterable[int]
) -> Iterator[Assign]:
    yield Assign(
        targets=[Name(id="DType", ctx=Store())],
        value=Call(
            func=Name(id="TypeVar", ctx=Load()),
            args=[
                Str(s="DType"),
                Name(id="float", ctx=Load()),
                Name(id="int", ctx=Load()),
                Name(id="bool", ctx=Load()),
                Name(id="str", ctx=Load()),
            ],
            keywords=[],
        ),
        lineno=None,
    )
    for dim in dims:
        yield Assign(
            targets=[Name(id=f"Size{dim}", ctx=Store())],
            value=Call(
                func=Name(id="TypeVar", ctx=Load()),
                args=[Str(s=f"Size{dim}")],
                keywords=[
                    keyword(arg="bound", value=Name(id="int", ctx=Load()))
                ],
            ),
            lineno=None,
        )

    for dim in dims:
        yield Assign(
            targets=[Name(id=f"SizeArg{dim}", ctx=Store())],
            value=Call(
                func=Name(id="TypeVar", ctx=Load()),
                args=[
                    Str(s=f"SizeArg{dim}"),
                    *(
                        Subscript(
                            value=Name(id="Literal", ctx=Load()),
                            slice=Index(value=Num(n=size)),
                            ctx=Load(),
                        )
                        for size in sizes
                    ),
                ],
                keywords=[],
            ),
            lineno=None,
        )
