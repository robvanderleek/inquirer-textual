from typing import Any

from textual.app import ComposeResult

from inquirer_textual.widgets.InquirerWidget import InquirerWidget


class InquirerMulti(InquirerWidget):
    """A prompt that allows the user to answer multiple prompts in sequence."""

    DEFAULT_CSS = """
        InquirerMulti {
            height: auto;
        }
    """

    def __init__(self, widgets: dict[str, InquirerWidget]) -> None:
        """
        Args:
            widgets (dict[str, InquirerWidget]): A dictionary of InquirerWidget instances to present in sequence of definition.
        """
        super().__init__()
        self.widgets = widgets
        self._current_widget_index = 0
        self._return_values_dict: dict[str, Any] = {}

    async def on_inquirer_widget_submit(self, message: InquirerWidget.Submit) -> None:
        current_item = list(self.widgets.items())[self._current_widget_index]
        self._return_values_dict[current_item[0]] = message.value
        await current_item[1].on_command(message.command)
        self._current_widget_index += 1
        if self._current_widget_index < len(self.widgets):
            message.stop()
            next_widget = self.query_one(f'#widget-{self._current_widget_index}')
            next_widget.styles.display = 'block'
            next_widget.focus()
        else:
            message.value = self._return_values_dict

    def compose(self) -> ComposeResult:
        for idx, item in enumerate(self.widgets.items()):
            item[1].id = f'widget-{idx}'
            if idx > 0:
                item[1].styles.display = 'none'
            yield item[1]
