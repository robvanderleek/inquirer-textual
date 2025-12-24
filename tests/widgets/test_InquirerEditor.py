from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.widgets.InquirerEditor import InquirerEditor


def test_snapshot(snap_compare):
    app = InquirerApp()
    app.widget = InquirerEditor('Analysis report:')

    async def run_before(pilot) -> None:
        await pilot.press('ctrl+c')

    assert snap_compare(app, run_before=run_before)
