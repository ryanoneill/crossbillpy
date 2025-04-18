"""This package contains the Crossbill string package.

Package: crossbill.string

Description:
Crossbill string provides the components necessary to create clients and
servers that operate on strings.
For example:
* StringPipelineFactory
* StringRequest
* StringRequestCodec
* StringResponse
* StringResponseCodec
"""

from .pipeline_factory import StringPipelineFactory
from .request import StringRequest
from .request_codec import StringRequestCodec
from .response import StringResponse
from .response_codec import StringResponseCodec

__all__ = [
    "StringPipelineFactory",
    "StringRequest",
    "StringRequestCodec",
    "StringResponse",
    "StringResponseCodec",
]
