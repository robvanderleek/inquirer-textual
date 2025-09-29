from typing import Self

from textual import getters
from textual.app import ComposeResult
from textual.containers import HorizontalGroup
from textual.widgets import Input

from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.widgets.InquirerWidget import InquirerWidget
from inquirer_textual.widgets.PromptMessage import PromptMessage


class InquirerSecret(InquirerWidget):
    DEFAULT_CSS = """
    InquirerSecret {
        height: auto;
    }
    #inquirer-secret-input {
        border: none;
        background: transparent;
        color: $input-color;
        padding: 0;
        height: 1;
    }
    """
    app = getters.app(InquirerApp)

    def __init__(self, message: str):
        super().__init__()
        self.message = message
        self.input: Input | None = None

    def on_input_submitted(self, submitted: Input.Submitted):
        self.post_message(InquirerWidget.Submit(submitted.value))

    def focus(self, scroll_visible: bool = True) -> Self:
        if self.input:
            return self.input.focus(scroll_visible)
        else:
            return super().focus(scroll_visible)

    def compose(self) -> ComposeResult:
        with HorizontalGroup():
            yield PromptMessage(self.message)
            self.input = Input(id="inquirer-secret-input")
            self.input.password = True
            yield self.input
