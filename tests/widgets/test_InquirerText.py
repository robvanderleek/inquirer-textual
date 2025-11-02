from __future__ import annotations

from typing import Iterable

from textual.validation import Validator, ValidationResult

from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.common.InquirerContext import InquirerContext
from inquirer_textual.widgets.InquirerText import InquirerText
from inquirer_textual.common.Result import Result


def test_snapshot(snap_compare):
    widget = InquirerText('Name:')
    context = InquirerContext(widget)
    app = InquirerApp(context)

    assert snap_compare(app)


def test_snapshot_with_default_value(snap_compare):
    widget = InquirerText('Name:', default='John Doe')
    context = InquirerContext(widget)
    app = InquirerApp(context)

    assert snap_compare(app)


async def test_validator_success():
    class UniqueNameValidator(Validator):
        def __init__(self, existing_names: Iterable[str] | None = None) -> None:
            super().__init__()
            self.existing_names = existing_names if existing_names else []

        def validate(self, value: str) -> ValidationResult:
            return self.failure() if value in self.existing_names else self.success()

    widget = InquirerText('Name:', validators=UniqueNameValidator(['Alice', 'Bob']))
    context = InquirerContext(widget)
    app = InquirerApp(context)

    async with app.run_test() as pilot:
        await pilot.press('C', 'h', 'a', 'r', 'l', 'i', 'e')
        assert widget.input.value == 'Charlie'
        await pilot.press("enter")
    result: Result[str] = app._return_value

    assert result.value == 'Charlie'


async def test_validator_failure():
    class UniqueNameValidator(Validator):
        def __init__(self, existing_names: Iterable[str] | None = None) -> None:
            super().__init__()
            self.existing_names = existing_names if existing_names else []

        def validate(self, value: str) -> ValidationResult:
            return self.failure() if value in self.existing_names else self.success()

    widget = InquirerText('Name:', validators=UniqueNameValidator(['Alice', 'Bob']))
    context = InquirerContext(widget)
    app = InquirerApp(context)

    async with app.run_test() as pilot:
        await pilot.press('B', 'o', 'b')
        assert widget.input.value == 'Bob'
        await pilot.press("enter")
    result: Result[str] = app._return_value

    assert result is None
