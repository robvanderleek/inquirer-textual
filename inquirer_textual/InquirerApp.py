from __future__ import annotations

from asyncio import AbstractEventLoop
from threading import Event
from typing import TypeVar, Callable, Any

from textual.app import App, AutopilotCallbackType
from textual.app import ComposeResult
from textual.binding import Binding, BindingsMap
from textual.widgets import Footer

from inquirer_textual.common.InquirerHeader import InquirerHeader
from inquirer_textual.common.Result import Result
from inquirer_textual.common.Shortcut import Shortcut
from inquirer_textual.common.StandardTheme import StandardTheme
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
    BINDINGS = [
        Binding("ctrl+d", "quit", "Quit", show=False, priority=True)
    ]

    def __init__(self) -> None:
        self.widget: InquirerWidget | None = None
        self.shortcuts: list[Shortcut] | None = None
        self.header: str | list[str] | None = None
        self.show_footer: bool = False
        self.result: Result[T] | None = None
        self.result_ready: Event | None = None
        self.inquiry_func: Callable[[InquirerApp[T]], None] | None = None
        self.inquiry_func_stop: bool = False
        super().__init__()

    def on_mount(self) -> None:
        self._update_bindings()
        if self.inquiry_func:
            self.run_worker(self.inquiry_func_worker, thread=True)

    def _update_bindings(self) -> None:
        self._bindings = BindingsMap()
        if self.shortcuts:
            for shortcut in self.shortcuts:
                self._bindings.bind(shortcut.key, f'shortcut("{shortcut.command}")',
                                    description=shortcut.description,
                                    show=shortcut.show)

    def inquiry_func_worker(self):
        if self.inquiry_func:
            self.inquiry_func(self)

    def action_shortcut(self, command: str):
        value = self.widget.current_value() if self.widget else None
        self._handle_result(command, value)

    async def action_quit(self):
        self._handle_result('quit', None)

    def on_inquirer_widget_submit(self, event: InquirerWidget.Submit) -> None:
        self._handle_result(event.command, event.value)

    def _handle_result(self, command: str | None, value: Any | None):
        if self.result_ready is not None:
            self.result = Result(command, value)  # type: ignore[arg-type]
            self.result_ready.set()
        else:
            self.call_after_refresh(lambda: self._terminate(command, value))

    def _terminate(self, command: str | None = None, value: Any | None = None):
        self.inquiry_func_stop = True
        if self.result_ready:
            self.result_ready.set()
        if command is not None:
            self.app.exit(Result(command, value))
        else:
            self.exit(value)

    def compose(self) -> ComposeResult:
        if self.header is not None:
            yield InquirerHeader(self.header)
        if self.widget:
            yield self.widget
            self.widget.focus()
            if self.show_footer:
                yield Footer()

    def focus_widget(self):
        if self.widget:
            self.call_after_refresh(self.widget.focus)

    def prompt(self, widget: InquirerWidget, shortcuts: list[Shortcut] | None = None) -> Result[T]:
        if shortcuts:
            self.shortcuts = shortcuts
            self.show_footer = True
        self._update_bindings()
        self.widget = widget
        if not self.result_ready:
            self.result_ready = Event()
        self.call_from_thread(self.refresh, recompose=True)
        self.call_from_thread(self.focus_widget)
        self.result_ready.wait()
        self.result_ready.clear()
        if self.inquiry_func_stop:
            raise RuntimeError("InquirerApp has been stopped.")
        return self.result  # type: ignore[return-value]

    def stop(self, value: Any = None):
        if value:
            self.call_after_refresh(lambda: self._terminate(value=value))
        else:
            self.call_from_thread(self.exit)

    def run(
            self,
            *,
            headless: bool = False,
            inline: bool = False,
            inline_no_clear: bool = False,
            mouse: bool = True,
            size: tuple[int, int] | None = None,
            auto_pilot: AutopilotCallbackType | None = None,
            loop: AbstractEventLoop | None = None,
            inquiry_func: Callable[[InquirerApp[T]], None] | None = None,
    ) -> Result[T]:
        if not self.inquiry_func:
            self.inquiry_func = inquiry_func
        return super().run(
            headless=headless,
            inline=inline,
            inline_no_clear=inline_no_clear,
            mouse=mouse,
            size=size,
            auto_pilot=auto_pilot,
            loop=loop,
        )

    def get_theme_variable_defaults(self) -> dict[str, str]:
        return {
            'input-color': StandardTheme.input_color,
            'prompt-color': StandardTheme.prompt_color,
            'error-color': StandardTheme.error_color,
            'select-list-item-highlight-foreground': StandardTheme.select_list_item_highlight_foreground,
            'select-question-mark': StandardTheme.select_question_mark,
        }
