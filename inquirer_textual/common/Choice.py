from dataclasses import dataclass
from typing import Any

COMMAND_SELECT = 'select'

@dataclass
class Choice:
    name: str
    data: Any = None
    command: str = COMMAND_SELECT

    def __str__(self) -> str:
        return self.name
