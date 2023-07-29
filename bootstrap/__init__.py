from omc4py.interactive import open_interactives

from .session import Session


def open_session() -> Session:
    _, interactive = open_interactives("omc")
    return Session(interactive)
