from contextlib import AbstractContextManager as _AbstractContextManager
from typing import Any

import zmq as _zmq

class Context:
    def __init__(self, io_threads: int = ...) -> None: ...
    def socket(
        self,
        socket_type: int,
    ) -> Socket: ...

class Socket(_AbstractContextManager["Socket"]):
    def connect(self, addr: str) -> _zmq._SocketContext: ...
    async def recv_string(
        self,
        flags: int | None = ...,
        encoding: str = ...,
    ) -> str: ...
    async def send_string(
        self,
        u: str,
        flags: int | None = ...,
        copy: bool | None = ...,
        encoding: str = ...,
    ) -> None: ...
    def __exit__(self, *exc_info: Any) -> None: ...
