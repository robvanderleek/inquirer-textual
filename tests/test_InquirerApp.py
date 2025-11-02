from textual.app import App

from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.common.Choice import Choice
from inquirer_textual.common.InquirerContext import InquirerContext
from inquirer_textual.widgets.InquirerSelect import InquirerSelect
from inquirer_textual.common.Result import Result
from inquirer_textual.common.Shortcut import Shortcut


async def test_shortcut():
    widget = InquirerSelect('Environment:', [Choice('a'), Choice('b'), Choice('c')])
    context = InquirerContext(widget, shortcuts=[Shortcut('v', 'view', 'View')])
    app: InquirerApp[App[Result[Choice]]] = InquirerApp(context)

    async with app.run_test() as pilot:
        assert widget.selected_item.name == 'a'
        await pilot.press("v")
    result = app._return_value

    assert result.value.name == 'a'
    assert result.command == 'view'


def test_snapshot_shortcut(snap_compare):
    widget = InquirerSelect('Environment:', [Choice('a'), Choice('b'), Choice('c')])
    context = InquirerContext(widget, shortcuts=[Shortcut('v', 'view', 'View')], show_footer=True)
    app = InquirerApp(context)

    assert snap_compare(app)


def test_snapshot_shortcut_no_description(snap_compare):
    widget = InquirerSelect('Environment:', [Choice('a'), Choice('b'), Choice('c')])
    context = InquirerContext(widget, shortcuts=[Shortcut('v', 'view')], show_footer=True)
    app = InquirerApp(context)

    assert snap_compare(app)
