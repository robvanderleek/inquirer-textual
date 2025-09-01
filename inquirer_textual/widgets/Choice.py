from dataclasses import dataclass
from typing import Any


@dataclass
class Choice:
    name: str
    value: Any = None
