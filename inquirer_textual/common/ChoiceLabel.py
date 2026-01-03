from __future__ import annotations

from textual.widgets import Label

from inquirer_textual.common.StandardTheme import StandardTheme
from inquirer_textual.common.Choice import Choice


class ChoiceLabel(Label):
    def __init__(self, item: str | Choice):
        super().__init__(f'  {item if isinstance(item, str) else item.name}')
        self._text = item if isinstance(item, str) else item.name
        self.item = item

    def add_pointer(self):
        self.update(f'{StandardTheme.pointer_character} {self._text}')

    def remove_pointer(self):
        self.update(f'  {self._text}')
