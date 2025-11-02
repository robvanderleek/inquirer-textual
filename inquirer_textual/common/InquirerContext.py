from dataclasses import dataclass
from threading import Event

from inquirer_textual.common.Result import Result
from inquirer_textual.common.Shortcut import Shortcut
from inquirer_textual.widgets.InquirerWidget import InquirerWidget

@dataclass
class InquirerContext:
    widget: InquirerWidget
    shortcuts: list[Shortcut] | None = None
    show_footer: bool = False
    result: Result | None = None
    result_ready: Event = Event()
