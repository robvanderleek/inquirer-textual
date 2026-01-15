# Getting Started

## Install

The first step is to install Inquirer-Textual.

Inside a virtual environemnt, this library can be installed with:

```shell
pip install inquirer-textual
```

## Simple text prompt

The prompt API is very straightforward, for example to get a text input:

```python
from inquirer_textual import prompts

if __name__ == "__main__":
    name = prompts.text('Enter your name:')
    print(f'Hello, {name}! 👋')
```

![Simple text prompt](simple_text_prompt.gif)
