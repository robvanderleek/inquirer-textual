from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.common.Choice import COMMAND_SELECT
from inquirer_textual.common.InquirerResult import InquirerResult
from inquirer_textual.widgets.InquirerEcho import InquirerEcho


def test_snapshot(snap_compare):
    app = InquirerApp()
    app.widget = InquirerEcho('[bold]Hello[/bold] [green]world![/green]')

    assert snap_compare(app)


async def test_result():
    app = InquirerApp()
    app.widget = InquirerEcho('[bold]Hello[/bold] [green]world![/green]')

    async with app.run_test() as pilot:
        await pilot.press('enter')
    result = app._return_value

    assert isinstance(result, InquirerResult)
    assert result.command == COMMAND_SELECT
    assert result.value is None
