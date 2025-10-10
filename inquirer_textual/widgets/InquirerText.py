from typing import Self, Iterable

from textual.app import ComposeResult
from textual.containers import HorizontalGroup
from textual.validation import Validator
from textual.widgets import Input

from inquirer_textual.widgets.InquirerWidget import InquirerWidget
from inquirer_textual.common.PromptMessage import PromptMessage


class InquirerText(InquirerWidget):
    """A text input prompt that allows the user to enter a string."""

    DEFAULT_CSS = """
    InquirerText {
        height: auto;
    }
    #inquirer-text-input {
        border: none;
        background: transparent;
        color: $input-color;
        padding: 0;
        height: 1;
    }
    """

    def __init__(self, message: str, default: str = '', validators: Validator | Iterable[Validator] | None = None):
        """
        Args:
            message (str): The prompt message to display.
            default (str): The default value if the user presses Enter without input.
            validators (Validator | Iterable[Validator] | None): A validator or list of validators to validate the
                input.
        """
        super().__init__()
        self.message = message
        self.input: Input | None = None
        self.default = default
        self.validators = validators

    def on_mount(self):
        super().on_mount()
        self.input.value = self.default

    def on_input_submitted(self, submitted: Input.Submitted):
        if self.validators is None or submitted.validation_result.is_valid:
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
            self.input = Input(id="inquirer-text-input", validators=self.validators)
            yield self.input
