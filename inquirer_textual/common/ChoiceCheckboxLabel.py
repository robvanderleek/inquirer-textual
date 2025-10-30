from __future__ import annotations

from textual.widgets import Label

from inquirer_textual.common.Choice import Choice


class ChoiceCheckboxLabel(Label):
    def __init__(self, item: str | Choice):
        super().__init__(f'\u25cb {item if isinstance(item, str) else item.name}')
        self._text = item if isinstance(item, str) else item.name
        self.item = item
        self.checked = False

    def check(self):
        self.checked = True
        self.update(f'\u25c9 {self._text}')

    def uncheck(self):
        self.checked = False
        self.update(f'\u25cb {self._text}')

    def toggle(self):
        self.uncheck() if self.checked else self.check()
