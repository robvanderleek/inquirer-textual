from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.common.Choice import Choice
from inquirer_textual.common.Shortcut import Shortcut
from inquirer_textual.widgets.InquirerSelect import InquirerSelect


async def test_shortcut():
    widget = InquirerSelect('Environment:', [Choice('a'), Choice('b'), Choice('c')])
    app = InquirerApp()
    app.widget = widget
    app.shortcuts = [Shortcut('v', 'view', 'View')]

    async with app.run_test() as pilot:
        assert widget.selected_item.name == 'a'
        await pilot.press("v")
    result = app._return_value

    assert result.value.name == 'a'
    assert result.command == 'view'


def test_snapshot_shortcut(snap_compare):
    app = InquirerApp()
    app.widget = InquirerSelect('Environment:', [Choice('a'), Choice('b'), Choice('c')])
    app.shortcuts = [Shortcut('v', 'view', 'View')]
    app.show_footer = True

    assert snap_compare(app)


def test_snapshot_shortcut_no_description(snap_compare):
    app = InquirerApp()
    app.widget = InquirerSelect('Environment:', [Choice('a'), Choice('b'), Choice('c')])
    app.shortcuts = [Shortcut('v', 'view')]
    app.show_footer = True

    assert snap_compare(app)
