from __future__ import annotations

from typing import Callable, Awaitable

from textual import work
from textual.app import ComposeResult
from textual.containers import HorizontalGroup
from textual.reactive import Reactive
from textual.widgets import Static

from inquirer_textual.common.Answer import Answer
from inquirer_textual.common.Choice import Choice
from inquirer_textual.common.Prompt import Prompt
from inquirer_textual.common.SpinnerWidget import SpinnerWidget
from inquirer_textual.widgets.base.InquirerWidget import InquirerWidget


class InquirerChoicesWidget(InquirerWidget):
    """Base class for list-based widgets like InquirerSelect and InquirerCheckbox."""

    _is_loading = Reactive(True)

    def __init__(self, message: str, choices_factory: list[str | Choice] | Callable[[], Awaitable[list[str | Choice]]],
                 name: str | None = None, mandatory: bool = False,
                 height: int | str | None = None):
        """
            Args:
                choices (list[str | Choice]): A list of choices to present to the user.
                name (str | None): The name of the input field.
                mandatory (bool): Whether at least one selection is mandatory.
                height (int | str | None): If None, for inline apps the height will be determined based on the number
                of choices.
        """
        super().__init__(name=name, mandatory=mandatory)
        self.message = message
        self._choices_factory = choices_factory
        self._choices: list[str | Choice] | None = None if callable(choices_factory) else choices_factory
        self.height = height
        self.show_result: bool = False
        self.selected_value: str | Choice | None = None
        self._is_loading = True if callable(choices_factory) else False

    def on_mount(self):
        super().on_mount()
        if callable(self._choices_factory):
            self._load_choices()
        else:
            self._adjust_height()

    def _adjust_height(self):
        if self.height is not None:
            if self.height == 'auto':
                self.styles.min_height = 10
            self.styles.height = self.height
        elif self.app.is_inline and self._choices is not None:
            self.styles.height = min(10, len(self._choices) + 1)
        else:
            self.styles.height = '1fr'

    @work
    async def _load_choices(self) -> None:
        self._choices = await self._choices_factory()
        self._adjust_height()
        self._is_loading = False
        await self.recompose()
        self.focus()

    def compose_choices_widget(self) -> ComposeResult:
        raise NotImplementedError("Subclasses must implement the compose_choices_widget method.")

    def compose(self) -> ComposeResult:
        if self._is_loading:
            with HorizontalGroup():
                yield SpinnerWidget()
                yield Static("Loading choices...")
        elif self.show_result:
            with HorizontalGroup():
                yield Prompt(self.message)
                if self.selected_value is not None:
                    yield Answer(str(self.selected_value))
        else:
            yield from self.compose_choices_widget()
