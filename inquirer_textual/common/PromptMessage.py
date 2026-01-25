from textual.app import ComposeResult
from textual.containers import HorizontalGroup
from textual.widget import Widget
from textual.widgets import Static, Label


class PromptMessage(Widget):
    DEFAULT_CSS = """
        PromptMessage {
            width: auto;
            height: auto;
        }
        #prompt-message-container {
            width: auto;
            margin-right: 1;
        }
        #prompt-message-question-mark {
            width: auto;
            color: $inquirer-textual-question-mark;
        }
        """

    def __init__(self, message: str):
        super().__init__()
        self.message = message

    def compose(self) -> ComposeResult:
        with HorizontalGroup(id='prompt-message-container'):
            yield Static('? ', id='prompt-message-question-mark')
            yield Label(self.message)
