<style>
.md-content .md-typeset h1 { display: none; }
</style>

<div align="center">
    <img src="assets/logo-light.png"/>
</div>

<p align="center"> <em>Versatile library for terminal user input in Python</em>
</p>

<div align="center">
    <a href="https://github.com/robvanderleek/inquirer-textual/actions/workflows/main.yml" target="_blank">
        <img src="https://github.com/robvanderleek/inquirer-textual/actions/workflows/main.yml/badge.svg" alt="Badge" class="off-glb">
    </a>
    <a href="https://mypy-lang.org/" target="_blank">
        <img src="https://www.mypy-lang.org/static/mypy_badge.svg" alt="Badge" class="off-glb">
    </a>
    <a href="https://github.com/astral-sh/ruff" target="_blank">
        <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json" alt="Badge" class="off-glb">
    </a>
    <a href="https://github.com/robvanderleek/inquirer-textual/blob/_codelimit_reports/main/codelimit.md" target="_blank">
        <img src="https://github.com/robvanderleek/inquirer-textual/blob/_codelimit_reports/main/badge.svg?raw=true" alt="Badge" class="off-glb">
    </a>
    <a href="https://pypi.org/project/inquirer-textual/" target="_blank">
        <img src="https://img.shields.io/pypi/v/inquirer-textual?label=pypi%20package" alt="Badge" class="off-glb">
    </a>
</div>

## Introduction

The goal of this Python library is to make user input simple, using a versatile
[set of prompts](prompts/checkbox.md).

Under the hood, this library uses the sophisticated
[Textual](https://textual.textualize.io/) TUI framework, which means you get:

- Rich prompts
- Inline or fullscreen prompts
- Mouse support
- Themes

## Example

![Example](prompts/checkbox.gif)

The Python code for the example above:

```python
--8<-- "examples/prompt_checkbox.py"
```

With `uv` you can run the example out of the box:

```shell
uv run --with inquirer-textual checkbox.py
```

## Installation

Create and activate a virtual environment (for example with
[uv](https://docs.astral.sh/uv/)), and then install this package:

```shell
pip install inquirer-textual
```

## Design principles

* **Keep simple things simple**: High-level prompts API for getting user input
* **Inquirer-like syntax**: API similar to many other Inquirer libraries
* **Single dependency**: The Textual TUI framework
