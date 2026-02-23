from __future__ import annotations

from textual import events
from textual.app import ComposeResult
from textual.containers import HorizontalGroup

from inquirer_textual.common.Prompt import Prompt
from inquirer_textual.widgets.InquirerWidget import InquirerWidget


class InquirerWaitForKey(InquirerWidget):
    """A prompt that waits for the user to press a key."""

    DEFAULT_CSS = """
    InquirerWaitForKey {
        height: auto;
    }
    """
    can_focus = True

    def __init__(self, message: str, key: str = 'enter', name: str | None = None, mandatory: bool = False):
        """
        Args:
            message (str): The prompt message to display.
            key (str): The key to wait for (default is 'enter').
            name (str | None): The name of the prompt.
            mandatory (bool): Whether a response is mandatory.
        """
        super().__init__(name=name, mandatory=mandatory)
        self.message = message
        self.key = key

    def on_key(self, event: events.Key):
        if event.key == self.key:
            self.submit_current_value()

    def current_value(self):
        return None

    def compose(self) -> ComposeResult:
        with HorizontalGroup():
            yield Prompt(self.message)
