from dataclasses import dataclass


@dataclass
class Choice:
    name: str
    value: any = None
