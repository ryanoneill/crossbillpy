"""This package contains the Crossbill core package.

Package: crossbill.core

Description:
Crossbill core provides the abstractual core nouns of crossbill.
For example:
* Request
* Response
* Service
* Filter
* Codec
"""

from .request import Request, RequestType
from .response import Response, ResponseType
from .service import Service

__all__ = [
    "Request",
    "RequestType",
    "Response",
    "ResponseType",
    "Service",
]
