from typing import TypeVar

from textual.app import App
from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Footer

T = TypeVar('T')


class InquirerApp(App[T]):
    CSS = """
        App {
            background: transparent;
        }
        Screen {
            border-top: none;
            border-bottom: none;
            background: transparent;
        }
        """
    ENABLE_COMMAND_PALETTE = False
    INLINE_PADDING = 0

    def __init__(self, widget: Widget, show_footer: bool = False):
        super().__init__()
        self.widget = widget
        self.show_footer = show_footer

    def compose(self) -> ComposeResult:
        yield self.widget
        if self.show_footer:
            yield Footer()

    def get_theme_variable_defaults(self) -> dict[str, str]:
        return {
            'select-question-mark': '#e5c07b',
            'select-list-item-highlight-foreground': '#61afef',
        }
