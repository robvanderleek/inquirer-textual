# CLI

Through the `inq` CLI, prompts can be used used in your shell commands/scripts. For example, to show a checkbox:

```shell
uvx inq checkbox -m "Choose your toppings" -c Pepperoni -c Mushrooms -c Onions`
```

![Example](cli.gif)

## Installation

### uvx

Running the CLI with `uvx` (part of `uv`), does not require any installation:

```shell
uvx inq checkbox -m "Choose your toppings" -c Pepperoni -c Mushrooms -c Onions`
```

### Homebrew

There's a tap available to install `inq` via Homebrew:

```shell
brew tap robvanderleek/inq
```

```shell
brew install inq
```
