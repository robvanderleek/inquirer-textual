from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.common.Result import Result
from inquirer_textual.widgets.InquirerCheckbox import InquirerCheckbox


async def test_select_entries():
    widget = InquirerCheckbox('Choice:', ['a', 'b', 'c'])
    app = InquirerApp(widget)

    async with app.run_test() as pilot:
        assert widget.selected_item == 'a'
        await pilot.press("space")
        await pilot.press("down")
        await pilot.press("down")
        await pilot.press("space")
        await pilot.press("enter")
    result: Result[list[str]] = app._return_value

    assert result.value == ['a', 'c']
    assert result.command == 'select'


def test_snapshot(snap_compare):
    widget = InquirerCheckbox('Choice:', ['a', 'b', 'c'])
    app = InquirerApp(widget)

    async def run_before(pilot) -> None:
        await pilot.press("space")
        await pilot.press("down")
        await pilot.press("down")
        await pilot.press("space")

    assert snap_compare(app, run_before=run_before)
