"""Module that includes the `Address` class."""

from dataclasses import dataclass


@dataclass
class Address:
    """Address is the encapsulation of a remote location.

    At this time, an `Address` is represented by a `host` and a `port`.
    """

    host: str
    port: int
