from textual.app import App
from textual.app import ComposeResult
from textual.binding import Binding
from textual.widget import Widget
from textual.widgets import Footer


class InquirerApp(App[str]):
    INLINE_PADDING = 0
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
    BINDINGS = [Binding("q", "quit", "Quit", priority=True)]

    def __init__(self, widget: Widget):
        super().__init__()
        self.widget = widget

    def compose(self) -> ComposeResult:
        yield self.widget
        yield Footer()
