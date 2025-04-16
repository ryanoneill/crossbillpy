"""This package contains the Crossbill transport package.

Package: crossbill.transport

Description:
Crossbill transport provides the components necessary to make bytes go across
the wire.
For example:
* Bridge
"""

from .bridge import Bridge

__all__ = [
    "Bridge",
]
