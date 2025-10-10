from textual.app import ComposeResult
from textual.containers import VerticalGroup
from textual.widgets import ListItem, ListView

from inquirer_textual.common.Choice import Choice
from inquirer_textual.common.ChoiceCheckboxLabel import ChoiceCheckboxLabel
from inquirer_textual.common.PromptMessage import PromptMessage
from inquirer_textual.widgets.InquirerWidget import InquirerWidget


class InquirerCheckbox(InquirerWidget):
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

    def __init__(self, message: str, choices: list[str | Choice], enabled: list[str | Choice] | None = None):
        super().__init__()
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
