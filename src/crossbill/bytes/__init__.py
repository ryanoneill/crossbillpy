"""This package contains the Crossbill bytes package.

Package: crossbill.bytes

Description:
Crossbill bytes provides the components necessary to create clients and
servers that operate on bytes.
For example:
* BytesPipelineFactory
* BytesRequest
* BytesRequestCodec
* BytesResponse
* BytesResponseCodec
"""

from .pipeline_factory import BytesPipelineFactory
from .request import BytesRequest
from .request_codec import BytesRequestCodec
from .response import BytesResponse
from .response_codec import BytesResponseCodec

__all__ = [
    "BytesPipelineFactory",
    "BytesRequest",
    "BytesRequestCodec",
    "BytesResponse",
    "BytesResponseCodec",
]
