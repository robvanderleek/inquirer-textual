from __future__ import annotations

from textual import events
from textual.app import ComposeResult
from textual.widgets import TextArea
from typing_extensions import Self

from inquirer_textual.common.Answer import Answer
from inquirer_textual.common.Choice import COMMAND_SELECT
from inquirer_textual.common.Prompt import Prompt
from inquirer_textual.widgets.InquirerWidget import InquirerWidget


class InquirerTextArea(InquirerWidget):
    """A text input prompt that allows the user to enter multiline text."""

    DEFAULT_CSS = """
    #inquirer-text-area-text-area {
        border: none;
        color: $inquirer-textual-input-color;
        padding: 0;
    }
    """

    def __init__(self, message: str, name: str | None = None, default: str = '', mandatory: bool = False,
                 height: int | str = 10):
        """
        Args:
            message (str): The prompt message to display.
            name (str | None): The name of the prompt, used as the key in the answers dictionary.
            default (str): The default value if the user presses Enter without input.
            mandatory (bool): Whether this prompt is mandatory.
            height (int | str | None): If None, for inline apps the height will be determined based on the number of
            choices.
        """
        super().__init__(name=name, mandatory=mandatory)
        self.message = message
        self.text_area: TextArea | None = None
        self.default = default
        self.selected_value: str | None = None
        self.show_result: bool = False
        self.height = height

    def on_mount(self):
        super().on_mount()
        self.styles.height = self.height

    def on_key(self, event: events.Key):
        if event.key == 'ctrl+enter':
            event.stop()
            if self.text_area and not self.text_area.text.endswith('\n'):
                self.text_area.text += '\n'
            self.submit_current_value()

    def focus(self, scroll_visible: bool = True) -> Self:
        if self.text_area:
            return self.text_area.focus(scroll_visible)
        else:
            return super().focus(scroll_visible)

    def current_value(self):
        return self.text_area.text if self.text_area else None

    async def on_command(self, command: str | None) -> None:
        self.selected_value = self.current_value() if command == COMMAND_SELECT else None
        self.styles.height = self.text_area.document.line_count if self.text_area else 1
        self.show_result = True
        await self.recompose()

    def compose(self) -> ComposeResult:
        if self.show_result:
            yield Prompt(self.message)
            if self.selected_value is not None:
                yield Answer(str(self.selected_value))
        else:
            yield Prompt(self.message)
            self.text_area = TextArea(self.default, id="inquirer-text-area-text-area")
            yield self.text_area
