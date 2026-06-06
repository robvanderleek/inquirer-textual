from __future__ import annotations

from textual.containers import HorizontalGroup
from textual.widgets import Input
from typing_extensions import Literal

from inquirer_textual.common.Answer import Answer
from inquirer_textual.common.Choice import COMMAND_SELECT
from inquirer_textual.common.Prompt import Prompt
from inquirer_textual.widgets.base.InquirerWidget import InquirerWidget


class InquirerNumber(InquirerWidget):
    """A number input widget that allows the user to input a numerical value."""

    DEFAULT_CSS = """
    InquirerNumber {
        height: auto;
    }
    #inquirer-number-input {
        border: none;
        color: $inquirer-textual-input-color;
        padding: 0;
        height: 1;
    }
    """

    def __init__(self, message: str, name: str | None = None, default: int | float | None = None,
                 input_type: Literal['integer', 'number'] = 'integer', mandatory: bool = False):
        """
        Args:
            message (str): The prompt message to display.
            name (str | None): The name of the input field.
            default (int | float | None): The default value if the user presses Enter without input.
            input_type (Literal['integer', 'number']): The type of number input ('integer' or 'number').
            mandatory (bool): Whether the input is mandatory.
        """
        super().__init__(name=name, mandatory=mandatory)
        self.message = message
        self.default = default
        self.input_type = input_type
        self.input: Input | None = None
        self.selected_value: int | float | None = None
        self.show_result: bool = False

    def on_mount(self):
        super().on_mount()
        if self.default is not None:
            self.input.value = str(self.default)

    def on_input_submitted(self) -> None:
        self.submit_current_value()

    def focus(self, scroll_visible: bool = True):
        if self.input:
            return self.input.focus(scroll_visible)
        else:
            return super().focus(scroll_visible)

    async def on_command(self, command: str | None) -> None:
        self.selected_value = self.current_value() if command == COMMAND_SELECT else None
        self.show_result = True
        await self.recompose()

    def current_value(self):
        if self.input and self.input.value:
            if self.input_type == 'integer':
                return int(self.input.value)
            elif self.input_type == 'number':
                return float(self.input.value)
        return None

    def compose(self):
        if self.show_result:
            with HorizontalGroup():
                yield Prompt(self.message)
                if self.selected_value is not None:
                    yield Answer(str(self.selected_value))
        else:
            with HorizontalGroup():
                yield Prompt(self.message)
                self.input = Input(id="inquirer-number-input", type=self.input_type)
                yield self.input
