
class OMCSessionBase:
    pass


class AsyncOMCSessionBase(
    OMCSessionBase,
):
    pass


class AsyncOMCSessionZMQ(
    AsyncOMCSessionBase,
):
    pass

    @classmethod
    def create(
        cls
    ):
        return cls()

    async def hello_world(self):
        print("hello_world!")

    async def __aenter__(self):
        return self

    async def __aexit__(
        self,
        exception_type,
        exception,
        traceback,
    ):
        pass
