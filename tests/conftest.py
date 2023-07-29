from __future__ import annotations

from collections.abc import Generator

import pytest

from omc4py import latest, open_session


@pytest.fixture(scope="session")
def session() -> Generator[latest.Session, None, None]:
    with open_session() as session:
        yield session
