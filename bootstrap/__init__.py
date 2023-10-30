import sys
import typing

import typing_extensions


def _monkey_patch_typing() -> None:
    if sys.version_info < (3, 8):
        for extension in [
            "Literal",
            "Protocol",
            "get_args",
            "get_origin",
            "runtime_checkable",
        ]:
            _extend_typing(extension)


def _extend_typing(attr: str) -> None:
    extension = getattr(typing_extensions, attr)
    if getattr(typing, attr, None) is not extension:
        setattr(typing, attr, extension)


_monkey_patch_typing()
