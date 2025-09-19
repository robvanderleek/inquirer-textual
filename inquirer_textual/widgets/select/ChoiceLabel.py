from textual.widgets import Label

from inquirer_textual.widgets.Choice import Choice


class ChoiceLabel(Label):
    def __init__(self, item: str | Choice):
        super().__init__(f'  {item if isinstance(item, str) else item.name}')
        self._text = item if isinstance(item, str) else item.name
        self.item = item

    def add_pointer(self):
        self.update(f'\u276f {self._text}')

    def remove_pointer(self):
        self.update(f'  {self._text}')
