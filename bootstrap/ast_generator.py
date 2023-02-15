from __future__ import annotations

from ast import (
    AnnAssign,
    Assign,
    Call,
    ClassDef,
    Ellipsis,
    Expr,
    FunctionDef,
    ImportFrom,
    Index,
    Load,
    Name,
    NameConstant,
    Num,
    Store,
    Str,
    Subscript,
    Tuple,
    alias,
    arg,
    arguments,
    expr,
    keyword,
)
from collections.abc import Iterable, Iterator
from itertools import product
from typing import NewType

from .util import countup

Dimension = NewType("Dimension", int)


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


def iter_ndarray_class_defs(dims: Iterable[int]) -> Iterator[ClassDef]:
    for dim in map(Dimension, dims):
        yield _ndarray_class_def(dim)


def _ndarray_class_def(dim: Dimension) -> ClassDef:
    item_type: expr
    if dim == 1:
        item_type = Name(id="DType", ctx=Load())
    else:
        item_type = Subscript(
            value=Name(id=f"_NDArray__{dim-1}", ctx=Load()),
            slice=Index(
                value=Tuple(
                    elts=[
                        Name(id="DType", ctx=Load()),
                        *(
                            Name(id=f"Size{i}", ctx=Load())
                            for i in countup(2, dim - 1)
                        ),
                    ],
                    ctx=Load(),
                )
            ),
            ctx=Load(),
        )
    return ClassDef(
        name=f"_NDArray__{dim}",
        bases=[
            Subscript(
                value=Name(id="Generic", ctx=Load()),
                slice=Index(
                    value=Tuple(
                        elts=[
                            Name(id="DType", ctx=Load()),
                            *(
                                Name(id=f"Size{i}", ctx=Load())
                                for i in range(1, dim + 1)
                            ),
                        ],
                        ctx=Load(),
                    )
                ),
                ctx=Load(),
            ),
            Subscript(
                value=Name(id="Sequence", ctx=Load()),
                slice=Index(value=item_type),
                ctx=Load(),
            ),
        ],
        keywords=[],
        body=[
            AnnAssign(
                target=Name(id="ndim", ctx=Store()),
                annotation=Subscript(
                    value=Name(id="Literal", ctx=Load()),
                    slice=Index(value=Num(n=dim)),
                    ctx=Load(),
                ),
                value=None,
                simple=1,
            ),
            AnnAssign(
                target=Name(id="shape", ctx=Store()),
                annotation=Subscript(
                    value=Name(id="tuple", ctx=Load()),
                    slice=Index(
                        value=Tuple(
                            elts=[
                                *(
                                    Name(id=f"Size{i}", ctx=Load())
                                    for i in range(1, dim + 1)
                                ),
                            ],
                            ctx=Load(),
                        )
                    ),
                ),
                value=None,
                simple=1,
            ),
            FunctionDef(
                name="__len__",
                args=arguments(
                    args=[arg(arg="self", annotation=None)],
                    vararg=None,
                    kwonlyargs=[],
                    kw_defaults=[],
                    kwarg=None,
                    defaults=[],
                    posonlyargs=[],
                ),
                body=[Expr(value=Ellipsis())],
                decorator_list=[],
                returns=Name(id="Size1", ctx=Load()),
                lineno=None,
            ),
            FunctionDef(
                name="__getitem__",
                args=arguments(
                    args=[
                        arg(arg="self", annotation=None),
                        arg(
                            arg="index",
                            annotation=Subscript(
                                value=Name(id="Union", ctx=Load()),
                                slice=Index(
                                    value=Tuple(
                                        elts=[
                                            Name(id="int", ctx=Load()),
                                            Subscript(
                                                value=Name(
                                                    id="tuple", ctx=Load()
                                                ),
                                                slice=Index(
                                                    value=Name(
                                                        id="int", ctx=Load()
                                                    )
                                                ),
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    )
                                ),
                                ctx=Load(),
                            ),
                        ),
                    ],
                    vararg=None,
                    kwonlyargs=[],
                    kw_defaults=[],
                    kwarg=None,
                    defaults=[],
                    posonlyargs=[],
                ),
                body=[Expr(value=Ellipsis())],
                decorator_list=[Name(id="overload", ctx=Load())],
                returns=item_type,
                lineno=None,
            ),
            FunctionDef(
                name="__getitem__",
                args=arguments(
                    args=[
                        arg(arg="self", annotation=None),
                        arg(
                            arg="index",
                            annotation=Subscript(
                                value=Name(id="Union", ctx=Load()),
                                slice=Index(
                                    value=Tuple(
                                        elts=[
                                            Name(id="slice", ctx=Load()),
                                            Subscript(
                                                value=Name(
                                                    id="tuple", ctx=Load()
                                                ),
                                                slice=Index(
                                                    value=Name(
                                                        id="slice", ctx=Load()
                                                    )
                                                ),
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    )
                                ),
                                ctx=Load(),
                            ),
                        ),
                    ],
                    vararg=None,
                    kwonlyargs=[],
                    kw_defaults=[],
                    kwarg=None,
                    defaults=[],
                    posonlyargs=[],
                ),
                body=[Expr(value=Ellipsis())],
                decorator_list=[Name(id="overload", ctx=Load())],
                returns=Subscript(
                    value=Name(id=f"_NDArray__{dim}", ctx=Load()),
                    slice=Index(
                        value=Tuple(
                            elts=[
                                Name(id="DType", ctx=Load()),
                                *(
                                    Name(
                                        id="int" if i == 1 else f"Size{i}",
                                        ctx=Load(),
                                    )
                                    for i in countup(1, dim)
                                ),
                            ],
                            ctx=Load(),
                        )
                    ),
                    ctx=Load(),
                ),
                lineno=None,
            ),
        ],
        decorator_list=[],
    )


def iter_array_overload_function_defs(
    dims: Iterable[int],
) -> Iterator[FunctionDef]:
    for dim in map(Dimension, [0, *dims]):
        yield from array_overload_function_defs(dim)


def array_overload_function_defs(dim: Dimension) -> Iterator[FunctionDef]:
    annotation = Name(id="DType", ctx=Load())
    for _ in range(dim):
        annotation = Subscript(
            value=Name(id="Sequence", ctx=Load()),
            slice=Index(value=annotation),
            ctx=Load(),
        )

    object_arg = arg(arg="object", annotation=annotation)
    dtype_kwonlyarg = arg(
        arg="dtype",
        annotation=Subscript(
            value=Name(id="Optional", ctx=Load()),
            slice=Index(
                value=Subscript(
                    value=Name(id="type", ctx=Load()),
                    slice=Index(value=Name(id="DType", ctx=Load())),
                    ctx=Load(),
                )
            ),
            ctx=Load(),
        ),
    )

    for explicit_sequence in product(*([(True, False)] * dim)):
        shape_kwonlyarg = arg(
            arg="shape",
            annotation=Subscript(
                value=Name(id="tuple", ctx=Load()),
                slice=Index(
                    value=Tuple(
                        elts=[
                            Name(id=f"SizeArg{i}", ctx=Load())
                            if explicit
                            else NameConstant(value=None)
                            for i, explicit in enumerate(
                                explicit_sequence, start=1
                            )
                        ],
                        ctx=Load(),
                    )
                ),
                ctx=Load(),
            ),
        )

        if dim == 0:
            returns = Name(id="DType", ctx=Load())
        else:
            returns = Subscript(
                value=Name(id=f"_NDArray__{dim}", ctx=Load()),
                slice=Index(
                    value=Tuple(
                        elts=[
                            Name(id="DType", ctx=Load()),
                            *(
                                Name(
                                    id=f"SizeArg{i}" if explicit else "int",
                                    ctx=Load(),
                                )
                                for i, explicit in enumerate(
                                    explicit_sequence, start=1
                                )
                            ),
                        ],
                        ctx=Load(),
                    )
                ),
                ctx=Load(),
            )

        yield FunctionDef(
            name="array",
            args=arguments(
                args=[object_arg],
                vararg=None,
                kwonlyargs=[
                    dtype_kwonlyarg,
                    shape_kwonlyarg,
                ],
                kw_defaults=[NameConstant(value=None), None],
                kwarg=None,
                defaults=[],
                posonlyargs=[],
            ),
            body=[Expr(value=Ellipsis())],
            decorator_list=[Name(id="overload", ctx=Load())],
            returns=returns,
            lineno=None,
        )
