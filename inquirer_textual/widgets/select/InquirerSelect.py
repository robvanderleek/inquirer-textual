from textual import getters
from textual.app import ComposeResult
from textual.containers import VerticalGroup
from textual.widgets import ListView, ListItem

from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.widgets.Choice import Choice
from inquirer_textual.widgets.InquirerWidget import InquirerWidget
from inquirer_textual.widgets.PromptMessage import PromptMessage
from inquirer_textual.widgets.select.ChoiceLabel import ChoiceLabel


class InquirerSelect(InquirerWidget):
    DEFAULT_CSS = """
        #inquirer-select-list-view {
            background: transparent;
        }
        #inquirer-select-list-view ListItem.-highlight {
            color: $select-list-item-highlight-foreground;
            background: transparent;
        }
        """
    app = getters.app(InquirerApp)

    def __init__(self, message: str, choices: list[str | Choice], default: Choice | None = None):
        super().__init__()
        self.message = message
        self.choices = choices
        self.list_view: ListView | None = None
        self.selected_label: ChoiceLabel | None = None
        self.selected_item: Choice | None = None
        self.default = default

    def on_mount(self):
        self.styles.height = min(10, len(self.choices) + 1)

    def on_list_view_highlighted(self, event: ListView.Highlighted) -> None:
        if self.selected_label:
            self.selected_label.remove_pointer()
        label = event.item.query_one(ChoiceLabel)
        label.add_pointer()
        self.selected_label = label
        self.selected_item = label.item

    def on_list_view_selected(self, _: ListView.Selected) -> None:
        self.app.select_current()

    def current_value(self):
        return self.selected_item

    def compose(self) -> ComposeResult:
        with VerticalGroup():
            initial_index = 0
            items: list[ListItem] = []
            for idx, choice in enumerate(self.choices):
                list_item = ListItem(ChoiceLabel(choice))
                items.append(list_item)
                if self.default and choice == self.default:
                    initial_index = idx
            self.list_view = ListView(*items, id='inquirer-select-list-view', initial_index=initial_index)
            yield PromptMessage(self.message)
            yield self.list_view
