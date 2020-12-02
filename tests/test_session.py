
from omc4py import (
    TypeName,
    open_session,
)
import pytest


def test_open_session():
    with open_session() as session:
        assert session is not None


@pytest.fixture
def session():
    with open_session() as session:
        yield session


def test_OpenModelica(
    session  # fixture
):
    assert session.isPackage("OpenModelica")
