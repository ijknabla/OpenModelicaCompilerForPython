from __future__ import annotations

from asyncio import AbstractEventLoop, get_event_loop
from collections.abc import Callable, Generator
from functools import wraps
from typing import TYPE_CHECKING, TypeVar

import pytest

import omc4py.modelica
from omc4py import Session, open_session

if TYPE_CHECKING:
    from typing_extensions import Concatenate, Never, ParamSpec

    from omc4py.modelica import MethodType, ReturnType, SelfType

    P = ParamSpec("P")
    T = TypeVar("T")

    Call = Callable[
        Concatenate[MethodType[P, T], str, dict[str, str], SelfType, P],
        ReturnType[T],
    ]


@pytest.fixture(scope="session")  # TODO: remove this fixture
def event_loop() -> AbstractEventLoop:
    return get_event_loop()


def wrap_call(call: Call[P, T]) -> Call[P, T]:
    @wraps(call)
    def wrapped(
        f: MethodType[P, T],
        funcname: str,
        rename: dict[str, str],
        self: SelfType,
        /,
        *args: P.args,
        **kwargs: P.kwargs,
    ) -> ReturnType[T]:
        f(self, *args, **kwargs)
        return call(f, funcname, rename, self, *args, **kwargs)

    return wrapped


@pytest.fixture
def session(
    _session: Session,
) -> Generator[Session, None, None]:
    yield _session
    _session.__check__()


@pytest.fixture(scope="session")
def _function_coverage() -> Generator[None, None, None]:
    with pytest.MonkeyPatch().context() as _monkeypatch:
        _monkeypatch.setattr(
            omc4py.modelica, "_call", wrap_call(omc4py.modelica._call)
        )
        yield


@pytest.fixture(scope="session")
def _session(_function_coverage: Never) -> Generator[Session, None, None]:
    with open_session() as session:
        yield session
