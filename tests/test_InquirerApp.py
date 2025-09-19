from textual.app import App

from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.widgets.Choice import Choice
from inquirer_textual.widgets.select.InquirerSelect import InquirerSelect
from inquirer_textual.widgets.Result import Result
from inquirer_textual.widgets.Shortcut import Shortcut


async def test_shortcut():
    widget = InquirerSelect('Environment:', [Choice('a'), Choice('b'), Choice('c')])
    app: InquirerApp[App[Result[Choice]]] = InquirerApp(widget, [Shortcut('v', 'view', 'View')])

    async with app.run_test() as pilot:
        assert widget.selected_item.name == 'a'
        await pilot.press("v")
    result = app._return_value

    assert result.value.name == 'a'
    assert result.command == 'view'


def test_snapshot_shortcut(snap_compare):
    widget = InquirerSelect('Environment:', [Choice('a'), Choice('b'), Choice('c')])
    app = InquirerApp(widget, shortcuts=[Shortcut('v', 'view', 'View')], show_footer=True)

    assert snap_compare(app)


def test_snapshot_shortcut_no_description(snap_compare):
    widget = InquirerSelect('Environment:', [Choice('a'), Choice('b'), Choice('c')])
    app = InquirerApp(widget, shortcuts=[Shortcut('v', 'view')], show_footer=True)

    assert snap_compare(app)
