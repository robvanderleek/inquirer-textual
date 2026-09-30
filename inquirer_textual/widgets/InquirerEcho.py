from __future__ import annotations

from textual.app import ComposeResult
from textual.containers import VerticalScroll
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
        self._adjust_height()

    def _adjust_height(self):
        if self.app.is_inline:
            self.styles.height = 10
        else:
            self.styles.height = '1fr'

    def current_value(self):
        return None

    def compose(self) -> ComposeResult:
        with VerticalScroll():
            yield Static(self.content)
