from __future__ import annotations

from rich.text import Text
from textual.app import ComposeResult
from textual.containers import Vertical
from textual.widget import Widget
from textual.widgets import Static


class InquirerHeader(Widget):
    DEFAULT_CSS = """
        InquirerHeader {
            margin-bottom: 0;
        }
        
        .inquirer-header-static {
            width: 1fr;
        }
    """

    def __init__(self, text: str | Text | list[str | Text]) -> None:
        super().__init__()
        self._text = text if isinstance(text, list) else [text]

    def on_mount(self):
        self.styles.height = len(self._text)

    def compose(self) -> ComposeResult:
        with Vertical():
            for line in self._text:
                yield Static(line, classes="inquirer-header-static")
