from dataclasses import dataclass
from typing import Any


@dataclass
class Choice:
    name: str
    value: Any = None

    def __str__(self):
        return self.name
