from typing import Any

from textual.message import Message
from textual.widget import Widget


class InquirerWidget(Widget):
    class Submit(Message):
        def __init__(self, value: Any, command: str | None = "select"):
            super().__init__()
            self.value = value
            self.command = command

    def current_value(self):
        raise NotImplementedError("Subclasses must implement current_value method")
