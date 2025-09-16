from textual.app import ComposeResult
from textual.containers import HorizontalGroup
from textual.widget import Widget
from textual.widgets import Input

from inquirer_textual.widgets.PromptMessage import PromptMessage


class InquirerNumber(Widget):
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
        super().__init__()
        self.message = message

    def on_input_submitted(self, event: Input.Submitted):
        self.app.exit(event.value)

    def compose(self) -> ComposeResult:
        with HorizontalGroup():
            yield PromptMessage(self.message)
            yield Input(id="inquirer-number-input", type="integer")
