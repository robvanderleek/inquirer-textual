# Inquirer-Textual

<div align="center">

![Logo](https://raw.githubusercontent.com/robvanderleek/inquirer-textual/main/docs/assets/logo-light.png)

</div>

<div align="center">

  *Versatile library for user input in Python 🎙️*

</div>

<div align="center">

[![main](https://github.com/robvanderleek/inquirer-textual/actions/workflows/main.yml/badge.svg)](https://github.com/robvanderleek/inquirer-textual/actions/workflows/main.yml)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
[![Linting: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

</div>

All terminal programs start small. Some stay small, and some become incredibly
big. The goal of this Python library is to make user input simple for small
programs, while enabling a smooth transition to a comprehensive UI library as
your program grows.

Read the [documentation here](https://robvanderleek.github.io/inquirer-textual/)

## Installation

Create and activate a virtual environment (for example with
[uv](https://docs.astral.sh/uv/)), and then install this package:

```shell
pip install inquirer-textual
```

## Development

Add this library as an editable local dependency to another project using `uv`:

```shell
uv add --editable <path-to-inquirer-textual>
```

### Textual console

1. Open the Textual Development Console:

```shell
uv run textual console
```

2. Run application in development mode:

```shell
uv run textual run --dev examples/prompt_pattern.py
```

### Static documentation

Generating the static documentation:

```shell
uv run mkdocs build
```

Viewing the static documentation:

```shell
uv run mkdocs serve
```
