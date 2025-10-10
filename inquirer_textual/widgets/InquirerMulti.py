from typing import Any

from textual.app import ComposeResult
from textual.widgets import ContentSwitcher

from inquirer_textual.widgets.InquirerWidget import InquirerWidget


class InquirerMulti(InquirerWidget):
    """A prompt that allows the user to answer multiple prompts in sequence."""

    DEFAULT_CSS = """
        InquirerMulti {
            height: auto;
        }
    """

    def __init__(self, widgets: list[InquirerWidget]) -> None:
        """
        Args:
            widgets (list[InquirerWidget]): A list of InquirerWidget instances to present in sequence.
        """
        super().__init__()
        self.widgets = widgets
        self._current_widget_index = 0
        self._return_values: list[Any] = []

    def on_mount(self):
        self.query_one(ContentSwitcher).current = f'widget-{self._current_widget_index}'
        self.query_one(ContentSwitcher).visible_content.focus()

    def on_inquirer_widget_submit(self, message: InquirerWidget.Submit) -> None:
        self._return_values.append(message.value)
        self._current_widget_index += 1
        if self._current_widget_index < len(self.widgets):
            message.stop()
            self.query_one(ContentSwitcher).current = f'widget-{self._current_widget_index}'
            self.query_one(ContentSwitcher).visible_content.focus()
        else:
            message.value = self._return_values

    def compose(self) -> ComposeResult:
        with ContentSwitcher(initial=f'widget-{self._current_widget_index}'):
            for idx, widget in enumerate(self.widgets):
                widget.id = f'widget-{idx}'
                yield widget
