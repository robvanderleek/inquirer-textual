from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.widgets.InquirerSecret import InquirerSecret


def test_snapshot(snap_compare):
    app = InquirerApp()
    app.widget = InquirerSecret('Password:')

    assert snap_compare(app)


def test_snapshot_hide_input(snap_compare):
    app = InquirerApp()
    app.widget = InquirerSecret('Password:')

    async def run_before(pilot) -> None:
        await pilot.press('a')
        await pilot.press('b')
        await pilot.press('c')

    assert snap_compare(app, run_before=run_before)


async def test_current_value():
    app = InquirerApp()
    app.widget = InquirerSecret('Password:')

    async with app.run_test() as pilot:
        await pilot.press('h', 'e', 'l', 'l', 'o')
        await pilot.press("enter")
    result = app._return_value

    assert result.value == 'hello'
