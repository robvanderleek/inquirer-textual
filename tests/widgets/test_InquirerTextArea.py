from __future__ import annotations

from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.widgets.InquirerTextArea import InquirerTextArea


def test_snapshot(snap_compare):
    app = InquirerApp()
    app.widget = InquirerTextArea('Feedback:')

    assert snap_compare(app)


def test_snapshot_with_default_value(snap_compare):
    app = InquirerApp()
    app.widget = InquirerTextArea('Feedback:', default='Love your product!\nKeep up the great work!', height=5)

    assert snap_compare(app)


async def test_named():
    widget = InquirerTextArea('Feedback:', name='feedback')
    app = InquirerApp()
    app.widget = widget

    async with app.run_test() as pilot:
        await pilot.press('H', 'e', 'l', 'l', 'o')
        await pilot.press("ctrl+enter")
    result = app._return_value

    assert result.name == 'feedback'
    assert result.value == 'Hello\n'
