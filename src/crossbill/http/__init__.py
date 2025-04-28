"""This package contains the Crossbill http package.

Package: crossbill.http

Description:
Crossbill http provides the components necessary to create clients and servers
that operate on http requests and responses.
For example:
* HttpRequest
* HttpResponse
* Method
* Status
"""

from .method import Method
from .request import HttpRequest
from .response import HttpResponse
from .status import Status

__all__ = [
    "HttpRequest",
    "HttpResponse",
    "Method",
    "Status",
]
