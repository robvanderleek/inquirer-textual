from __future__ import annotations

from dataclasses import dataclass

from rich.text import Text

from inquirer_textual.common.Shortcut import Shortcut


@dataclass
class PromptSettings:
    clear: bool = False
    header: str | Text | list[str | Text] | None = None
    inline: bool = True
    mandatory: bool = False
    mouse: bool = False
    shortcuts: list[Shortcut] | None = None
    theme: str = 'inquirer-textual-default'
