from dataclasses import dataclass


@dataclass
class Shortcut:
    key: str
    command: str
    description: str | None = None
