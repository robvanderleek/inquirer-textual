from inquirer_textual.widgets.InquirerWidget import InquirerWidget
from inquirer_textual.common.PromptMessage import PromptMessage
from textual import events
from textual.app import ComposeResult
from textual.containers import HorizontalGroup
from textual.widgets import Label


class InquirerConfirm(InquirerWidget):
    """A confirmation prompt that allows the user to confirm or reject."""

    DEFAULT_CSS = """
    InquirerConfirm {
        height: auto;
    }
    """
    can_focus = True

    def __init__(self, message: str, confirm_character: str = 'y', reject_character: str = 'n', default=False,
                 mandatory: bool = True):
        """
        Args:
            message (str): The prompt message to display.
            confirm_character (str): The character to use for confirmation.
            reject_character (str): The character to use for rejection.
            default (bool): The default value if the user presses Enter without input.
            mandatory (bool): Whether a response is mandatory.
        """
        super().__init__(mandatory)
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
            event.stop()
            self.post_message(InquirerWidget.Submit(self.value))

    def current_value(self):
        return self.value

    def compose(self) -> ComposeResult:
        with HorizontalGroup():
            yield PromptMessage(self.message)
            yield self.label
