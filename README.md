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

This project uses `pytest` along with `asyncio` in order to run asynchronous
tests. A predominant number of tests within this library will fit that criteria
due to the nature of the domain space. 

To run the existing unit tests, run the following from the command line.

```shell
$ uv run pytest
```

#### Coverage

This project uses `coverage` and `pytest-cov` for measuring code coverage. To
generate the report when running tests, run the following from the command line.

```shell
$ uv run pytest --cov
```
