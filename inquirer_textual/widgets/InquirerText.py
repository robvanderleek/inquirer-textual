from textual.app import ComposeResult
from textual.containers import HorizontalGroup
from textual.widget import Widget
from textual.widgets import Input, Label


class InquirerText(Widget):
    DEFAULT_CSS = """
    #inquirer-text-label {
        margin-right: 1;
    }
    #inquirer-text-input {
        border: none;
        background: black 0%;
        padding: 0;
        height: 1;
    }
    """

    def __init__(self, message: str):
        super().__init__()
        self.message = message

    def on_mount(self):
        self.styles.height = 1

    def on_input_submitted(self, event: Input.Submitted):
        self.app.exit(event.value)

    def compose(self) -> ComposeResult:
        with HorizontalGroup():
            yield Label(self.message, id="inquirer-text-label")
            yield Input(id="inquirer-text-input")
