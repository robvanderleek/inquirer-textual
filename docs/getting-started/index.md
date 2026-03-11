# Getting Started

## Install

The first step is to install Inquirer-Textual.

Inside a virtual environemnt, this library can be installed with:

```shell
pip install inquirer-textual
```

Or, if you're using the [`uv`](https://docs.astral.sh/uv/) package manager:

```shell
uv add inquirer-textual
```

## Single prompt

The prompt API is very straightforward, for example to get a text input:

```python
--8<-- "docs/getting-started/single_prompt.py"
```

![Single prompt](single_prompt.gif)

## Multiple prompts

By calling the prompt API multiple times, a form-like inquiry can be done:

```python
--8<-- "docs/getting-started/multiple_prompts.py"
```

![Multiple prompts](multiple_prompts.gif)

It's also possible to use a single multi prompt:

```python
--8<-- "docs/getting-started/multi_prompt.py"
```

![multi prompt](multi_prompt.gif)

## Prompt settings

All prompts have a `settings` parameter of type `PromptSettings`.
The following fields can be configured on this class:

### clear

A boolean indicating whether to clear the prompt and result from the screen
after an answer was submitted (`True`), or (`False`, default) leave the prompt
and answer on the screen.

### mandatory

A boolean indicating whether a prompt needs to be ansewered (`True`), or
(`False`, default) a prompt can be skipped with `ctrl+C` and a `None` value is
returned.

### mouse

A boolean indicating whether mouse support is active (`True`), or (`False`,
default) a mouse is not supported.
