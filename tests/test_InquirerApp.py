from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.widgets.Choice import Choice
from inquirer_textual.widgets.InquirerSelect import InquirerSelect
from inquirer_textual.widgets.SelectResult import SelectResult
from inquirer_textual.widgets.Shortcut import Shortcut


async def test_shortcut():
    widget = InquirerSelect('Environment:', [Choice('a'), Choice('b'), Choice('c')], [Shortcut('v', 'view', 'View')])
    app = InquirerApp(widget)

    async with app.run_test() as pilot:
        assert widget.selected_item.name == 'a'
        await pilot.press("v")
    result: SelectResult = app._return_value

    assert result.choice.name == 'a'
    assert result.command == 'view'


def test_snapshot_shortcut(snap_compare):
    widget = InquirerSelect('Environment:', [Choice('a'), Choice('b'), Choice('c')], [Shortcut('v', 'view', 'View')])
    app = InquirerApp(widget, show_footer=True)

    assert snap_compare(app)


def test_snapshot_shortcut_no_description(snap_compare):
    widget = InquirerSelect('Environment:', [Choice('a'), Choice('b'), Choice('c')], [Shortcut('v', 'view')])
    app = InquirerApp(widget, show_footer=True)

    assert snap_compare(app)
