from __future__ import annotations

from collections.abc import Callable, Generator
from contextlib import ExitStack
from functools import wraps
from typing import TYPE_CHECKING, TypeVar, cast

import pytest

import omc4py.modelica
from omc4py import Session
from tests import OpenSession

if TYPE_CHECKING:
    from typing_extensions import Concatenate, Never, ParamSpec

    from omc4py.modelica import MethodType, ReturnType, SelfType

    P = ParamSpec("P")
    T = TypeVar("T")

    Call = Callable[
        Concatenate[MethodType[P, T], str, dict[str, str], SelfType, P],
        ReturnType[T],
    ]


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
    assert set(map(str, _session.getClassNames())) == {
        "Complex",
        "Modelica",
        "ModelicaServices",
    }
    _session.__check__()


@pytest.fixture
def modelica_version(_session: Session) -> str:
    return _session.getVersion("Modelica")


@pytest.fixture
def open_session(
    _function_coverage: Never,
) -> Generator[OpenSession, None, None]:
    with ExitStack() as stack:

        def open_session() -> Session:
            from omc4py import open_session

            session = cast(Session, stack.enter_context(open_session()))
            stack.callback(session.__check__)
            return session

        yield open_session


@pytest.fixture(scope="session")
def _function_coverage() -> Generator[None, None, None]:
    with pytest.MonkeyPatch().context() as _monkeypatch:
        _monkeypatch.setattr(
            omc4py.modelica, "_call", wrap_call(omc4py.modelica._call)
        )
        yield


@pytest.fixture(scope="session")
def _session(_function_coverage: Never) -> Generator[Session, None, None]:
    from omc4py import open_session

    with open_session() as session:
        session.loadModel("Modelica")
        yield session
