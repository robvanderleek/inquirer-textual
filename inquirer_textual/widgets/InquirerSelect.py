from typing import Self

from inquirer_textual.common.Choice import Choice
from inquirer_textual.widgets.InquirerWidget import InquirerWidget
from inquirer_textual.common.PromptMessage import PromptMessage
from inquirer_textual.common.ChoiceLabel import ChoiceLabel
from textual.app import ComposeResult
from textual.containers import VerticalGroup
from textual.widgets import ListView, ListItem


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

    def __init__(self, message: str, choices: list[str | Choice], default: str | Choice | None = None,
                 mandatory: bool = True):
        super().__init__(mandatory)
        self.message = message
        self.choices = choices
        self.list_view: ListView | None = None
        self.selected_label: ChoiceLabel | None = None
        self.selected_item: str | Choice | None = None
        self.default = default

    def on_mount(self):
        super().on_mount()
        self.styles.height = min(10, len(self.choices) + 1)

    def on_list_view_highlighted(self, event: ListView.Highlighted) -> None:
        if self.selected_label:
            self.selected_label.remove_pointer()
        label = event.item.query_one(ChoiceLabel)
        label.add_pointer()
        self.selected_label = label
        self.selected_item = label.item

    def on_list_view_selected(self, _: ListView.Selected):
        if isinstance(self.selected_item, Choice):
            self.post_message(InquirerWidget.Submit(self.selected_item, self.selected_item.command))
        else:
            self.post_message(InquirerWidget.Submit(self.selected_item))

    def focus(self, scroll_visible: bool = True) -> Self:
        if self.list_view:
            return self.list_view.focus(scroll_visible)
        else:
            return super().focus(scroll_visible)

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
