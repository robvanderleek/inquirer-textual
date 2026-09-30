from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.widgets.InquirerEcho import InquirerEcho


def test_snapshot(snap_compare):
    app = InquirerApp()
    app.widget = InquirerEcho('[bold]Hello[/bold] [green]world![/green]')

    assert snap_compare(app)


async def test_result():
    app = InquirerApp()
    app.widget = InquirerEcho('[bold]Hello[/bold] [green]world![/green]')

    result = app._return_value

    assert result is None
