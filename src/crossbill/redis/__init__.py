"""This package contains the Crossbill redis package.

Package: crossbill.redis

Description:
Crossbill redis provides the components necessary to create clients and servers
that operate on redis commands and replies.
For example:
* SimpleStringCodec
"""

from .simple_string_codec import SimpleStringCodec

__all__ = [
    "SimpleStringCodec"
]
