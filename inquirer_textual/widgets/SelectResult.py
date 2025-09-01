from dataclasses import dataclass

from inquirer_textual.widgets.Choice import Choice


@dataclass
class SelectResult:
    command: str
    choice: str | Choice
