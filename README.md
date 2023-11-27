# Game Of Life (golife)

[![Build](https://github.com/BrianLusina/game-of-life/actions/workflows/build.yml/badge.svg)](https://github.com/BrianLusina/game-of-life/actions/workflows/build.yml)
[![Lint](https://github.com/BrianLusina/game-of-life/actions/workflows/lint.yml/badge.svg)](https://github.com/BrianLusina/game-of-life/actions/workflows/lint.yml)
[![Tests](https://github.com/BrianLusina/game-of-life/actions/workflows/tests.yaml/badge.svg)](https://github.com/BrianLusina/game-of-life/actions/workflows/tests.yaml)

Inspired by [John Horton Conway's](https://en.wikipedia.org/wiki/John_Horton_Conway)
[Game of life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).
This is a [cellular automaton](https://en.wikipedia.org/wiki/Cellular_automaton) simulation whose evolution depends on
its initial state and does not require further input from any player.

## Pre-requisites

1. Ensure that you have [Python version 3.12.0](https://www.python.org/) setup locally, you can set this up
   using [pyenv](https://github.com/pyenv/pyenv) if you have multiple versions of Python on your local development
   environment.
2. [Poetry](https://python-poetry.org/) is used for managing dependencies, ensure you have that setup locally.
3. [Virtualenv](https://virtualenv.pypa.io/) Not a hard requirement as poetry should setup a virtual environment for
   you, but can be used as well to setup a virtual environment.

## Setup

1. After cloning the project, install the dependencies required with:

   ```shell
   poetry install
   ```
   > When using poetry

   Or
   ```shell
   make install
   ```
   > When using [GNU Make](https://www.gnu.org/s/make/manual/make.html), this is a wrapper around the top commend

2. Install `golife` in editable mode:
   ```shell
   cd golife
   pip install -e .
   ```

## Execution

To execute `golife`, go ahead and run the below command:

```shell
golife -a
```
