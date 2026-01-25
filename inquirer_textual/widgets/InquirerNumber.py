from __future__ import annotations

from textual.app import ComposeResult
from textual.containers import HorizontalGroup
from textual.widgets import Input
from typing_extensions import Self, Literal

from inquirer_textual.common.PromptMessage import PromptMessage
from inquirer_textual.widgets.InquirerWidget import InquirerWidget


class InquirerNumber(InquirerWidget):
    """A number input widget that allows the user to input a numerical value."""

    DEFAULT_CSS = """
    InquirerNumber {
        height: auto;
    }
    #inquirer-number-input {
        border: none;
        background: $inquirer-textual-background;
        color: $inquirer-textual-input-color;
        padding: 0;
        height: 1;
    }
    """

    def __init__(self, message: str, name: str | None = None, input_type: Literal['integer', 'number'] = 'integer',
                 mandatory: bool = False):
        """
        Args:
            message (str): The prompt message to display.
            name (str | None): The name of the input field.
            input_type (Literal['integer', 'number']): The type of number input ('integer' or 'number').
            mandatory (bool): Whether the input is mandatory.
        """
        super().__init__(name=name, mandatory=mandatory)
        self.message = message
        self.input_type = input_type
        self.input: Input | None = None

    def on_input_submitted(self) -> None:
        self.submit_current_value()

    def focus(self, scroll_visible: bool = True) -> Self:
        if self.input:
            return self.input.focus(scroll_visible)
        else:
            return super().focus(scroll_visible)

    def current_value(self):
        if self.input and self.input.value:
            if self.input_type == 'integer':
                return int(self.input.value)
            elif self.input_type == 'number':
                return float(self.input.value)
        return None

    def compose(self) -> ComposeResult:
        with HorizontalGroup():
            yield PromptMessage(self.message)
            self.input = Input(id="inquirer-number-input", type=self.input_type)
            yield self.input
