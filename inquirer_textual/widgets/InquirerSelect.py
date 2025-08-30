from textual.app import ComposeResult
from textual.containers import Vertical
from textual.widget import Widget
from textual.widgets import ListView, Label, ListItem, Static

from inquirer_textual.widgets.Choice import Choice


class ChoiceLabel(Label):
    def __init__(self, text: str):
        super().__init__('  ' + text)
        self.text = text

    def add_pointer(self):
        self.update(f'\u276f {self.text}')

    def remove_pointer(self):
        self.update(f'  {self.text}')


class InquirerSelect(Widget):
    DEFAULT_CSS = """
        #inquirer-select-list-view {
            background: transparent;
        }
        #inquirer-select-list-view ListItem.-highlight {
            color: $highlight-foreground;
            background: transparent;
        }
        """

    def __init__(self, message: str, choices: list[Choice]):
        super().__init__()
        self.message = message
        self.choices = choices
        self.list_view: ListView | None = None
        self.selected: ChoiceLabel | None = None

    def on_mount(self):
        self.styles.height = min(10, len(self.choices) + 1)

    def on_list_view_highlighted(self, event: ListView.Highlighted) -> None:
        if self.selected:
            self.selected.remove_pointer()
        label = event.item.query_one(ChoiceLabel)
        label.add_pointer()
        self.selected = label

    def on_list_view_selected(self, event: ListView.Selected) -> None:
        self.app.exit(self.choices[event.index])

    def compose(self) -> ComposeResult:
        items: list[ListItem] = []
        for choice in self.choices:
            list_item = ListItem(ChoiceLabel(choice.name))
            items.append(list_item)
        self.list_view = ListView(*items, id='inquirer-select-list-view')
        with Vertical():
            yield Static(self.message)
            yield self.list_view
