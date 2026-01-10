from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.widgets.InquirerEditor import InquirerEditor


def test_snapshot(snap_compare):
    app = InquirerApp()
    app.widget = InquirerEditor('Analysis report:')

    async def run_before(pilot) -> None:
        await pilot.press('ctrl+c')

    assert snap_compare(app, run_before=run_before)


async def test_named():
    app = InquirerApp()
    app.widget = InquirerEditor('Analysis report:', name='report')

    async with app.run_test() as pilot:
        await pilot.press("ctrl+c")
    result = app._return_value

    assert result.name == 'report'
