from contextlib import AbstractContextManager as _AbstractContextManager
from typing import Any
from typing import Literal as _Literal

PAIR: _Literal[0]
PUB: _Literal[1]
SUB: _Literal[2]
REQ: _Literal[3]
REP: _Literal[4]
DEALER: _Literal[5]
ROUTER: _Literal[6]
PULL: _Literal[7]
PUSH: _Literal[8]

class Context:
    def __init__(self, io_threads: int = ...) -> None: ...
    def socket(
        self,
        socket_type: int,
    ) -> Socket: ...

class Socket(_AbstractContextManager["Socket"]):
    def connect(self, addr: str) -> _SocketContext: ...
    def recv_string(
        self,
        flags: int | None = ...,
        encoding: str = ...,
    ) -> str: ...
    def send_string(
        self,
        u: str,
        flags: int | None = ...,
        copy: bool | None = ...,
        encoding: str = ...,
    ) -> None: ...
    def __exit__(self, *exc_info: Any) -> None: ...

class _SocketContext: ...
