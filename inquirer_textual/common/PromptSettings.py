from dataclasses import dataclass

from inquirer_textual.common.Shortcut import Shortcut


@dataclass
class PromptSettings:
    mandatory: bool = False
    shortcuts: list[Shortcut] | None = None
    clear: bool = False
    mouse: bool = False