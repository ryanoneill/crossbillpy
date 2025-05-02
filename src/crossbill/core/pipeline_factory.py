"""Module that includes the `PipelineFactory` abstract class."""

from abc import abstractmethod
from typing import Generic

from .pipeline import Pipeline
from .request import RequestType
from .response import ResponseType
from .service import Service


class PipelineFactory(Generic[RequestType, ResponseType]):
    """A `PipelineFactory` when called will create an instance of a `Pipeline`."""

    @abstractmethod
    async def __call__(
        self, service: Service[RequestType, ResponseType]
    ) -> Pipeline[RequestType, ResponseType]:
        """Returns a `Pipeline` based on the provided `Service`."""
        raise NotImplementedError()
