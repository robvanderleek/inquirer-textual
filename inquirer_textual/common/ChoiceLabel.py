from __future__ import annotations

from rich.text import Text
from textual.widgets import Label

from inquirer_textual.common.Choice import Choice
from inquirer_textual.common.defaults import DEFAULT_THEME, POINTER_CHARACTER


class ChoiceLabel(Label):
    def __init__(self, item: str | Choice, pattern: str | None = None):
        self._text = self._get_text(item, pattern)
        super().__init__(Text('  ').append_text(self._text))
        self.item = item

    def _get_text(self, item: str | Choice, pattern: str | None = None) -> Text:
        result = Text(item if isinstance(item, str) else item.name)
        if pattern:
            result.highlight_words([pattern], style=self.app.current_theme.accent or DEFAULT_THEME.accent,
                                   case_sensitive=False)
        return result

    def add_pointer(self):
        self.update(Text(f'{POINTER_CHARACTER} ').append_text(self._text))

    def remove_pointer(self):
        self.update(Text('  ').append_text(self._text))
