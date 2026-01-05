from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.common.Choice import Choice
from inquirer_textual.widgets.InquirerPattern import InquirerPattern


async def test_select_entry():
    app = InquirerApp()
    app.widget = InquirerPattern('Environment:', [Choice('a'), Choice('b'), Choice('c')])

    async with app.run_test() as pilot:
        await pilot.press("down")
        await pilot.press("enter")
    result = app._return_value

    assert result.value.name == 'b'
    assert result.command == 'select'


async def test_pattern_search():
    app = InquirerApp()
    app.widget = InquirerPattern('Environment:', [Choice('a'), Choice('b'), Choice('c')])

    async with app.run_test() as pilot:
        await pilot.press("c")
        await pilot.press("enter")
    result = app._return_value

    assert result.value.name == 'c'
    assert result.command == 'select'


def test_snapshot_pattern_search(snap_compare):
    app = InquirerApp()
    app.widget = InquirerPattern('Environment:', ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon'])

    async def run_before(pilot) -> None:
        await pilot.press('i', 'u', 'm')

    assert snap_compare(app, run_before=run_before)
