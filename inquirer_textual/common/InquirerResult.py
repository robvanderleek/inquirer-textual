from __future__ import annotations

import json
from dataclasses import dataclass
from typing import TypeVar, Generic

T = TypeVar('T')


@dataclass
class InquirerResult(Generic[T]):
    name: str | None
    value: T | None
    command: str | None

    def __str__(self) -> str:
        return str(self.value)

    def json(self):
        d = {}
        if self.name:
            d[self.name] = self.value
        else:
            d['value'] = self.value
        if self.command:
            d['command'] = self.command
        return json.dumps(d)
