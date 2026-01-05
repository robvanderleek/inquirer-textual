from dataclasses import dataclass
from typing import Any


@dataclass
class Choice:
    name: str
    data: Any = None
    command: str = 'select'

    def __str__(self) -> str:
        return self.name
