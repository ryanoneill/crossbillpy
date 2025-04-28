"""This package contains the Crossbill http package.

Package: crossbill.http

Description:
Crossbill http provides the components necessary to create clients and servers
that operate on http requests and responses.
"""

from .method import Method
from .status import Status

__all__ = [
    "Method",
    "Status",
]
