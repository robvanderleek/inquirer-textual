from textual import getters, events
from textual.app import ComposeResult
from textual.containers import HorizontalGroup
from textual.widgets import Label

from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.widgets.InquirerWidget import InquirerWidget
from inquirer_textual.widgets.PromptMessage import PromptMessage


class InquirerConfirm(InquirerWidget):
    DEFAULT_CSS = """
    InquirerText {
        height: auto;
    }
    #inquirer-text-input {
        border: none;
        background: transparent;
        padding: 0;
        height: 1;
    }
    """
    app = getters.app(InquirerApp)
    can_focus = True

    def __init__(self, message: str):
        super().__init__()
        self.message = message
        self.label = Label('(y/n)')
        self.value: bool | None = None

    # def on_mount(self) -> None:
    #     self.focus()

    def on_key(self, event: events.Key):
        if event.key.lower() == 'y':
            self.value = True
            self.app.select_current()
        elif event.key.lower() == 'n':
            self.value = False
            self.app.select_current()
        elif event.key == 'enter':
            if self.value is None:
                self.value = True
            self.app.select_current()

    def current_value(self):
        return self.value

    def compose(self) -> ComposeResult:
        with HorizontalGroup():
            yield PromptMessage(self.message)
            yield self.label
