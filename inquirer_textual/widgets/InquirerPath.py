from __future__ import annotations

from enum import Enum
from pathlib import Path

from textual.app import ComposeResult
from textual.containers import HorizontalGroup
from textual.widgets import Input, Static
from typing_extensions import Self

from inquirer_textual.common.Prompt import Prompt
from inquirer_textual.widgets.InquirerWidget import InquirerWidget


class PathType(Enum):
    FILE = 'file'
    DIRECTORY = 'directory'
    ANY = 'any'


class InquirerPath(InquirerWidget):
    """An input prompt that allows the user to enter a file path."""

    DEFAULT_CSS = """
    InquirerPath {
        height: auto;
    }
    #inquirer-path-input {
        border: none;
        color: $inquirer-textual-input-color;
        padding: 0;
        height: 1;
    }
    #inquirer-path-error-message {
        color: $error;
        height: auto;
    }
    """

    def __init__(self, message: str, name: str | None = None, default: str = '', exists: bool = False,
                 path_type: PathType = PathType.ANY, mandatory: bool = False):
        """
        Args:
            message (str): The prompt message to display.
            default (str): The default value if the user presses Enter without input.
            exists (bool): If True, validate that the entered path exists.
        """
        super().__init__(name=name, mandatory=mandatory)
        self.message = message
        self.input: Input | None = None
        self.default = default
        self.exists = exists
        self.path_type = path_type

    def on_mount(self):
        super().on_mount()
        self.input.value = self.default

    def on_input_submitted(self, submitted: Input.Submitted):
        if self.exists:
            if not Path(submitted.value).exists():
                self._show_validation_error("The specified path does not exist.")
                return
        if self.path_type != PathType.ANY:
            path = Path(submitted.value)
            if self.path_type == PathType.FILE and not path.is_file():
                self._show_validation_error("The specified path is not a file.")
                return
            if self.path_type == PathType.DIRECTORY and not path.is_dir():
                self._show_validation_error("The specified path is not a directory.")
                return
        self._show_validation_error('')
        if self.input:
            self.input._cursor_visible = False
        self.submit_current_value()

    def _show_validation_error(self, message: str):
        error_message = self.query_one('#inquirer-path-error-message', Static)
        error_message.update(message)

    def focus(self, scroll_visible: bool = True) -> Self:
        if self.input:
            return self.input.focus(scroll_visible)
        else:
            return super().focus(scroll_visible)

    def current_value(self):
        return self.input.value if self.input else None

    def compose(self) -> ComposeResult:
        with HorizontalGroup():
            yield Prompt(self.message)
            self.input = Input(id="inquirer-path-input")
            yield self.input
        yield Static("", id="inquirer-path-error-message")
