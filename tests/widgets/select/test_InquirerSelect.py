from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.widgets.Choice import Choice
from inquirer_textual.widgets.Result import Result
from inquirer_textual.widgets.select.InquirerSelect import InquirerSelect


async def test_select_entry():
    widget = InquirerSelect('Environment:', [Choice('a'), Choice('b'), Choice('c')])
    app = InquirerApp(widget)

    async with app.run_test() as pilot:
        assert widget.selected_item.name == 'a'
        await pilot.press("down")
        await pilot.press("enter")
    result: Result[Choice] = app._return_value

    assert result.value.name == 'b'
    assert result.command == 'select'


async def test_up_down():
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


async def test_default():
    choices = [Choice('a'), Choice('b'), Choice('c')]
    widget = InquirerSelect('Environment:', choices, default=choices[1])
    app = InquirerApp(widget)
    async with app.run_test():
        assert widget.selected_item.name == 'b'


async def test_choice_with_command():
    widget = InquirerSelect('Environment:', [Choice('a', command='create'), Choice('b')])
    app = InquirerApp(widget)

    async with app.run_test() as pilot:
        assert widget.selected_item.name == 'a'
        await pilot.press("enter")
    result: Result[Choice] = app._return_value

    assert result.command == 'create'


async def test_mandatory():
    widget = InquirerSelect('Environment:', [Choice('a'), Choice('b'), Choice('c')], mandatory=True)
    app = InquirerApp(widget)
    async with app.run_test() as pilot:
        await pilot.press("ctrl+c")
    result: Result[Choice] = app._return_value

    assert result is None


async def test_not_mandatory():
    widget = InquirerSelect('Environment:', [Choice('a'), Choice('b'), Choice('c')], mandatory=False)
    app = InquirerApp(widget)
    async with app.run_test() as pilot:
        await pilot.press("ctrl+c")
    result: Result[Choice] = app._return_value

    assert result.command is None
    assert result.value is None


def test_snapshot_mandatory(snap_compare):
    widget = InquirerSelect('Environment:', [Choice('a'), Choice('b'), Choice('c')], mandatory=True)
    app = InquirerApp(widget)

    async def run_before(pilot) -> None:
        await pilot.press('ctrl+c')

    assert snap_compare(app, run_before=run_before)


def test_snapshot_not_mandatory(snap_compare):
    widget = InquirerSelect('Environment:', [Choice('a'), Choice('b'), Choice('c')], mandatory=False)
    app = InquirerApp(widget)

    async def run_before(pilot) -> None:
        await pilot.press('ctrl+c')

    assert snap_compare(app, run_before=run_before)
