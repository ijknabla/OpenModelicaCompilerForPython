from contextlib import ExitStack
from pathlib import Path
from tempfile import TemporaryDirectory

import pytest

from omc4py import Session
from omc4py.exception import OMCError


@pytest.mark.asyncio
async def test_relocate_functions(session: Session) -> None:
    s = session.asynchronous

    with ExitStack() as stack:
        directory = Path(stack.enter_context(TemporaryDirectory()))
        A_mo = directory / "A.mo"
        A_mo.write_text("function A end A;")

        success = (
            await s.OpenModelica.Scripting.Experimental.relocateFunctions(
                fileName=A_mo, names=[["", ""]]
            )
        )
        if not success:
            stack.enter_context(pytest.raises(OMCError))

        await s.__check__()
