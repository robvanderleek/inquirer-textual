from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

from inquirer_textual.widgets.base.InquirerWidget import InquirerWidget


@dataclass
class Shortcut:
    key: str
    command: str
    description: str | None = None
    show: bool = True
    check: Callable[[InquirerWidget], bool] | None = None

    def __post_init__(self):
        if self.description is None:
            self.description = self.command
        if self.check is None:
            self.check = lambda widget: True
