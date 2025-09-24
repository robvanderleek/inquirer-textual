from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.widgets.InquirerSecret import InquirerSecret


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
