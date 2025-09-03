from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.widgets.Choice import Choice
from inquirer_textual.widgets.InquirerSelect import InquirerSelect
from inquirer_textual.widgets.SelectResult import SelectResult
from inquirer_textual.widgets.Shortcut import Shortcut


async def test_select_up_down():
    widget = InquirerSelect('Environment:', [Choice('a'), Choice('b'), Choice('c')])
    app = InquirerApp(widget)
    async with app.run_test() as pilot:
        assert widget.selected_item.name == 'a'
        await pilot.press("down")
        assert widget.selected_item.name == 'b'
        await pilot.press("down")
        assert widget.selected_item.name == 'c'
        await pilot.press("up")
        assert widget.selected_item.name == 'b'


async def test_select():
    widget = InquirerSelect('Environment:', [Choice('a'), Choice('b'), Choice('c')])
    app = InquirerApp(widget)

    async with app.run_test() as pilot:
        assert widget.selected_item.name == 'a'
        await pilot.press("down")
        await pilot.press("enter")
    result: SelectResult = app._return_value

    assert result.choice.name == 'b'
    assert result.command == 'select'


async def test_shortcut():
    widget = InquirerSelect('Environment:', [Choice('a'), Choice('b'), Choice('c')], [Shortcut('v', 'view', 'View')])
    app = InquirerApp(widget)

    async with app.run_test() as pilot:
        assert widget.selected_item.name == 'a'
        await pilot.press("v")
    result: SelectResult = app._return_value

    assert result.choice.name == 'a'
    assert result.command == 'view'


def test_shortcut_snapshot(snap_compare):
    widget = InquirerSelect('Environment:', [Choice('a'), Choice('b'), Choice('c')], [Shortcut('v', 'view', 'View')])
    app = InquirerApp(widget)

    assert snap_compare(app)


def test_shortcut_no_description_snapshot(snap_compare):
    widget = InquirerSelect('Environment:', [Choice('a'), Choice('b'), Choice('c')], [Shortcut('v', 'view')])
    app = InquirerApp(widget)

    assert snap_compare(app)
