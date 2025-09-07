from textual.app import ComposeResult
from textual.containers import Horizontal, VerticalGroup
from textual.widget import Widget
from textual.widgets import ListView, Label, ListItem, Static

from inquirer_textual.widgets.Choice import Choice
from inquirer_textual.widgets.SelectResult import SelectResult
from inquirer_textual.widgets.Shortcut import Shortcut


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
            color: $select-list-item-highlight-foreground;
            background: transparent;
        }
        #inquirer-select-question-mark {
            width: 2;
            color: $select-question-mark;
        }
        #inquirer-select-header {
            height: 1;
        }
        """

    def __init__(self, message: str, choices: list[Choice], shortcuts: list[Shortcut] | None = None,
                 default: Choice | None = None):
        super().__init__()
        self.message = message
        self.choices = choices
        self.list_view: ListView | None = None
        self.selected_label: ChoiceLabel | None = None
        self.selected_item: Choice | None = None
        self.shortcuts = shortcuts
        self.default = default

    def on_mount(self):
        if self.shortcuts:
            for shortcut in self.shortcuts:
                self._bindings.bind(shortcut.key, f'shortcut("{shortcut.command}")', description=shortcut.description,
                                    show=shortcut.show)
        self.styles.height = min(10, len(self.choices) + 1)

    def on_list_view_highlighted(self, event: ListView.Highlighted) -> None:
        if self.selected_label:
            self.selected_label.remove_pointer()
        label = event.item.query_one(ChoiceLabel)
        label.add_pointer()
        self.selected_label = label
        self.selected_item = next(c for c in self.choices if c.name == label.text)

    def on_list_view_selected(self, _: ListView.Selected) -> None:
        self._exit_select('select')

    def action_shortcut(self, command: str):
        self._exit_select(command)

    def _exit_select(self, command: str):
        self.app.call_after_refresh(lambda: self.app.exit(SelectResult(command, self.selected_item)))

    def compose(self) -> ComposeResult:
        with VerticalGroup():
            initial_index = 0
            items: list[ListItem] = []
            for idx, choice in enumerate(self.choices):
                list_item = ListItem(ChoiceLabel(choice.name))
                items.append(list_item)
                if self.default and choice == self.default:
                    initial_index = idx
            self.list_view = ListView(*items, id='inquirer-select-list-view', initial_index=initial_index)
            with Horizontal(id='inquirer-select-header'):
                yield Static('? ', id='inquirer-select-question-mark')
                yield Static(self.message)
            yield self.list_view
