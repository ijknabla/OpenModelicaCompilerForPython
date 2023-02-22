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
    Module,
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
from collections import defaultdict
from collections.abc import Collection, Iterable, Iterator
from itertools import product
from typing import NewType, Optional

from .util import countup

Dimension = NewType("Dimension", int)


def array_stub_module(
    types: Collection[int], dims: Collection[int], sizes: Collection[int]
) -> Module:
    dims_ = list(map(Dimension, dims))

    return Module(
        body=[
            *_iter_import_froms(
                [
                    ("__future__", ["annotations"]),
                    ("collections.abc", ["Sequence"]),
                    (
                        "typing",
                        [
                            "Any",
                            "Generic",
                            "TypeVar",
                            "Union",
                            "overload",
                        ],
                    ),
                    ("typing_extensions", ["Literal"]),
                ]
            ),
            *_iter_array_stub_type_vars(types=types, dims=dims_, sizes=sizes),
            *_iter_array_class_defs(types=types, dims=dims_),
            *_iter_nd_array_class_defs(dims=dims_),
        ],
        type_ignores=[],
    )


def _iter_import_froms(
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


def _iter_array_stub_type_vars(
    types: Collection[int], dims: Collection[Dimension], sizes: Collection[int]
) -> Iterator[Assign]:
    yield Assign(
        targets=[Name(id=_dtype_name(), ctx=Store())],
        value=Call(
            func=Name(id="TypeVar", ctx=Load()),
            args=[Str(s=_dtype_name())],
            keywords=[],
        ),
        lineno=None,
    )
    for typ in types:
        yield Assign(
            targets=[Name(id=_dtype_name(typ), ctx=Store())],
            value=Call(
                func=Name(id="TypeVar", ctx=Load()),
                args=[Str(s=_dtype_name(typ))],
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


def _iter_array_class_defs(
    types: Collection[int], dims: Collection[Dimension]
) -> Iterator[ClassDef]:
    yield ClassDef(
        name=_array_class_name(meta=True),
        bases=[Name(id="type", ctx=Load())],
        keywords=[],
        body=[
            *_iter_array_meta_class_getitem_overload_function_defs(
                types=types, dims=dims
            )
        ],
        decorator_list=[],
    )
    yield ClassDef(
        name=_array_class_name(),
        bases=[],
        keywords=[
            keyword(
                arg="metaclass",
                value=Name(id=_array_class_name(meta=True), ctx=Load()),
            )
        ],
        body=[Expr(value=Ellipsis())],
        decorator_list=[],
    )


def _iter_array_meta_class_getitem_overload_function_defs(
    types: Collection[int], dims: Collection[Dimension]
) -> Iterator[FunctionDef]:
    for dim, typ in product(dims, types):
        yield from _array_meta_class_getitem_overload_function_defs(typ, dim)


def _array_meta_class_getitem_overload_function_defs(
    type: int,
    dim: Dimension,
) -> Iterator[FunctionDef]:
    dtype_annotation: expr
    returns_dtype_annotation: expr
    if type == 1:
        dtype_annotation = _union_subscript(
            _tuple([_dtype_type(), _tuple_subscript(_tuple([_dtype_type()]))])
        )
        returns_dtype_annotation = _name(_dtype_name())
    else:
        dtype_annotation = _tuple_subscript(
            _tuple(
                [
                    _type_subscript(_name(_dtype_name(i)))
                    for i in countup(1, type)
                ]
            )
        )
        returns_dtype_annotation = _union_subscript(
            _tuple([_name(_dtype_name(i)) for i in countup(1, type)])
        )

    for explicit_sequence in product(*([(True, False)] * dim)):
        index_shape = [
            _name(f"SizeArg{i}") if explicit else NameConstant(value=None)
            for i, explicit in enumerate(explicit_sequence, start=1)
        ]
        returns_shape = [
            _name(f"SizeArg{i}" if explicit else "int")
            for i, explicit in enumerate(explicit_sequence, start=1)
        ]

        yield FunctionDef(
            name="__getitem__",
            args=arguments(
                args=[
                    arg(arg="cls", annotation=None),
                    arg(
                        arg="index",
                        annotation=_tuple_subscript(
                            _tuple(
                                [
                                    dtype_annotation,
                                    _tuple_subscript(_tuple(elts=index_shape)),
                                ]
                            )
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
            decorator_list=[_name("overload")],
            returns=_type_subscript(
                _subscript(
                    value=_name(_array_class_name(dim)),
                    slice=_tuple(
                        elts=[returns_dtype_annotation, *returns_shape]
                    ),
                )
            ),
            lineno=None,
        )


def _iter_nd_array_class_defs(
    dims: Collection[Dimension],
) -> Iterator[ClassDef]:
    for dim in map(Dimension, dims):
        yield _nd_array_class_def(dim)


def _nd_array_class_def(dim: Dimension) -> ClassDef:
    return ClassDef(
        name=_array_class_name(dim),
        bases=[
            Subscript(
                value=Name(id="Generic", ctx=Load()),
                slice=Index(
                    value=Tuple(
                        elts=[
                            Name(id=_dtype_name(), ctx=Load()),
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
                slice=Index(
                    value=_indexed_array_class_name(
                        map(Dimension, countup(2, dim - 1))
                    )
                ),
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
                name="__eq__",
                args=arguments(
                    args=[
                        arg(arg="self", annotation=None),
                        arg(
                            arg="other", annotation=Name(id="Any", ctx=Load())
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
                decorator_list=[],
                returns=Name(id="bool", ctx=Load()),
                lineno=None,
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
            *_iter_array_getitem_overload_function_defs(dim=dim),
        ],
        decorator_list=[],
    )


def _iter_array_getitem_overload_function_defs(
    dim: Dimension,
) -> Iterator[FunctionDef]:
    for index_annotation, returns_annotation in _iter_index_annotations(dim):
        yield FunctionDef(
            name="__getitem__",
            args=arguments(
                args=[
                    arg(arg="self", annotation=None),
                    arg(
                        arg="index",
                        annotation=index_annotation,
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
            returns=returns_annotation,
            lineno=None,
        )


def _iter_index_annotations(dim: Dimension) -> Iterator[tuple[expr, expr]]:
    categories: defaultdict[
        tuple[Optional[Dimension], ...], list[tuple[bool, ...]]
    ]
    categories = defaultdict(list)

    for n_index in countup(1, dim):
        for is_slice_seq in product(*([[False, True]] * n_index)):
            indices = (
                *([None] * sum(is_slice_seq)),
                *map(Dimension, countup(1, dim)[len(is_slice_seq) :]),
            )
            categories[indices].append(is_slice_seq)

    for indices, is_slice_seqseq in sorted(
        categories.items(), key=lambda item: len(item[0])
    ):
        annotations: list[expr]
        annotations = []
        for is_slice_seq in sorted(is_slice_seqseq):
            name, *names = list(map(_slice_or_int, is_slice_seq))
            if not names:
                annotations.extend(
                    [
                        name,
                        Subscript(
                            value=Name(id="tuple", ctx=Load()),
                            slice=Index(value=name),
                            ctx=Load(),
                        ),
                    ]
                )
            else:
                annotations.append(
                    Subscript(
                        value=Name(id="tuple", ctx=Load()),
                        slice=Index(
                            value=Tuple(elts=[name, *names], ctx=Load())
                        ),
                        ctx=Load(),
                    )
                )

        annotation, *annotations = annotations

        if annotations:
            annotation = Subscript(
                value=Name(id="Union", ctx=Load()),
                slice=Index(
                    value=Tuple(elts=[annotation, *annotations], ctx=Load())
                ),
                ctx=Load(),
            )

        yield annotation, _indexed_array_class_name(indices)


def _slice_or_int(is_slice: bool) -> Name:
    return Name(id="slice" if is_slice else "int", ctx=Load())


def _name(id: str) -> Name:
    return Name(id=id, ctx=Load())


def _subscript(value: expr, slice: expr) -> Subscript:
    return Subscript(value=value, slice=slice, ctx=Load())


def _tuple_subscript(slice: expr) -> Subscript:
    return _subscript(value=_name("tuple"), slice=slice)


def _type_subscript(slice: expr) -> Subscript:
    return _subscript(value=_name("type"), slice=slice)


def _union_subscript(slice: expr) -> Subscript:
    return _subscript(value=_name("Union"), slice=slice)


def _tuple(elts: Iterable[expr]) -> Tuple:
    return Tuple(elts=list(elts), ctx=Load())


def _dtype_name(type: Optional[int] = None) -> str:
    return "DType" + ("" if type is None else f"{type}")


def _dtype_type(type: Optional[int] = None) -> Subscript:
    return Subscript(
        value=Name(id="type", ctx=Load()),
        slice=Name(id=_dtype_name(type), ctx=Load()),
        ctx=Load(),
    )


def _array_class_name(
    dim: Optional[Dimension] = None, meta: bool = False
) -> str:
    prefix = "" if dim is None else f"_{dim}D"
    suffix = "" if not meta else "Meta"
    return f"{prefix}Array{suffix}"


def _indexed_array_class_name(indices: Iterable[Optional[Dimension]]) -> expr:
    indices = tuple(indices)
    if not indices:
        return Name(id=_dtype_name(), ctx=Load())
    else:
        return Subscript(
            value=Name(
                id=_array_class_name(Dimension(len(indices))), ctx=Load()
            ),
            slice=Index(
                value=Tuple(
                    elts=[
                        Name(id=_dtype_name(), ctx=Load()),
                        *(
                            Name(
                                id="int" if index is None else f"Size{index}",
                                ctx=Load(),
                            )
                            for index in indices
                        ),
                    ],
                    ctx=Load(),
                )
            ),
            ctx=Load(),
        )
