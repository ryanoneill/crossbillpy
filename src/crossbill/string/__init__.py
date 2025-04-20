"""This package contains the Crossbill string package.

Package: crossbill.string

Description:
Crossbill string provides the components necessary to create clients and
servers that operate on strings.
For example:
* StringClient
* StringEchoService
* StringPipelineFactory
* StringRequest
* StringRequestCodec
* StringResponse
* StringResponseCodec
* StringServer
* StringService
"""

from .client import StringClient
from .pipeline_factory import StringPipelineFactory
from .request import StringRequest
from .request_codec import StringRequestCodec
from .response import StringResponse
from .response_codec import StringResponseCodec
from .server import StringServer
from .service import StringEchoService, StringService

__all__ = [
    "StringClient",
    "StringEchoService",
    "StringPipelineFactory",
    "StringRequest",
    "StringRequestCodec",
    "StringResponse",
    "StringResponseCodec",
    "StringServer",
    "StringService",
]
