from dataclasses import dataclass
from typing import TypeVar

T = TypeVar('T')


@dataclass
class Result[T]:
    command: str | None
    value: T

    def __str__(self):
        return str(self.value)
