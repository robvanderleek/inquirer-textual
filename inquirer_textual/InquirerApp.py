from __future__ import annotations

from asyncio import AbstractEventLoop
from threading import Event
from typing import TypeVar, Callable, Any

from textual.app import App, AutopilotCallbackType
from textual.app import ComposeResult
from textual.binding import Binding, BindingsMap
from textual.widgets import Footer

from inquirer_textual.common.Choice import COMMAND_SELECT
from inquirer_textual.common.InquirerHeader import InquirerHeader
from inquirer_textual.common.InquirerResult import InquirerResult
from inquirer_textual.common.Shortcut import Shortcut
from inquirer_textual.common.defaults import DEFAULT_THEME
from inquirer_textual.common.utils import get_cursor_row
from inquirer_textual.widgets.InquirerWidget import InquirerWidget

T = TypeVar('T')


class InquirerApp(App[InquirerResult[T]], inherit_bindings=False):  # type: ignore[call-arg]
    CSS = """
        Screen {
            border-top: none;
            border-bottom: none;
            # height: 1fr;
        }
        """
    ENABLE_COMMAND_PALETTE = False
    INLINE_PADDING = 0
    BINDINGS = [
        Binding("ctrl+d", "quit", "Quit", show=False, priority=True)
    ]

    def __init__(self, theme: str = 'inquirer-textual-default') -> None:
        self._theme = theme
        self._shortcuts: list[Shortcut] | None = None
        self.widget: InquirerWidget | None = None
        self.header: str | list[str] | None = None
        self.show_footer: bool = False
        self.result: InquirerResult[T] | None = None
        self.result_ready: Event | None = None
        self.inquiry_func: Callable[[InquirerApp[T]], None] | None = None
        self.inquiry_func_stop: bool = False
        self.inline_start_row: int | None = None
        super().__init__()

    @property
    def shortcuts(self) -> list[Shortcut] | None:
        return self._shortcuts

    @shortcuts.setter
    def shortcuts(self, value: list[Shortcut] | None):
        self._shortcuts = value
        if value:
            self.show_footer = True

    def on_mount(self) -> None:
        self.register_theme(DEFAULT_THEME)
        self.theme = self._theme
        self._update_bindings()
        if self.inquiry_func:
            self.run_worker(self.inquiry_func_worker, thread=True)
        if self.is_inline and self.inline_start_row is not None:
            inline_height = self._get_inline_height()
            if self.inline_start_row + 1 + inline_height < self.viewport_size.height:
                self.screen.styles.height = self.viewport_size.height - self.inline_start_row + 1

    def _update_bindings(self) -> None:
        self._bindings = BindingsMap()
        if self._shortcuts:
            for shortcut in self._shortcuts:
                self._bindings.bind(shortcut.key, f'shortcut("{shortcut.command}")',
                                    description=shortcut.description,
                                    show=shortcut.show)

    def inquiry_func_worker(self):
        if self.inquiry_func:
            self.inquiry_func(self)

    async def action_shortcut(self, command: str):
        value = self.widget.current_value() if self.widget else None
        await self._handle_result(command, value)

    async def action_quit(self):
        await self._handle_result('quit', None)

    async def on_inquirer_widget_submit(self, event: InquirerWidget.Submit) -> None:
        await self._handle_result(event.command, event.value)

    async def _handle_result(self, command: str | None, value: Any | None):
        if self.result_ready is not None:
            self.result = InquirerResult(
                self.widget.name if self.widget else None, value, command)  # type: ignore[arg-type]
            self.result_ready.set()
        else:
            if self.widget and command == COMMAND_SELECT:
                await self.widget.set_selected_value(value)
            if self.show_footer:
                self.query_one(Footer).styles.display = 'none'
            if self.is_inline and self.inline_start_row is not None:
                self.screen.styles.height = 'auto'
            self.call_after_refresh(lambda: self._terminate(command, value))

    async def _terminate(self, command: str | None = None, value: Any | None = None):
        self.inquiry_func_stop = True
        if self.result_ready:
            self.result_ready.set()
        self.app.exit(InquirerResult(self.widget.name if self.widget else None, value, command))

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

    def prompt(self, widget: InquirerWidget, shortcuts: list[Shortcut] | None = None) -> InquirerResult[T]:
        if shortcuts:
            self._shortcuts = shortcuts
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
    ) -> InquirerResult[T]:
        if not self.inquiry_func:
            self.inquiry_func = inquiry_func
        self.inline_start_row = get_cursor_row()
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
            'inquirer-textual-question-mark': self.current_theme.foreground or 'initial',
            'inquirer-textual-input-color': self.current_theme.foreground or 'initial',
        }
