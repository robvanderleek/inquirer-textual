from textual.app import App

from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.widgets.Choice import Choice
from inquirer_textual.widgets.InquirerNumber import InquirerNumber
from inquirer_textual.widgets.InquirerSelect import InquirerSelect
from inquirer_textual.widgets.InquirerText import InquirerText
from inquirer_textual.widgets.Result import Result
from inquirer_textual.widgets.Shortcut import Shortcut


def text(message: str, shortcuts: list[Shortcut] | None = None) -> Result[str]:
    widget = InquirerText(message)
    app: InquirerApp[str] = InquirerApp(widget, shortcuts, show_footer=bool(shortcuts))
    return app.run(inline=True)


def number(message: str, shortcuts: list[Shortcut] | None = None) -> Result[int]:
    widget = InquirerNumber(message)
    app = InquirerApp(widget, shortcuts, show_footer=bool(shortcuts))
    return app.run(inline=True)


def select(message: str, choices: list[str | Choice], shortcuts: list[Shortcut] | None = None,
           default: Choice | None = None) -> Result | None:
    if all(isinstance(c, str) for c in choices):
        choices = [Choice(name=c) for c in choices]
    widget = InquirerSelect(message, choices, default)
    app: InquirerApp[App[Result[str | Choice]]] = InquirerApp(widget, shortcuts, show_footer=bool(shortcuts))
    return app.run(inline=True)
