import pytest

from crossbill.core import Closable


class BadResource(Closable):
    async def close(self) -> None:
        # Tell pyright to ignore warning here
        # as this is bad on purpose
        return await super().close()  # pyright: ignore


class GoodResource(Closable):
    def __init__(self) -> None:
        self.is_open = True

    async def close(self) -> None:
        self.is_open = False


async def test_bad_closable() -> None:
    resource = BadResource()
    with pytest.raises(NotImplementedError):
        await resource.close()


async def test_good_closable() -> None:
    resource = GoodResource()
    assert resource.is_open
    await resource.close()
    assert not resource.is_open
