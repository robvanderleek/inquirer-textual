from textual import events
from textual.app import ComposeResult
from textual.containers import HorizontalGroup
from textual.geometry import Offset
from textual.widgets import Input, OptionList
from textual.widgets.option_list import Option

from inquirer_textual.common.Candidate import Candidate
from inquirer_textual.common.Prompt import Prompt
from inquirer_textual.common.match_utils import fuzzy_match
from inquirer_textual.widgets.InquirerWidget import InquirerWidget


class InquirerAutocompleteOption(Option):
    def __init__(self, candidate: Candidate):
        super().__init__(candidate.choice)
        self.candidate = candidate


class InquirerAutocomplete(InquirerWidget):
    DEFAULT_CSS = """
        InquirerAutocomplete {
            height: auto;
        }
        #inquirer-autocomplete-input {
            border: none;
            color: $inquirer-textual-input-color;
            padding: 0;
            height: 1;
        }
        #inquirer-autocomplete-option-list {
            width: auto;
            height: auto;
            max-height: 5;
            padding: 0;
            margin: 0;
            border: none;
            scrollbar-size-vertical: 1;
        }
        .option-list--option-highlighted {
            color: $block-cursor-blurred-foreground !important;
        }
    """

    def __init__(self, message: str, completions: list[str]):
        super().__init__()
        self._message = message
        self._completions = completions
        self._candidates: list[Candidate] = [Candidate(c) for c in completions]
        self._input: Input | None = None
        self._option_list: OptionList | None = None
        self._selected_value: str | None = None

    def on_mount(self):
        super().on_mount()
        self._option_list.styles.display = 'none'

    def on_key(self, event: events.Key):
        if self._option_list is None:
            return
        if event.key == 'down':
            if self._option_list.styles.display == 'none':
                self._option_list.styles.display = 'block'
                self._option_list.highlighted = 0
                self._align_option_list()
            else:
                self._option_list.action_cursor_down()
        elif event.key == 'up':
            self._option_list.action_cursor_up()
        elif event.key == 'enter':
            option = self._option_list.get_option_at_index(self._option_list.highlighted)
            with self.prevent(Input.Changed):
                self._input.value = ''
                self._input.insert_text_at_cursor(option.prompt)
            self._option_list.styles.display = 'none'

    def on_input_changed(self, changed: Input.Changed):
        self._align_option_list()
        self._option_list.clear_options()
        query = changed.value.strip()
        candidates = fuzzy_match(query, self._completions)
        self._option_list.add_options([c.render(self.app) for c in candidates])

    def _align_option_list(self):
        offset = self._input.cursor_screen_offset
        self._option_list.absolute_offset = Offset(offset.x - 1, offset.y + 1)

    def compose(self) -> ComposeResult:
        with HorizontalGroup():
            yield Prompt(self._message)
            self._input = Input(id="inquirer-autocomplete-input")
            yield self._input
        self._option_list = OptionList(*[c.render(self.app) for c in self._candidates],
                                       id="inquirer-autocomplete-option-list")
        self._option_list.can_focus = False
        yield self._option_list
