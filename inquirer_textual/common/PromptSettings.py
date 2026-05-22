from dataclasses import dataclass

from inquirer_textual.common.Shortcut import Shortcut


@dataclass
class PromptSettings:
    clear: bool = False
    inline: bool = True
    mandatory: bool = False
    mouse: bool = False
    shortcuts: list[Shortcut] | None = None
    theme: str = 'inquirer-textual-default'
