"""Module that includes the `PipelineFactory` abstract class."""

from abc import abstractmethod

from .pipeline import Pipeline
from .reqrep import ReqRepType
from .service import Service


class PipelineFactory(ReqRepType):
    """A `PipelineFactory` when called will create an instance of a `Pipeline`."""

    @abstractmethod
    async def __call__(self, service: Service) -> Pipeline:
        """Returns a `Pipeline` based on the provided `Service`."""
        raise NotImplementedError()
