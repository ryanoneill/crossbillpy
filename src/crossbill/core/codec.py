"""Module that includes the `Codec` abstract class."""

from abc import abstractmethod
from typing import Generic, TypeVar

InputType = TypeVar("InputType")
OutputType = TypeVar("OutputType")


class Codec(Generic[InputType, OutputType]):
    """A `Codec` transforms an `InputType` to an `OutputType` and back.

    A `Codec` contains an `encode` and `decode` method that are opposites of
    each other. The `encode` method transforms an instance of the `InputType`
    into an instance of the `OutputType`. The `decode` method transforms an
    instance of the `OutputType` into an instance of the `InputType`.

    Ideally, these functions should be inverses of each other. However, that is
    not always the case. For example, if a non-optimized representation of the
    `InputType` is passed to `encode`, and then passed to `decode` an optimized
    representation of the `InputType` could result, and should not be seen as
    wrong.
    """

    @abstractmethod
    async def encode(self, data: InputType) -> OutputType:
        """Asynchronously transfrom the `InputType` to the `OutputType`.

        This version of the `encode` method is abstract and should be
        implemented by concrete `Codec`s.
        """
        raise NotImplementedError()

    @abstractmethod
    async def decode(self, data: OutputType) -> InputType:
        """Asynchronously transform the `OutputType` to the `InputType`.

        This version of the `decode` method is abstract and should be
        implemented by concrete `Codec`s.
        """
        raise NotImplementedError()


class IdentityCodec(Codec[InputType, InputType]):
    """An `IdentityCodec` is a `Codec` that performs no transformations.

    An `IdentityCodec` is a `Codec` that has the same `InputType` and
    `OutputType`, but also doesn't modify its contents. For example, a `Codec`
    that reverses a string will have `str` as both the `InputType` and
    `OutputType`, but that would not be an `IdentityCodec` because the data
    is being reversed and then reversed back again. For an `IdentityCodec`,
    calling `encode` or `decode` will have no effect on the data provided.
    """

    async def encode(self, data: InputType) -> InputType:
        """Asynchronously return the `InputType` data passed in."""
        return data

    async def decode(self, data: InputType) -> InputType:
        """Asynchronously return the `InputType` data passed in."""
        return data
