
from omc4py import open_session


def test_open_session():
    with open_session() as session:
        assert session is not None
