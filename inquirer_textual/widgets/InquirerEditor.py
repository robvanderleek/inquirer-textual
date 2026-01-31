from __future__ import annotations

import os
import tempfile

from textual import events
from textual.app import ComposeResult
from textual.containers import HorizontalGroup
from textual.widgets import Static

from inquirer_textual.common.Prompt import Prompt
from inquirer_textual.widgets.InquirerWidget import InquirerWidget


class InquirerEditor(InquirerWidget):
    """An input widget that uses an external editor."""

    DEFAULT_CSS = """
        InquirerEditor {
            height: auto;
        }
        """
    can_focus = True

    def __init__(self, message: str | None = None, name: str | None = None):
        """
        Args:
            message (str): The prompt message to display.
            name (str): The name of the prompt.
        """
        super().__init__(name=name)
        self.message = message

    def on_mount(self):
        super().on_mount()
        if not self.message:
            self._launch_editor()

    def on_key(self, event: events.Key):
        if event.key == 'enter':
            event.stop()
            self._launch_editor()

    def _launch_editor(self):
        with self.app.suspend():
            tmp = tempfile.NamedTemporaryFile()
            filename = tmp.name
            os.system(f"{get_editor_command()} {filename}")
        with open(filename, 'r') as f:
            content = f.read()
        os.unlink(filename)
        self.post_message(InquirerWidget.Submit(content))

    def compose(self) -> ComposeResult:
        if self.message:
            with HorizontalGroup():
                yield Prompt(self.message)
                yield Static('[dim]Press <enter> to launch editor[/dim]')
        else:
            super().compose()


def get_editor_command() -> str:
    editor = os.environ.get('VISUAL')
    if not editor:
        editor = os.environ.get('EDITOR')
    if editor == 'nano':
        return 'nano -R'
    elif editor == 'code':
        return 'code -w -n'
    else:
        return 'vim -f -o'
