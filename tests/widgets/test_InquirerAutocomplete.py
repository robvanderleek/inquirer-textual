from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.widgets.InquirerAutocomplete import InquirerAutocomplete


def test_snapshot_normal_input(snap_compare):
    app = InquirerApp()
    app.widget = InquirerAutocomplete('Planet:',
                                      ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'])

    async def run_before(pilot) -> None:
        await pilot.press('E', 'a', 'r', 't', 'h')

    assert snap_compare(app, run_before=run_before)


def test_snapshot_show_option_list(snap_compare):
    app = InquirerApp()
    app.widget = InquirerAutocomplete('Planet:',
                                      ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'])

    async def run_before(pilot) -> None:
        await pilot.press('E', 'r')
        await pilot.press('down')

    assert snap_compare(app, run_before=run_before)


def test_snapshot_hide_option_list(snap_compare):
    app = InquirerApp()
    app.widget = InquirerAutocomplete('Planet:',
                                      ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'])

    async def run_before(pilot) -> None:
        await pilot.press('E', 'r')
        await pilot.press('down')
        await pilot.press('escape')

    assert snap_compare(app, run_before=run_before)


def test_snapshot_select_option_from_list(snap_compare):
    app = InquirerApp()
    app.widget = InquirerAutocomplete('Planet:',
                                      ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'])

    async def run_before(pilot) -> None:
        await pilot.press('E', 'r')
        await pilot.press('down')
        await pilot.press('down')
        await pilot.press('down')
        await pilot.press('enter')

    assert snap_compare(app, run_before=run_before)
