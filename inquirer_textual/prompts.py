from typing import Any, Iterable

from textual.validation import Validator

from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.common.Choice import Choice
from inquirer_textual.common.Result import Result
from inquirer_textual.common.Shortcut import Shortcut
from inquirer_textual.widgets.InquirerCheckbox import InquirerCheckbox
from inquirer_textual.widgets.InquirerConfirm import InquirerConfirm
from inquirer_textual.widgets.InquirerEditor import InquirerEditor
from inquirer_textual.widgets.InquirerMulti import InquirerMulti
from inquirer_textual.widgets.InquirerNumber import InquirerNumber
from inquirer_textual.widgets.InquirerSecret import InquirerSecret
from inquirer_textual.widgets.InquirerSelect import InquirerSelect
from inquirer_textual.widgets.InquirerText import InquirerText
from inquirer_textual.widgets.InquirerWidget import InquirerWidget


def checkbox(message: str, choices: list[str | Choice], shortcuts: list[Shortcut] | None = None,
             enabled: list[str | Choice] | None = None) -> Result[list[str | Choice]]:
    app: InquirerApp[list[str | Choice]] = InquirerApp()
    app.widget = InquirerCheckbox(message, choices, enabled)
    app.shortcuts = shortcuts
    app.show_footer = bool(shortcuts)
    return app.run(inline=True)


def confirm(message: str, shortcuts: list[Shortcut] | None = None, default: bool = False, mandatory: bool = False) -> \
        Result[bool]:
    app: InquirerApp[bool] = InquirerApp()
    app.widget = InquirerConfirm(message, default=default, mandatory=mandatory)
    app.shortcuts = shortcuts
    app.show_footer = bool(shortcuts)
    return app.run(inline=True)


def editor(message: str) -> Result[str]:
    app: InquirerApp[str] = InquirerApp()
    app.widget = InquirerEditor(message)
    return app.run()


def external(widget: InquirerWidget, shortcuts: list[Shortcut] | None = None) -> Result[int]:
    app: InquirerApp[int] = InquirerApp()
    app.widget = widget
    app.shortcuts = shortcuts
    app.show_footer = bool(shortcuts)
    return app.run(inline=True)


def multi(widgets: list[InquirerWidget], shortcuts: list[Shortcut] | None = None) -> Result[list[Any]]:
    app: InquirerApp[list[Any]] = InquirerApp()
    app.widget = InquirerMulti(widgets)
    app.shortcuts = shortcuts
    app.show_footer = bool(shortcuts)
    return app.run(inline=True)


def number(message: str, shortcuts: list[Shortcut] | None = None) -> Result[int]:
    app: InquirerApp[int] = InquirerApp()
    app.widget = InquirerNumber(message)
    app.shortcuts = shortcuts
    app.show_footer = bool(shortcuts)
    return app.run(inline=True)


def secret(message: str, shortcuts: list[Shortcut] | None = None) -> Result[str]:
    app: InquirerApp[str] = InquirerApp()
    app.widget = InquirerSecret(message)
    app.shortcuts = shortcuts
    app.show_footer = bool(shortcuts)
    return app.run(inline=True)


def select(message: str, choices: list[str | Choice], shortcuts: list[Shortcut] | None = None,
           default: str | Choice | None = None, mandatory: bool = False) -> Result[str | Choice]:
    app: InquirerApp[str | Choice] = InquirerApp()
    app.widget = InquirerSelect(message, choices, default, mandatory)
    app.shortcuts = shortcuts
    app.show_footer = bool(shortcuts)
    return app.run(inline=True)


def text(message: str, shortcuts: list[Shortcut] | None = None,
         validators: Validator | Iterable[Validator] | None = None) -> Result[str]:
    app: InquirerApp[str] = InquirerApp()
    app.widget = InquirerText(message, validators=validators)
    app.shortcuts = shortcuts
    app.show_footer = bool(shortcuts)
    return app.run(inline=True)
