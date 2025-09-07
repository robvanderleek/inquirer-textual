from textual.app import App

from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.widgets.Choice import Choice
from inquirer_textual.widgets.InquirerSelect import InquirerSelect
from inquirer_textual.widgets.InquirerText import InquirerText
from inquirer_textual.widgets.SelectResult import SelectResult
from inquirer_textual.widgets.Shortcut import Shortcut


def text(message: str) -> str:
    text_widget = InquirerText(message)
    app = InquirerApp(text_widget)
    return app.run(inline=True, inline_no_clear=True)


def select(message: str, choices: list[str | Choice], shortcuts: list[Shortcut] | None = None) -> SelectResult | None:
    if all(isinstance(c, str) for c in choices):
        choices = [Choice(name=c) for c in choices]
    select_widget = InquirerSelect(message, choices, shortcuts)
    app: InquirerApp[App[SelectResult]] = InquirerApp(select_widget, show_footer=bool(shortcuts))
    return app.run(inline=True, inline_no_clear=False)
