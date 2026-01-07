from dataclasses import dataclass

from inquirer_textual.common.Shortcut import Shortcut


@dataclass
class AppConfig:
    inline: bool = True
    shortcuts: list[Shortcut] | None = None
