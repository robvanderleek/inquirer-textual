from typing import Any, Iterable

from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.common.Choice import Choice
from inquirer_textual.common.InquirerContext import InquirerContext
from inquirer_textual.widgets.InquirerConfirm import InquirerConfirm
from inquirer_textual.widgets.InquirerMulti import InquirerMulti
from inquirer_textual.widgets.InquirerNumber import InquirerNumber
from inquirer_textual.widgets.InquirerSecret import InquirerSecret
from inquirer_textual.widgets.InquirerText import InquirerText
from inquirer_textual.widgets.InquirerWidget import InquirerWidget
from inquirer_textual.common.Result import Result
from inquirer_textual.common.Shortcut import Shortcut
from inquirer_textual.widgets.InquirerCheckbox import InquirerCheckbox
from inquirer_textual.widgets.InquirerSelect import InquirerSelect
from textual.validation import Validator


def text(message: str, shortcuts: list[Shortcut] | None = None,
         validators: Validator | Iterable[Validator] | None = None) -> Result[str]:
    widget = InquirerText(message, validators=validators)
    InquirerContext(widget, shortcuts=shortcuts, show_footer=bool(shortcuts))
    app: InquirerApp[str] = InquirerApp()
    return app.run(inline=True)


def secret(message: str, shortcuts: list[Shortcut] | None = None) -> Result[str]:
    InquirerContext.widget = InquirerSecret(message)
    InquirerContext.shortcuts = shortcuts
    InquirerContext.show_footer = bool(shortcuts)
    app: InquirerApp[str] = InquirerApp()
    return app.run(inline=True)


def number(message: str, shortcuts: list[Shortcut] | None = None) -> Result[int]:
    InquirerContext.widget = InquirerNumber(message)
    InquirerContext.shortcuts = shortcuts
    InquirerContext.show_footer = bool(shortcuts)
    app: InquirerApp[int] = InquirerApp()
    return app.run(inline=True)


def confirm(message: str, shortcuts: list[Shortcut] | None = None, default: bool = False, mandatory: bool = True) -> \
        Result[bool]:
    InquirerContext.widget = InquirerConfirm(message, default=default, mandatory=mandatory)
    InquirerContext.shortcuts = shortcuts
    InquirerContext.show_footer = bool(shortcuts)
    app: InquirerApp[bool] = InquirerApp()
    return app.run(inline=True)


def select(message: str, choices: list[str | Choice], shortcuts: list[Shortcut] | None = None,
           default: str | Choice | None = None, mandatory: bool = True) -> Result[str | Choice]:
    InquirerContext.widget = InquirerSelect(message, choices, default, mandatory)
    InquirerContext.shortcuts = shortcuts
    InquirerContext.show_footer = bool(shortcuts)
    app: InquirerApp[str | Choice] = InquirerApp()
    return app.run(inline=True)


def checkbox(message: str, choices: list[str | Choice], shortcuts: list[Shortcut] | None = None,
             enabled: list[str | Choice] | None = None) -> Result[list[str | Choice]]:
    InquirerContext.widget = InquirerCheckbox(message, choices, enabled)
    InquirerContext.shortcuts = shortcuts
    InquirerContext.show_footer = bool(shortcuts)
    app: InquirerApp[list[str | Choice]] = InquirerApp()
    return app.run(inline=True)


def multi(widgets: list[InquirerWidget], shortcuts: list[Shortcut] | None = None) -> Result[list[Any]]:
    InquirerContext.widget = InquirerMulti(widgets)
    InquirerContext.shortcuts = shortcuts
    InquirerContext.show_footer = bool(shortcuts)
    app: InquirerApp[list[Any]] = InquirerApp()
    return app.run(inline=True)
