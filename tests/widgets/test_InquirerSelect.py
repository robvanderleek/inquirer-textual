from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.common.Choice import Choice
from inquirer_textual.widgets.InquirerSelect import InquirerSelect


async def test_select_entry():
    app = InquirerApp()
    app.widget = InquirerSelect('Environment:', [Choice('a'), Choice('b'), Choice('c')])

    async with app.run_test() as pilot:
        await pilot.press("down")
        await pilot.press("enter")
    result = app._return_value

    assert result.value.name == 'b'
    assert result.command == 'select'


async def test_up_down():
    widget = InquirerSelect('Environment:', [Choice('a'), Choice('b'), Choice('c')])
    app = InquirerApp()
    app.widget = widget
    async with app.run_test() as pilot:
        assert widget.selected_item.name == 'a'
        await pilot.press("down")
        assert widget.selected_item.name == 'b'
        await pilot.press("down")
        assert widget.selected_item.name == 'c'
        await pilot.press("up")
        assert widget.selected_item.name == 'b'


async def test_default():
    choices = [Choice('a'), Choice('b'), Choice('c')]
    widget = InquirerSelect('Environment:', choices, default=choices[1])
    app = InquirerApp()
    app.widget = widget
    async with app.run_test():
        assert widget.selected_item.name == 'b'


async def test_choice_with_command():
    widget = InquirerSelect('Environment:', [Choice('a', command='create'), Choice('b')])
    app = InquirerApp()
    app.widget = widget

    async with app.run_test() as pilot:
        assert widget.selected_item.name == 'a'
        await pilot.press("enter")
    result = app._return_value

    assert result.command == 'create'


async def test_mandatory():
    app = InquirerApp()
    app.widget = InquirerSelect('Environment:', [Choice('a'), Choice('b'), Choice('c')], mandatory=True)
    async with app.run_test() as pilot:
        await pilot.press("ctrl+c")
    result = app._return_value

    assert result is None


async def test_not_mandatory():
    app = InquirerApp()
    app.widget = InquirerSelect('Environment:', [Choice('a'), Choice('b'), Choice('c')], mandatory=False)

    async with app.run_test() as pilot:
        await pilot.press("ctrl+c")
    result = app._return_value

    assert result.command is None
    assert result.value is None


def test_snapshot_mandatory(snap_compare):
    app = InquirerApp()
    app.widget = InquirerSelect('Environment:', [Choice('a'), Choice('b'), Choice('c')], mandatory=True)

    async def run_before(pilot) -> None:
        await pilot.press('ctrl+c')

    assert snap_compare(app, run_before=run_before)


def test_snapshot_not_mandatory(snap_compare):
    app = InquirerApp()
    app.widget = InquirerSelect('Environment:', [Choice('a'), Choice('b'), Choice('c')], mandatory=False)

    async def run_before(pilot) -> None:
        await pilot.press('ctrl+c')

    assert snap_compare(app, run_before=run_before)
