from typing import Any

from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.widgets.InquirerMulti import InquirerMulti
from inquirer_textual.widgets.InquirerSecret import InquirerSecret
from inquirer_textual.widgets.Choice import Choice
from inquirer_textual.widgets.InquirerConfirm import InquirerConfirm
from inquirer_textual.widgets.InquirerNumber import InquirerNumber
from inquirer_textual.widgets.InquirerText import InquirerText
from inquirer_textual.widgets.InquirerWidget import InquirerWidget
from inquirer_textual.widgets.Result import Result
from inquirer_textual.widgets.Shortcut import Shortcut
from inquirer_textual.widgets.checkbox.InquirerCheckbox import InquirerCheckbox
from inquirer_textual.widgets.select.InquirerSelect import InquirerSelect


def text(message: str, shortcuts: list[Shortcut] | None = None) -> Result[str]:
    widget = InquirerText(message)
    app: InquirerApp[str] = InquirerApp(widget, shortcuts, show_footer=bool(shortcuts))
    return app.run(inline=True)


def secret(message: str, shortcuts: list[Shortcut] | None = None) -> Result[str]:
    widget = InquirerSecret(message)
    app: InquirerApp[str] = InquirerApp(widget, shortcuts, show_footer=bool(shortcuts))
    return app.run(inline=True)


def number(message: str, shortcuts: list[Shortcut] | None = None) -> Result[int]:
    widget = InquirerNumber(message)
    app: InquirerApp[int] = InquirerApp(widget, shortcuts, show_footer=bool(shortcuts))
    return app.run(inline=True)


def confirm(message: str, shortcuts: list[Shortcut] | None = None) -> Result[bool]:
    widget = InquirerConfirm(message)
    app: InquirerApp[bool] = InquirerApp(widget, shortcuts, show_footer=bool(shortcuts))
    return app.run(inline=True)


def select(message: str, choices: list[str | Choice], shortcuts: list[Shortcut] | None = None,
           default: str | Choice | None = None, mandatory: bool = True) -> Result | None:
    widget = InquirerSelect(message, choices, default, mandatory)
    app: InquirerApp[str | Choice] = InquirerApp(widget, shortcuts, show_footer=bool(shortcuts))
    return app.run(inline=True)


def checkbox(message: str, choices: list[str | Choice], shortcuts: list[Shortcut] | None = None,
             enabled: list[str | Choice] | None = None) -> Result[list[str | Choice]]:
    widget = InquirerCheckbox(message, choices, enabled)
    app: InquirerApp[list[str | Choice]] = InquirerApp(widget, shortcuts, show_footer=bool(shortcuts))
    return app.run(inline=True)

def multi(widgets: list[InquirerWidget], shortcuts: list[Shortcut] | None = None) -> Result[list[Any]]:
    widget = InquirerMulti(widgets)
    app: InquirerApp[list[Any]] = InquirerApp(widget, shortcuts, show_footer=bool(shortcuts))
    return app.run(inline=True)