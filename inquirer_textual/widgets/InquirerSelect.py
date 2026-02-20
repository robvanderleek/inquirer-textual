from __future__ import annotations

from textual.app import ComposeResult
from textual.containers import VerticalGroup, HorizontalGroup
from textual.widgets import ListView, ListItem
from typing_extensions import Self

from inquirer_textual.common.Answer import Answer
from inquirer_textual.common.Choice import Choice, COMMAND_SELECT
from inquirer_textual.common.ChoiceLabel import ChoiceLabel
from inquirer_textual.common.Prompt import Prompt
from inquirer_textual.widgets.InquirerWidget import InquirerWidget


class InquirerSelect(InquirerWidget):
    """A select widget that allows a single selection from a list of choices."""

    def __init__(self, message: str, choices: list[str | Choice], name: str | None = None,
                 default: str | Choice | None = None, mandatory: bool = True, height: int | str | None = None):
        """
        Args:
            message (str): The prompt message to display.
            choices (list[str | Choice]): A list of choices to present to the user.
            default (str | Choice | None): The default choice to pre-select.
            mandatory (bool): Whether a response is mandatory.
            height (int | str | None): If None, for inline apps the height will be determined based on the number of choices.
        """
        super().__init__(name=name, mandatory=mandatory)
        self.message = message
        self.choices = choices
        self.list_view: ListView | None = None
        self.selected_label: ChoiceLabel | None = None
        self.selected_item: str | Choice | None = None
        self.default = default
        self.selected_value: str | Choice | None = None
        self.show_result: bool = False
        self.height = height

    def on_mount(self):
        super().on_mount()
        if self.height is not None:
            self.styles.height = self.height
        elif self.app.is_inline:
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

    async def on_command(self, command: str | None) -> None:
        self.selected_value = self.current_value() if command == COMMAND_SELECT else None
        self.styles.height = 1
        self.show_result = True
        await self.recompose()

    def compose(self) -> ComposeResult:
        if self.show_result:
            with HorizontalGroup():
                yield Prompt(self.message)
                if self.selected_value is not None:
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
