from typing import Iterable

from textual.validation import Validator, ValidationResult


class UniqueValidator(Validator):
    def __init__(self, existing_names: Iterable[str] | None = None) -> None:
        super().__init__()
        self.existing_names = existing_names if existing_names else []

    def validate(self, value: str) -> ValidationResult:
        return self.failure() if value in self.existing_names else self.success()
