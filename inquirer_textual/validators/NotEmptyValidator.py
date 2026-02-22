from textual.validation import Validator, ValidationResult


class NotEmptyValidator(Validator):

    def validate(self, value: str) -> ValidationResult:
        return self.success() if value.strip() else self.failure()
