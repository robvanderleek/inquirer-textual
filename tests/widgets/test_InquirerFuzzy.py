from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.common.Choice import Choice
from inquirer_textual.widgets.InquirerFuzzy import InquirerFuzzy


async def test_fuzzy_search():
    app = InquirerApp()
    app.widget = InquirerFuzzy('Environment:', [Choice('a'), Choice('b'), Choice('c')])

    async with app.run_test() as pilot:
        await pilot.press("c")
        await pilot.press("enter")
    result = app._return_value

    assert result.value.name == 'c'
    assert result.command == 'select'


def test_snapshot_fuzzy_search(snap_compare):
    app = InquirerApp()
    app.widget = InquirerFuzzy('Environment:', ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon'])

    async def run_before(pilot) -> None:
        await pilot.press('i', 'm')

    assert snap_compare(app, run_before=run_before)
