from textual import events
from textual.app import ComposeResult
from textual.containers import HorizontalGroup
from textual.geometry import Offset
from textual.widgets import Input, OptionList

from inquirer_textual.common.Prompt import Prompt
from inquirer_textual.widgets.InquirerWidget import InquirerWidget


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
            border: none;
            padding: 0;
        }
        
        .option-list--option-highlighted {
            color: $block-cursor-blurred-foreground !important;
        }
    """

    def __init__(self, message: str, candidates: list[str]):
        super().__init__()
        self.message = message
        self.candidates = candidates
        self.input: Input | None = None
        self.option_list: OptionList | None = None

    def on_key(self, event: events.Key):
        if self.option_list is None:
            return
        if event.key == 'down':
            self.option_list.action_cursor_down()
        elif event.key == 'up':
            self.option_list.action_cursor_up()
        elif event.key == 'enter':
            option = self.option_list.get_option_at_index(self.option_list.highlighted)
            self.input.value = option.prompt

    def on_input_changed(self, changed: Input.Changed):
        offset = self.app.cursor_position
        self.option_list.absolute_offset = Offset(offset.x - 1, offset.y + 1)
        self.app.refresh(layout=True)

    def compose(self) -> ComposeResult:
        with HorizontalGroup():
            yield Prompt(self.message)
            self.input = Input(id="inquirer-autocomplete-input")
            yield self.input
            self.option_list = OptionList(*self.candidates, id="inquirer-autocomplete-option-list")
            self.option_list.can_focus = False
            yield self.option_list
