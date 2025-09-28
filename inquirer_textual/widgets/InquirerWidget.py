from typing import Any

from textual.message import Message
from textual.widget import Widget


class InquirerWidget(Widget):
    class Submit(Message):
        def __init__(self, value: Any):
            super().__init__()
            self.value = value

    def current_value(self):
        raise NotImplementedError("Subclasses must implement current_value method")
