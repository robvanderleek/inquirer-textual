from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.widgets.Choice import Choice
from inquirer_textual.widgets.InquirerSelect import InquirerSelect


async def test_select():
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
