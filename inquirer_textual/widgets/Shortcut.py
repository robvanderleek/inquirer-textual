from dataclasses import dataclass


@dataclass
class Shortcut:
    key: str
    command: str
    description: str | None = None
    show: bool = True

    def __post_init__(self):
        if self.description is None:
            self.description = self.command