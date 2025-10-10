from typing import Self

from textual.app import ComposeResult
from textual.containers import HorizontalGroup
from textual.widgets import Input

from inquirer_textual.widgets.InquirerWidget import InquirerWidget
from inquirer_textual.common.PromptMessage import PromptMessage


class InquirerNumber(InquirerWidget):
    """A number input widget that allows the user to input a numerical value."""

    DEFAULT_CSS = """
    InquirerNumber {
        height: auto;
    }
    #inquirer-number-input {
        border: none;
        background: transparent;
        color: $input-color;
        padding: 0;
        height: 1;
    }
    """

    def __init__(self, message: str):
        """
        Args:
            message (str): The prompt message to display.
        """
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

    def current_value(self):
        return self.input.value if self.input else None

    def compose(self) -> ComposeResult:
        with HorizontalGroup():
            yield PromptMessage(self.message)
            self.input = Input(id="inquirer-number-input", type="integer")
            yield self.input
