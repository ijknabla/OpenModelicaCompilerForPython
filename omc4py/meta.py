from __future__ import annotations

from collections.abc import ByteString, Mapping
from typing import TYPE_CHECKING, Any, Generic, TypeVar

from typing_extensions import Protocol, SupportsIndex, runtime_checkable

T_co = TypeVar("T_co", covariant=True)

if TYPE_CHECKING:
    _GenericMeta = type
    _ProtocolMeta = type
else:
    _GenericMeta = type(Generic)
    _ProtocolMeta = type(Protocol)


SEQUENCE_BUT_NOT_ARRAY = {ByteString, Mapping, memoryview, str}


class _SupportsArrayIndexingMeta(_ProtocolMeta):
    def __instancecheck__(cls, instance: Any) -> bool:
        return issubclass(type(instance), cls) and 0 < len(instance)

    def __subclasscheck__(cls, subclass: type[Any]) -> bool:
        return (
            not issubclass(subclass, tuple(SEQUENCE_BUT_NOT_ARRAY))
            and hasattr(subclass, "__len__")
            and hasattr(subclass, "__getitem__")
        )


@runtime_checkable
class SupportsArrayIndexing(
    Protocol[T_co], metaclass=_SupportsArrayIndexingMeta
):
    def __len__(self) -> int:
        ...

    def __getitem__(self, index: SupportsIndex) -> T_co:
        ...
