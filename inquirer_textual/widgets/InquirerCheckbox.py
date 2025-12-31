from __future__ import annotations

from textual.app import ComposeResult
from textual.containers import VerticalGroup
from textual.widgets import ListItem, ListView
from typing_extensions import Self

from inquirer_textual.common.Choice import Choice
from inquirer_textual.common.ChoiceCheckboxLabel import ChoiceCheckboxLabel
from inquirer_textual.common.PromptMessage import PromptMessage
from inquirer_textual.widgets.InquirerWidget import InquirerWidget


class InquirerCheckbox(InquirerWidget):
    """A checkbox widget that allows multiple selections from a list of choices."""

    DEFAULT_CSS = """
            #inquirer-checkbox-list-view {
                background: transparent;
            }
            #inquirer-checkbox-list-view ListItem.-highlight {
                color: $select-list-item-highlight-foreground;
                background: transparent;
            }
            """
    BINDINGS = [
        ("space", "toggle_selected", "Toggle selection"),
    ]

    def __init__(self, message: str, choices: list[str | Choice], enabled: list[str | Choice] | None = None,
                 mandatory: bool = False):
        """
            Args:
                message (str): The prompt message to display.
                choices (list[str | Choice]): A list of choices to present to the user.
                enabled (list[str | Choice] | None): A list of choices that should be pre-selected.
        """
        super().__init__(mandatory=mandatory)
        self.message = message
        self.choices = choices
        self.enabled = enabled
        self.list_view: ListView | None = None
        self.selected_label: ChoiceCheckboxLabel | None = None
        self.selected_item: str | Choice | None = None

    def on_mount(self):
        self.styles.height = min(10, len(self.choices) + 1)

    def action_toggle_selected(self) -> None:
        if self.selected_label:
            self.selected_label.toggle()

    def on_list_view_highlighted(self, event: ListView.Highlighted) -> None:
        label = event.item.query_one(ChoiceCheckboxLabel)
        self.selected_label = label
        self.selected_item = label.item

    def on_list_view_selected(self, _: ListView.Selected) -> None:
        self.post_message(InquirerWidget.Submit(self.current_value()))

    def focus(self, scroll_visible: bool = True) -> Self:
        if self.list_view:
            return self.list_view.focus(scroll_visible)
        else:
            return super().focus(scroll_visible)

    def current_value(self):
        labels = self.query(ChoiceCheckboxLabel)
        return [label.item for label in labels if label.checked]

    def compose(self) -> ComposeResult:
        with VerticalGroup():
            items: list[ListItem] = []
            for idx, choice in enumerate(self.choices):
                list_item = ListItem(ChoiceCheckboxLabel(choice))
                items.append(list_item)
            self.list_view = ListView(*items, id='inquirer-checkbox-list-view')
            yield PromptMessage(self.message)
            yield self.list_view
