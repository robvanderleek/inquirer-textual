from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.common.InquirerContext import InquirerContext
from inquirer_textual.widgets.InquirerSecret import InquirerSecret
from inquirer_textual.common.Result import Result


def test_snapshot(snap_compare):
    widget = InquirerSecret('Password:')
    context = InquirerContext(widget)
    app = InquirerApp(context)

    assert snap_compare(app)


def test_snapshot_hide_input(snap_compare):
    widget = InquirerSecret('Password:')
    context = InquirerContext(widget)
    app = InquirerApp(context)

    async def run_before(pilot) -> None:
        await pilot.press('a')
        await pilot.press('b')
        await pilot.press('c')

    assert snap_compare(app, run_before=run_before)


async def test_current_value():
    widget = InquirerSecret('Password:')
    context = InquirerContext(widget)
    app = InquirerApp(context)

    async with app.run_test() as pilot:
        await pilot.press('h', 'e', 'l', 'l', 'o')
        assert widget.input.value == 'hello'
        await pilot.press("enter")
    result: Result[str] = app._return_value

    assert result.value == 'hello'
