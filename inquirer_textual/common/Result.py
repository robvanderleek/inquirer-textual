from __future__ import annotations

from dataclasses import dataclass
from typing import TypeVar, Generic

T = TypeVar('T')


@dataclass
class Result(Generic[T]):
    command: str | None
    value: T

    def __str__(self):
        return str(self.value)
