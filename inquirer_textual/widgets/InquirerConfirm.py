from __future__ import annotations

from textual import events
from textual.app import ComposeResult
from textual.containers import HorizontalGroup
from textual.widgets import Label

from inquirer_textual.common.Answer import Answer
from inquirer_textual.common.Choice import COMMAND_SELECT
from inquirer_textual.common.Prompt import Prompt
from inquirer_textual.widgets.InquirerWidget import InquirerWidget


class InquirerConfirm(InquirerWidget):
    """A confirmation prompt that allows the user to confirm or reject."""

    DEFAULT_CSS = """
    InquirerConfirm {
        height: auto;
    }
    """
    can_focus = True

    def __init__(self, message: str, confirm_character: str = 'y', reject_character: str = 'n', name: str | None = None,
                 default=False, mandatory: bool = False):
        """
        Args:
            message (str): The prompt message to display.
            confirm_character (str): The character to use for confirmation.
            reject_character (str): The character to use for rejection.
            name (str | None): The name of the prompt.
            default (bool): The default value if the user presses Enter without input.
            mandatory (bool): Whether a response is mandatory.
        """
        super().__init__(name=name, mandatory=mandatory)
        if len(confirm_character) != 1 or len(reject_character) != 1:
            raise ValueError("confirm_character and reject_character must be a single character")
        if confirm_character.lower() == reject_character.lower():
            raise ValueError("confirm_character and reject_character must be different")
        self.message = message
        self.confirm_character = confirm_character
        self.reject_character = reject_character
        c = confirm_character if not default else confirm_character.upper()
        r = reject_character if default else reject_character.upper()
        self.label = Label(f'({c}/{r})')
        self.value: bool = default
        self.selected_value: bool | None = None
        self.show_result: bool = False

    def on_key(self, event: events.Key):
        if event.key.lower() == 'y':
            self.value = True
            self.submit_current_value()
        elif event.key.lower() == 'n':
            self.value = False
            self.submit_current_value()
        elif event.key == 'enter':
            event.stop()
            self.submit_current_value()

    def current_value(self):
        return self.value

    async def on_command(self, command: str | None) -> None:
        self.selected_value = self.current_value() if command == COMMAND_SELECT else None
        self.styles.height = 1
        self.show_result = True
        await self.recompose()

    def compose(self) -> ComposeResult:
        if self.show_result:
            with HorizontalGroup():
                yield Prompt(self.message)
                if self.selected_value is not None:
                    yield Answer(self.confirm_character if self.selected_value else self.reject_character)
        else:
            with HorizontalGroup():
                yield Prompt(self.message)
                yield self.label
