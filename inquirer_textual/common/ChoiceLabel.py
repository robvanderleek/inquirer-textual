from __future__ import annotations

from rich.text import Text
from textual.widgets import Label

from inquirer_textual.common.Choice import Choice
from inquirer_textual.common.StandardTheme import StandardTheme


class ChoiceLabel(Label):
    def __init__(self, item: str | Choice, pattern: str | None = None):
        self._text = ChoiceLabel._get_text(item, pattern)
        super().__init__(Text('  ').append_text(self._text))
        self.item = item

    @classmethod
    def _get_text(cls, item: str | Choice, pattern: str | None = None) -> Text:
        result = Text(item if isinstance(item, str) else item.name)
        if pattern:
            result.highlight_words([pattern], style=StandardTheme.prompt_color, case_sensitive=False)
        return result

    def add_pointer(self):
        self.update(Text(f'{StandardTheme.pointer_character} ').append_text(self._text))

    def remove_pointer(self):
        self.update(Text(f'  ').append_text(self._text))
