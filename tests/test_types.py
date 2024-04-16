from typing import TYPE_CHECKING

from omc4py import open_session


def test_session_types() -> None:
    if TYPE_CHECKING:
        from omc4py import (
            AsyncSession,
            Session,
            v_1_13,
            v_1_14,
            v_1_15,
            v_1_16,
            v_1_17,
            v_1_18,
            v_1_19,
            v_1_20,
            v_1_21,
            v_1_22,
            v_1_23,
        )

        a: Session
        b: AsyncSession
        a_13: v_1_13.Session
        b_13: v_1_13.AsyncSession
        a_14: v_1_14.Session
        b_14: v_1_14.AsyncSession
        a_15: v_1_15.Session
        b_15: v_1_15.AsyncSession
        a_16: v_1_16.Session
        b_16: v_1_16.AsyncSession
        a_17: v_1_17.Session
        b_17: v_1_17.AsyncSession
        a_18: v_1_18.Session
        b_18: v_1_18.AsyncSession
        a_19: v_1_19.Session
        b_19: v_1_19.AsyncSession
        a_20: v_1_20.Session
        b_20: v_1_20.AsyncSession
        a_21: v_1_21.Session
        b_21: v_1_21.AsyncSession
        a_22: v_1_22.Session
        b_22: v_1_22.AsyncSession
        a_23: v_1_23.Session
        b_23: v_1_23.AsyncSession

        a_13 = open_session(version=(1, 13))
        a_13 = open_session(version=(1, 13), asyncio=False)  # noqa: F841
        b_13 = open_session(version=(1, 13), asyncio=True)  # noqa: F841

        a_14 = open_session(version=(1, 14))
        a_14 = open_session(version=(1, 14), asyncio=False)  # noqa: F841
        b_14 = open_session(version=(1, 14), asyncio=True)  # noqa: F841

        a_15 = open_session(version=(1, 15))
        a_15 = open_session(version=(1, 15), asyncio=False)  # noqa: F841
        b_15 = open_session(version=(1, 15), asyncio=True)  # noqa: F841

        a_16 = open_session(version=(1, 16))
        a_16 = open_session(version=(1, 16), asyncio=False)  # noqa: F841
        b_16 = open_session(version=(1, 16), asyncio=True)  # noqa: F841

        a_17 = open_session(version=(1, 17))
        a_17 = open_session(version=(1, 17), asyncio=False)  # noqa: F841
        b_17 = open_session(version=(1, 17), asyncio=True)  # noqa: F841

        a_18 = open_session(version=(1, 18))
        a_18 = open_session(version=(1, 18), asyncio=False)  # noqa: F841
        b_18 = open_session(version=(1, 18), asyncio=True)  # noqa: F841

        a_19 = open_session(version=(1, 19))
        a_19 = open_session(version=(1, 19), asyncio=False)  # noqa: F841
        b_19 = open_session(version=(1, 19), asyncio=True)  # noqa: F841

        a_20 = open_session(version=(1, 20))
        a_20 = open_session(version=(1, 20), asyncio=False)  # noqa: F841
        b_20 = open_session(version=(1, 20), asyncio=True)  # noqa: F841

        a_21 = open_session(version=(1, 21))
        a_21 = open_session(version=(1, 21), asyncio=False)  # noqa: F841
        b_21 = open_session(version=(1, 21), asyncio=True)  # noqa: F841

        a_22 = open_session(version=(1, 22))
        a_22 = open_session(version=(1, 22), asyncio=False)  # noqa: F841
        b_22 = open_session(version=(1, 22), asyncio=True)  # noqa: F841

        a_23 = open_session(version=(1, 23))
        a_23 = open_session(version=(1, 23), asyncio=False)  # noqa: F841
        b_23 = open_session(version=(1, 23), asyncio=True)  # noqa: F841

        a_24 = open_session(version=(1, 24))
        a_24 = open_session(version=(1, 24), asyncio=False)  # noqa: F841
        b_24 = open_session(version=(1, 24), asyncio=True)  # noqa: F841
        a_24 = open_session(version=(1, 25))
        a_24 = open_session(version=(1, 25), asyncio=False)  # noqa: F841
        b_24 = open_session(version=(1, 25), asyncio=True)  # noqa: F841
        a_24 = open_session(version=(1, 26))
        a_24 = open_session(version=(1, 26), asyncio=False)  # noqa: F841
        b_24 = open_session(version=(1, 26), asyncio=True)  # noqa: F841

        a = open_session()
        a = open_session(asyncio=False)  # noqa: F841
        b = open_session(asyncio=True)  # noqa: F841
