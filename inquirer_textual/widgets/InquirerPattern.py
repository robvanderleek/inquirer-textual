from __future__ import annotations

from textual import on, events
from textual.app import ComposeResult
from textual.containers import VerticalGroup, HorizontalGroup
from textual.css.query import NoMatches
from textual.reactive import reactive
from textual.widgets import ListView, ListItem, Input, Static
from typing_extensions import Self

from inquirer_textual.common.Choice import Choice
from inquirer_textual.common.ChoiceLabel import ChoiceLabel
from inquirer_textual.common.PromptMessage import PromptMessage
from inquirer_textual.common.StandardTheme import StandardTheme
from inquirer_textual.widgets.InquirerWidget import InquirerWidget


class InquirerPattern(InquirerWidget):
    """A select widget that allows a single selection from a list of choices with pattern filtering."""

    DEFAULT_CSS = """
        #inquirer-pattern-list-view {
            background: transparent;
        }
        #inquirer-pattern-list-view ListItem.-highlight {
            color: $select-list-item-highlight-foreground;
            background: transparent;
        }
        #inquirer-pattern-query-container {
            width: auto;
            # border: red;
        }
        #inquirer-pattern-query {
            border: none;
            background: transparent;
            color: $input-color;
            padding: 0;
            height: 1;
            width: 20;
        }
        #inquirer-pattern-query-pointer {
            width: auto;
            color: $prompt-color;
        }
        """

    candidates: reactive[list[str | Choice]] = reactive([])

    def __init__(self, message: str, choices: list[str | Choice], default: str | Choice | None = None,
                 mandatory: bool = True):
        """
        Args:
            message (str): The prompt message to display.
            choices (list[str | Choice]): A list of choices to present to the user.
            default (str | Choice | None): The default choice to pre-select.
            mandatory (bool): Whether a response is mandatory.
        """
        super().__init__(mandatory)
        self.message = message
        self.choices = choices
        self.candidates = choices.copy()
        self.list_view: ListView | None = None
        self.selected_label: ChoiceLabel | None = None
        self.selected_item: str | Choice | None = None
        self.default = default
        self.query: Input | None = None

    def on_mount(self):
        super().on_mount()
        if self.app.is_inline:
            self.styles.height = min(10, len(self.choices) + 1)
        else:
            self.styles.height = '1fr'

    def on_list_view_highlighted(self, event: ListView.Highlighted) -> None:
        if self.selected_label:
            self.selected_label.remove_pointer()
        if event.item:
            try:
                label = event.item.query_one(ChoiceLabel)
                label.add_pointer()
                self.selected_label = label
                self.selected_item = label.item
                return
            except NoMatches:
                pass
        self.selected_label = None
        self.selected_item = None

    def on_list_view_selected(self, _: ListView.Selected):
        if isinstance(self.selected_item, Choice):
            self.submit_current_value(self.selected_item.command)
        else:
            self.submit_current_value()

    def focus(self, scroll_visible: bool = True) -> Self:
        if self.query:
            return self.query.focus(scroll_visible)
        else:
            return super().focus(scroll_visible)

    def current_value(self):
        return self.selected_item

    def _collect_list_items(self):
        items: list[ListItem] = []
        for candidate in self.candidates:
            list_item = ListItem(ChoiceLabel(candidate, self.query.value if self.query else None))
            items.append(list_item)
        return items

    def _find_initial_index(self):
        initial_index = 0
        for idx, choice in enumerate(self.choices):
            if self.default and choice == self.default:
                initial_index = idx
        return initial_index

    @on(Input.Changed, '#inquirer-pattern-query')
    async def handle_query_changed(self, event: Input.Changed):
        query = event.value.lower()
        if query == '':
            self.candidates = self.choices.copy()
        else:
            filtered = []
            for choice in self.choices:
                name = choice.name if isinstance(choice, Choice) else choice
                if query in name.lower():
                    filtered.append(choice)
            self.candidates = filtered
        assert isinstance(self.list_view, ListView)
        await self.list_view.clear()
        list_items = self._collect_list_items()
        await self.list_view.extend(list_items)
        if list_items:
            self.list_view.index = 0

    def watch_candidates(self, candidates: list[str | Choice]) -> None:
        count_suffix = f'[{len(candidates)}/{len(self.choices)}]'
        try:
            count_widget = self.query_one('#inquirer-pattern-query-count-suffix', Static)
            count_widget.update(count_suffix)
        except NoMatches:
            pass

    def on_key(self, event: events.Key):
        assert isinstance(self.list_view, ListView)
        if event.key == 'down':
            event.stop()
            self.list_view.action_cursor_down()
        elif event.key == 'up':
            event.stop()
            self.list_view.action_cursor_up()
        elif event.key == 'enter':
            event.stop()
            self.list_view.action_select_cursor()

    def compose(self) -> ComposeResult:
        with VerticalGroup():
            self.list_view = ListView(*self._collect_list_items(), id='inquirer-pattern-list-view',
                                      initial_index=self._find_initial_index())
            with HorizontalGroup():
                yield PromptMessage(self.message)
                yield Static(f'[{len(self.candidates)}/{len(self.choices)}]', id='inquirer-pattern-query-count-suffix')
            with HorizontalGroup(id='inquirer-pattern-query-container'):
                yield Static(f'{StandardTheme.pointer_character} ', id='inquirer-pattern-query-pointer')
                self.query = Input(id="inquirer-pattern-query")
                yield self.query
            yield self.list_view
