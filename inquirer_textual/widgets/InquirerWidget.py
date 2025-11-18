from __future__ import annotations

from typing import Any

from textual.message import Message
from textual.widget import Widget


class InquirerWidget(Widget):
    class Submit(Message):
        def __init__(self, value: Any, command: str | None = "select"):
            super().__init__()
            self.value = value
            self.command = command

    def __init__(self, mandatory: bool = True):
        super().__init__()
        self.mandatory = mandatory

    def on_mount(self):
        if not self.mandatory:
            self._bindings.bind('ctrl+c', 'exit_now', show=False)

    def action_exit_now(self):
        self.post_message(InquirerWidget.Submit(None, 'ctrl+c'))

    def current_value(self):
        raise NotImplementedError("Subclasses must implement current_value method")
