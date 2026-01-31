from rich.text import Text
from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Static


class Answer(Widget):
    DEFAULT_CSS = """
        Answer {
            height: auto;
        }
        #inquirer-textual-answer {
            color: $inquirer-textual-input-color;
        }
        """

    def __init__(self, text: str):
        super().__init__()
        self.text = text

    def compose(self) -> ComposeResult:
        yield Static(Text(self.text), id='inquirer-textual-answer')
