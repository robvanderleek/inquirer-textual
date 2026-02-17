from __future__ import annotations

from textual.app import ComposeResult
from textual.containers import VerticalGroup, HorizontalGroup
from textual.widgets import ListItem, ListView
from typing_extensions import Self

from inquirer_textual.common.Answer import Answer
from inquirer_textual.common.Choice import Choice
from inquirer_textual.common.ChoiceCheckboxLabel import ChoiceCheckboxLabel
from inquirer_textual.common.Prompt import Prompt
from inquirer_textual.widgets.InquirerWidget import InquirerWidget


class InquirerCheckbox(InquirerWidget):
    """A checkbox widget that allows multiple selections from a list of choices."""

    BINDINGS = [
        ("space", "toggle_selected", "Toggle selection"),
    ]

    def __init__(self, message: str, choices: list[str | Choice], name: str | None = None,
                 enabled: list[str | Choice] | None = None, mandatory: bool = False, height: int | str | None = None):
        """
            Args:
                message (str): The prompt message to display.
                choices (list[str | Choice]): A list of choices to present to the user.
                name (str | None): The name of the input field.
                enabled (list[str | Choice] | None): A list of choices that should be pre-selected.
                mandatory (bool): Whether at least one selection is mandatory.
                height (int | str | None): If None, for inline apps the height will be determined based on the number
                of choices.
        """
        super().__init__(name=name, mandatory=mandatory)
        self.message = message
        self.choices = choices
        self.enabled = enabled
        self.list_view: ListView | None = None
        self.selected_label: ChoiceCheckboxLabel | None = None
        self.selected_item: str | Choice | None = None
        self.selected_value: list[str | Choice] | None = None
        self.show_selected_value: bool = False
        self.height = height

    def on_mount(self):
        super().on_mount()
        if self.height is not None:
            self.styles.height = self.height
        elif self.app.is_inline:
            self.styles.height = min(10, len(self.choices) + 1)
        else:
            self.styles.height = '1fr'

    def action_toggle_selected(self) -> None:
        if self.selected_label:
            self.selected_label.toggle()

    def on_list_view_highlighted(self, event: ListView.Highlighted) -> None:
        label = event.item.query_one(ChoiceCheckboxLabel)
        self.selected_label = label
        self.selected_item = label.item

    def on_list_view_selected(self, _: ListView.Selected) -> None:
        self.submit_current_value()

    def focus(self, scroll_visible: bool = True) -> Self:
        if self.list_view:
            return self.list_view.focus(scroll_visible)
        else:
            return super().focus(scroll_visible)

    def current_value(self):
        labels = self.query(ChoiceCheckboxLabel)
        return [label.item for label in labels if label.checked]

    async def set_selected_value(self, value: list[str | Choice]) -> None:
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
                items: list[ListItem] = []
                for idx, choice in enumerate(self.choices):
                    list_item = ListItem(ChoiceCheckboxLabel(choice))
                    items.append(list_item)
                self.list_view = ListView(*items, id='inquirer-checkbox-list-view')
                yield Prompt(self.message)
                yield self.list_view
