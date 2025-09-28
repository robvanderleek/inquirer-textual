from typing import Any

from textual.widgets import ContentSwitcher

from inquirer_textual.widgets.InquirerWidget import InquirerWidget


class InquirerMulti(InquirerWidget):
    def __init__(self, widgets: list[InquirerWidget]) -> None:
        super().__init__()
        self.widgets = widgets
        self._current_widget_index = 0
        self._return_values: list[Any] = []

    def on_inquirer_widget_submit(self, message: InquirerWidget.Submit) -> None:
        self._return_values.append(message.value)
        self._current_widget_index += 1
        if self._current_widget_index < len(self.widgets):
            message.stop()
            self.query_one(ContentSwitcher).current = f'widget-{self._current_widget_index}'
            self.query_one(ContentSwitcher).visible_content.focus()
        else:
            message.value = self._return_values

    def compose(self):
        with ContentSwitcher(initial=f'widget-{self._current_widget_index}'):
            for idx, widget in enumerate(self.widgets):
                widget.id = f'widget-{idx}'
                yield widget
