from omc4py.latest.aio import Session as BasicSession
from omc4py.modelica import external

from . import one

class OneSession(BasicSession):
    @external(".one")
    @classmethod
    async def one(_) -> one:
        raise NotImplementedError()
