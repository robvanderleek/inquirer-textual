from textual import getters
from textual.app import ComposeResult
from textual.containers import HorizontalGroup
from textual.widgets import Input

from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.widgets.InquirerWidget import InquirerWidget
from inquirer_textual.widgets.PromptMessage import PromptMessage


class InquirerNumber(InquirerWidget):
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
    app = getters.app(InquirerApp)

    def __init__(self, message: str):
        super().__init__()
        self.message = message
        self.input: Input | None = None

    def current_value(self):
        return self.input.value

    def on_input_submitted(self, _: Input.Submitted):
        self.app.select_current()

    def compose(self) -> ComposeResult:
        with HorizontalGroup():
            yield PromptMessage(self.message)
            self.input = Input(id="inquirer-number-input", type="integer")
            yield self.input
