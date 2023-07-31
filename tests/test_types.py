from typing import TYPE_CHECKING

from omc4py import open_session


def test_session_types() -> None:
    if TYPE_CHECKING:
        from omc4py import (
            v_1_13,
            v_1_14,
            v_1_15,
            v_1_16,
            v_1_17,
            v_1_18,
            v_1_19,
            v_1_20,
            v_1_21,
        )

        a_13: v_1_13.Session
        b_13: v_1_13.aio.Session
        a_14: v_1_14.Session
        b_14: v_1_14.aio.Session
        a_15: v_1_15.Session
        b_15: v_1_15.aio.Session
        a_16: v_1_16.Session
        b_16: v_1_16.aio.Session
        a_17: v_1_17.Session
        b_17: v_1_17.aio.Session
        a_18: v_1_18.Session
        b_18: v_1_18.aio.Session
        a_19: v_1_19.Session
        b_19: v_1_19.aio.Session
        a_20: v_1_20.Session
        b_20: v_1_20.aio.Session
        a_21: v_1_21.Session
        b_21: v_1_21.aio.Session

        a_13 = open_session(version=(0, 0))
        a_13 = open_session(version=(0, 0), asyncio=False)
        b_13 = open_session(version=(0, 0), asyncio=True)

        a_13 = open_session(version=(1, 0))
        a_13 = open_session(version=(1, 0), asyncio=False)
        b_13 = open_session(version=(1, 0), asyncio=True)
        a_13 = open_session(version=(1, 1))
        a_13 = open_session(version=(1, 1), asyncio=False)
        b_13 = open_session(version=(1, 1), asyncio=True)
        a_13 = open_session(version=(1, 2))
        a_13 = open_session(version=(1, 2), asyncio=False)
        b_13 = open_session(version=(1, 2), asyncio=True)
        a_13 = open_session(version=(1, 3))
        a_13 = open_session(version=(1, 3), asyncio=False)
        b_13 = open_session(version=(1, 3), asyncio=True)
        a_13 = open_session(version=(1, 4))
        a_13 = open_session(version=(1, 4), asyncio=False)
        b_13 = open_session(version=(1, 4), asyncio=True)
        a_13 = open_session(version=(1, 5))
        a_13 = open_session(version=(1, 5), asyncio=False)
        b_13 = open_session(version=(1, 5), asyncio=True)
        a_13 = open_session(version=(1, 6))
        a_13 = open_session(version=(1, 6), asyncio=False)
        b_13 = open_session(version=(1, 6), asyncio=True)
        a_13 = open_session(version=(1, 7))
        a_13 = open_session(version=(1, 7), asyncio=False)
        b_13 = open_session(version=(1, 7), asyncio=True)
        a_13 = open_session(version=(1, 8))
        a_13 = open_session(version=(1, 8), asyncio=False)
        b_13 = open_session(version=(1, 8), asyncio=True)
        a_13 = open_session(version=(1, 9))
        a_13 = open_session(version=(1, 9), asyncio=False)
        b_13 = open_session(version=(1, 9), asyncio=True)
        a_13 = open_session(version=(1, 10))
        a_13 = open_session(version=(1, 10), asyncio=False)
        b_13 = open_session(version=(1, 10), asyncio=True)
        a_13 = open_session(version=(1, 11))
        a_13 = open_session(version=(1, 11), asyncio=False)
        b_13 = open_session(version=(1, 11), asyncio=True)
        a_13 = open_session(version=(1, 12))
        a_13 = open_session(version=(1, 12), asyncio=False)
        b_13 = open_session(version=(1, 12), asyncio=True)
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
        a_21 = open_session(version=(1, 22))
        a_21 = open_session(version=(1, 22), asyncio=False)  # noqa: F841
        b_21 = open_session(version=(1, 22), asyncio=True)  # noqa: F841
        a_21 = open_session(version=(1, 23))
        a_21 = open_session(version=(1, 23), asyncio=False)  # noqa: F841
        b_21 = open_session(version=(1, 23), asyncio=True)  # noqa: F841

        # a_21 = open_session(version=(2, 0))
        # a_21 = open_session(version=(2, 0), asyncio=False)  # noqa: F841
        # b_21 = open_session(version=(2, 0), asyncio=True)  # noqa: F841

        a_21 = open_session()
        a_21 = open_session(asyncio=False)  # noqa: F841
        b_21 = open_session(asyncio=True)  # noqa: F841
