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
</div>

## About

All terminal programs start small. Some stay small, and some become incredibly
big. The goal of this Python library is to make user input simple for small
programs, but also support a smooth transition to a comprehensive UI library as
your program grows.

This library is based on the sophisticated
[Textual](https://textual.textualize.io/) TUI framework.

## Example

![Example](prompts/checkbox.gif)

The Python code for the example above:

```python
--8<-- "examples/prompts/checkbox.py"
```

With `uv` you can run the example out of the box:

```shell
uv run --with inquirer-textual checkbox.py
```

## Key features and design principles

* **Keep simple things simple**: High-level prompts API for getting user input
* **Support evolving programs**: From small scripts to full-featured TUI
  applications
* **Inquirer-like syntax**: API similar to many other Inquirer libraries
* **Single dependency**: The Textual TUI framework
