from __future__ import annotations

from textual.app import ComposeResult
from textual.containers import HorizontalGroup
from textual.visual import VisualType
from textual.widgets import Static

from inquirer_textual.widgets.base.InquirerWidget import InquirerWidget


class InquirerEcho(InquirerWidget):
    """A prompt that just displays content"""

    DEFAULT_CSS = """
    InquirerEcho {
        height: auto;
    }
    """

    def __init__(self, content: VisualType, name: str | None = None, mandatory: bool = False):
        """
        Args:
            content (VisualType): The content to display.
            name (str | None): The name of the prompt.
            mandatory (bool): Whether a response is mandatory.
        """
        super().__init__(name=name, mandatory=mandatory)
        self.content = content

    def on_mount(self):
        super().on_mount()
        self.submit_current_value()

    def current_value(self):
        return None

    def compose(self) -> ComposeResult:
        with HorizontalGroup():
            yield Static(self.content)
