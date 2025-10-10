from typing import Iterable

from textual.validation import Validator, ValidationResult

from inquirer_textual import prompts


class UniqueNameValidator(Validator):
    def __init__(self, existing_names: Iterable[str] | None = None) -> None:
        super().__init__()
        self.existing_names = existing_names if existing_names else []

    def validate(self, value: str) -> ValidationResult:
        return self.failure() if value in self.existing_names else self.success()

if __name__ == '__main__':
    answer = prompts.text('Name:', validators=UniqueNameValidator(['Alice', 'Bob']))
    print(answer)
