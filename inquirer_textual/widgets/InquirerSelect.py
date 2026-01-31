from __future__ import annotations

from textual.app import ComposeResult
from textual.containers import VerticalGroup, HorizontalGroup
from textual.widgets import ListView, ListItem, Static
from typing_extensions import Self

from inquirer_textual.common.Answer import Answer
from inquirer_textual.common.Choice import Choice
from inquirer_textual.common.ChoiceLabel import ChoiceLabel
from inquirer_textual.common.Prompt import Prompt
from inquirer_textual.widgets.InquirerWidget import InquirerWidget


class InquirerSelect(InquirerWidget):
    """A select widget that allows a single selection from a list of choices."""

    def __init__(self, message: str, choices: list[str | Choice], name: str | None = None,
                 default: str | Choice | None = None, mandatory: bool = True):
        """
        Args:
            message (str): The prompt message to display.
            choices (list[str | Choice]): A list of choices to present to the user.
            default (str | Choice | None): The default choice to pre-select.
            mandatory (bool): Whether a response is mandatory.
        """
        super().__init__(name=name, mandatory=mandatory)
        self.message = message
        self.choices = choices
        self.list_view: ListView | None = None
        self.selected_label: ChoiceLabel | None = None
        self.selected_item: str | Choice | None = None
        self.default = default
        self.selected_value: str | Choice | None = None
        self.show_selected_value: bool = False

    def on_mount(self):
        super().on_mount()
        if self.app.is_inline:
            self.styles.height = min(10, len(self.choices) + 1)
        else:
            self.styles.height = '1fr'

    def on_list_view_highlighted(self, event: ListView.Highlighted) -> None:
        if self.selected_label:
            self.selected_label.remove_pointer()
        label = event.item.query_one(ChoiceLabel)
        label.add_pointer()
        self.selected_label = label
        self.selected_item = label.item

    def on_list_view_selected(self, _: ListView.Selected):
        if isinstance(self.selected_item, Choice):
            self.submit_current_value(self.selected_item.command)
        else:
            self.submit_current_value()

    def focus(self, scroll_visible: bool = True) -> Self:
        if self.list_view:
            return self.list_view.focus(scroll_visible)
        else:
            return super().focus(scroll_visible)

    def current_value(self):
        return self.selected_item

    async def set_selected_value(self, value: str | Choice) -> None:
        self.selected_value = value
        self.styles.height = 1
        self.show_selected_value = True
        await self.recompose()

    def compose(self) -> ComposeResult:
        if self.show_selected_value:
            with HorizontalGroup():
                yield Prompt(self.message)
                yield Answer(str(self.selected_value))
        else:
            with VerticalGroup():
                initial_index = 0
                items: list[ListItem] = []
                for idx, choice in enumerate(self.choices):
                    list_item = ListItem(ChoiceLabel(choice))
                    items.append(list_item)
                    if self.default and choice == self.default:
                        initial_index = idx
                self.list_view = ListView(*items, id='inquirer-select-list-view', initial_index=initial_index)
                yield Prompt(self.message)
                yield self.list_view
