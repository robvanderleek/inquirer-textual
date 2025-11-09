from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.widgets.InquirerCheckbox import InquirerCheckbox


async def test_select_entries():
    app = InquirerApp()
    app.widget = InquirerCheckbox('Choice:', ['a', 'b', 'c'])

    async with app.run_test() as pilot:
        await pilot.press("space")
        await pilot.press("down")
        await pilot.press("down")
        await pilot.press("space")
        await pilot.press("enter")
    result = app._return_value

    assert result.value == ['a', 'c']
    assert result.command == 'select'


def test_snapshot(snap_compare):
    app = InquirerApp()
    app.widget = InquirerCheckbox('Choice:', ['a', 'b', 'c'])

    async def run_before(pilot) -> None:
        await pilot.press("space")
        await pilot.press("down")
        await pilot.press("down")
        await pilot.press("space")

    assert snap_compare(app, run_before=run_before)
