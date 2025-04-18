"""This package contains the Crossbill string package.

Package: crossbill.string

Description:
Crossbill string provides the components necessary to create clients and
servers that operate on strings.
For example:
* StringRequest
* StringResponse
"""

from .request import StringRequest
from .response import StringResponse

__all__ = ["StringRequest", "StringResponse"]
