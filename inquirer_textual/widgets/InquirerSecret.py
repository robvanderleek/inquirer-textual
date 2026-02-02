from __future__ import annotations

from textual.app import ComposeResult
from textual.containers import HorizontalGroup
from textual.widgets import Input
from typing_extensions import Self

from inquirer_textual.common.Prompt import Prompt
from inquirer_textual.widgets.InquirerWidget import InquirerWidget


class InquirerSecret(InquirerWidget):
    """A secret input prompt that allows the user to enter a secret value (e.g., password)."""

    DEFAULT_CSS = """
    InquirerSecret {
        height: auto;
    }
    #inquirer-secret-input {
        border: none;
        color: $inquirer-textual-input-color;
        padding: 0;
        height: 1;
    }
    """

    def __init__(self, message: str, name: str | None = None, mandatory: bool = False):
        """
        Args:
            message (str): The prompt message to display.
        """
        super().__init__(name=name, mandatory=mandatory)
        self.message = message
        self.input: Input | None = None

    def on_input_submitted(self, submitted: Input.Submitted):
        self.post_message(InquirerWidget.Submit(submitted.value))

    def focus(self, scroll_visible: bool = True) -> Self:
        if self.input:
            return self.input.focus(scroll_visible)
        else:
            return super().focus(scroll_visible)

    def current_value(self):
        return self.input.value if self.input else None

    def compose(self) -> ComposeResult:
        with HorizontalGroup():
            yield Prompt(self.message)
            self.input = Input(id="inquirer-secret-input")
            self.input.password = True
            yield self.input
