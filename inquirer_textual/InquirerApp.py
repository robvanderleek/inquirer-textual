from typing import TypeVar

from textual.app import App
from textual.app import ComposeResult
from textual.widgets import Footer

from inquirer_textual.widgets.InquirerWidget import InquirerWidget
from inquirer_textual.common.Result import Result
from inquirer_textual.common.Shortcut import Shortcut

T = TypeVar('T')


class InquirerApp(App[Result[T]], inherit_bindings=False): # type: ignore[call-arg]
    CSS = """
        App {
            background: transparent;
        }
        Screen {
            border-top: none;
            border-bottom: none;
            background: transparent;
            height: auto;
        }
        """
    ENABLE_COMMAND_PALETTE = False
    INLINE_PADDING = 0

    def __init__(self, widget: InquirerWidget, shortcuts: list[Shortcut] | None = None, show_footer: bool = False):
        super().__init__()
        self.widget = widget
        self.shortcuts = shortcuts
        self.show_footer = show_footer

    def on_mount(self) -> None:
        if self.shortcuts:
            for shortcut in self.shortcuts:
                self._bindings.bind(shortcut.key, f'shortcut("{shortcut.command}")',
                                    description=shortcut.description,
                                    show=shortcut.show)

    def action_shortcut(self, command: str):
        self._exit_select(command)

    def on_inquirer_widget_submit(self, event: InquirerWidget.Submit) -> None:
        self.call_after_refresh(lambda: self.app.exit(Result(event.command, event.value)))

    def select_current(self):
        self._exit_select('select')

    def _exit_select(self, command: str):
        self.call_after_refresh(lambda: self.app.exit(Result(command, self.widget.current_value())))

    def compose(self) -> ComposeResult:
        yield self.widget
        if self.show_footer:
            yield Footer()

    def get_theme_variable_defaults(self) -> dict[str, str]:
        return {
            'select-question-mark': '#e5c07b',
            'select-list-item-highlight-foreground': '#61afef',
            'input-color': '#98c379'
        }
