from textual import events
from textual.app import ComposeResult
from textual.containers import HorizontalGroup
from textual.widgets import Label

from inquirer_textual.widgets.InquirerWidget import InquirerWidget
from inquirer_textual.widgets.PromptMessage import PromptMessage


class InquirerConfirm(InquirerWidget):
    """A simple clickable button."""
    DEFAULT_CSS = """
    InquirerConfirm {
        height: auto;
    }
    """
    can_focus = True

    def __init__(self, message: str, confirm_character: str = 'y', reject_character: str = 'n', default=False):
        super().__init__()
        if len(confirm_character) != 1 or len(reject_character) != 1:
            raise ValueError("confirm_character and reject_character must be a single character")
        if confirm_character.lower() == reject_character.lower():
            raise ValueError("confirm_character and reject_character must be different")
        self.message = message
        c = confirm_character if not default else confirm_character.upper()
        r = reject_character if default else reject_character.upper()
        self.label = Label(f'({c}/{r})')
        self.value: bool = default

    def on_key(self, event: events.Key):
        if event.key.lower() == 'y':
            self.value = True
            self.post_message(InquirerWidget.Submit(self.value))
        elif event.key.lower() == 'n':
            self.value = False
            self.post_message(InquirerWidget.Submit(self.value))
        elif event.key == 'enter':
            if self.value is None:
                self.value = True
            self.post_message(InquirerWidget.Submit(self.value))

    def current_value(self):
        return self.value

    def compose(self) -> ComposeResult:
        with HorizontalGroup():
            yield PromptMessage(self.message)
            yield self.label
