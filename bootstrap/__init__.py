from omc4py.compiler import AsyncOMCInteractive

from .session import Session


def open_session() -> Session:
    return Session(AsyncOMCInteractive.open())
