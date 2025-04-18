"""This package contains the Crossbill string package.

Package: crossbill.string

Description:
Crossbill string provides the components necessary to create clients and
servers that operate on strings.
For example:
* StringRequest
* StringRequestCodec
* StringResponse
* StringResponseCodec
"""

from .request import StringRequest
from .request_codec import StringRequestCodec
from .response import StringResponse
from .response_codec import StringResponseCodec

__all__ = [
    "StringRequest",
    "StringRequestCodec",
    "StringResponse",
    "StringResponseCodec",
]
