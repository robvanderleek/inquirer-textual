from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.widgets.InquirerSecret import InquirerSecret
from inquirer_textual.widgets.Result import Result


def test_snapshot(snap_compare):
    widget = InquirerSecret('Password:')
    app = InquirerApp(widget)

    assert snap_compare(app)


def test_snapshot_hide_input(snap_compare):
    widget = InquirerSecret('Password:')
    app = InquirerApp(widget)

    async def run_before(pilot) -> None:
        await pilot.press('a')
        await pilot.press('b')
        await pilot.press('c')

    assert snap_compare(app, run_before=run_before)


async def test_current_value():
    widget = InquirerSecret('Password:')
    app = InquirerApp(widget)

    async with app.run_test() as pilot:
        await pilot.press('h', 'e', 'l', 'l', 'o')
        assert widget.current_value() == 'hello'
        await pilot.press("enter")
    result: Result[str] = app._return_value

    assert result.value == 'hello'
