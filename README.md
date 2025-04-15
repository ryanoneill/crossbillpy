# Crossbill

## Description

TODO

## Getting Started

The `crossbill` project uses `uv`, "[a]n extremely fast Python package and
project manager, written in Rust." If you don't have it installed, follow
the [installation guide](https://docs.astral.sh/uv/getting-started/installation/)
in order to do so.

### Dependency Installation

With `uv` installed, run the following from the command line to ensure that all
dependencies are properly installed.

```shell
$ uv sync
```
### Testing

This project uses `pytest` along with `anyio` in order to run asynchronous
tests. A predominant number of tests within this library will fit that criteria
due to the nature of the domain space. See
[Testing with AnyIO](https://anyio.readthedocs.io/en/stable/testing.html) for
more information on the interplay between the two.

To run the existing unit tests, run the following from the command line.

```shell
$ uv run pytest
```



