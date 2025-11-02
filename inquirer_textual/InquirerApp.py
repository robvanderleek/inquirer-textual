from __future__ import annotations

from typing import TypeVar

from textual.app import App
from textual.app import ComposeResult
from textual.widgets import Footer

from inquirer_textual.common.Result import Result
from inquirer_textual.common.InquirerContext import InquirerContext
from inquirer_textual.widgets.InquirerWidget import InquirerWidget

T = TypeVar('T')


class InquirerApp(App[Result[T]], inherit_bindings=False):  # type: ignore[call-arg]
    CSS = """
        App {
            background: black;
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

    def __init__(self, context: InquirerContext):
        self.context = context
        super().__init__()

    def on_mount(self) -> None:
        if self.context.shortcuts:
            for shortcut in self.context.shortcuts:
                self._bindings.bind(shortcut.key, f'shortcut("{shortcut.command}")',
                                    description=shortcut.description,
                                    show=shortcut.show)

    def action_shortcut(self, command: str):
        self._exit_select(command)

    def on_inquirer_widget_submit(self, event: InquirerWidget.Submit) -> None:
        self.call_after_refresh(lambda: self.app.exit(Result(event.command, event.value)))

    def _exit_select(self, command: str):
        self.call_after_refresh(lambda: self.app.exit(Result(command, self.context.widget.current_value())))

    def compose(self) -> ComposeResult:
        yield self.context.widget
        if self.context.show_footer:
            yield Footer()

    def get_theme_variable_defaults(self) -> dict[str, str]:
        return {
            'select-question-mark': '#e5c07b',
            'select-list-item-highlight-foreground': '#61afef',
            'input-color': '#98c379'
        }
