from __future__ import annotations

from rich.console import ConsoleRenderable
from rich.text import Text
from textual.app import App

from inquirer_textual.common.Choice import Choice
from inquirer_textual.common.defaults import DEFAULT_THEME


class Candidate:
    def __init__(self, choice: Choice | str, match_indices: list[int] | None = None):
        self.choice = choice
        self.match_indices = match_indices

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Candidate):
            return NotImplemented
        return self.choice == other.choice and self.match_indices == other.match_indices

    def render(self, app: App) -> ConsoleRenderable:
        result = Text(self.choice if isinstance(self.choice, str) else self.choice.name)
        if self.match_indices:
            for index in self.match_indices:
                result.stylize(app.current_theme.accent or DEFAULT_THEME.accent, index, index + 1)
        return result