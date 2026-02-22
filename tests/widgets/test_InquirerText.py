from __future__ import annotations

from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.validators.UniqueValidator import UniqueValidator
from inquirer_textual.widgets.InquirerText import InquirerText


def test_snapshot(snap_compare):
    app = InquirerApp()
    app.widget = InquirerText('Name:')

    assert snap_compare(app)


def test_snapshot_with_default_value(snap_compare):
    app = InquirerApp()
    app.widget = InquirerText('Name:', default='John Doe')

    assert snap_compare(app)


async def test_validator_success():
    widget = InquirerText('Name:', validators=UniqueValidator(['Alice', 'Bob']))
    app = InquirerApp()
    app.widget = widget

    async with app.run_test() as pilot:
        await pilot.press('C', 'h', 'a', 'r', 'l', 'i', 'e')
        assert widget.input.value == 'Charlie'
        await pilot.press("enter")
    result = app._return_value

    assert result.value == 'Charlie'


async def test_validator_failure():
    widget = InquirerText('Name:', validators=UniqueValidator(['Alice', 'Bob']))
    app = InquirerApp()
    app.widget = widget

    async with app.run_test() as pilot:
        await pilot.press('B', 'o', 'b')
        assert widget.input.value == 'Bob'
        await pilot.press("enter")
    result = app._return_value

    assert result is None


async def test_named():
    widget = InquirerText('Name:', name='username')
    app = InquirerApp()
    app.widget = widget

    async with app.run_test() as pilot:
        await pilot.press('C', 'h', 'a', 'r', 'l', 'i', 'e')
        await pilot.press("enter")
    result = app._return_value

    assert result.name == 'username'
    assert result.value == 'Charlie'
