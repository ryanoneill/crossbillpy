"""Module that provides the `Closable` Protocol."""

from abc import abstractmethod
from typing import Protocol


class Closable(Protocol):
    """`Closable` is a Protocol that indicates that the class has a `close` method."""

    @abstractmethod
    async def close(self) -> None:
        """Closes the resource. Should be concrete in implementation classes."""
        raise NotImplementedError()
