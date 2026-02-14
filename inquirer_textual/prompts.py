from typing import Any, Iterable

from textual.validation import Validator

from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.common.Choice import Choice
from inquirer_textual.common.InquirerResult import InquirerResult
from inquirer_textual.common.Shortcut import Shortcut
from inquirer_textual.widgets.InquirerCheckbox import InquirerCheckbox
from inquirer_textual.widgets.InquirerConfirm import InquirerConfirm
from inquirer_textual.widgets.InquirerEditor import InquirerEditor
from inquirer_textual.widgets.InquirerMulti import InquirerMulti
from inquirer_textual.widgets.InquirerNumber import InquirerNumber
from inquirer_textual.widgets.InquirerPath import InquirerPath, PathType
from inquirer_textual.widgets.InquirerPattern import InquirerPattern
from inquirer_textual.widgets.InquirerSecret import InquirerSecret
from inquirer_textual.widgets.InquirerSelect import InquirerSelect
from inquirer_textual.widgets.InquirerText import InquirerText
from inquirer_textual.widgets.InquirerWidget import InquirerWidget


def checkbox(message: str, choices: list[str | Choice], enabled: list[str | Choice] | None = None,
             mandatory: bool = False, shortcuts: list[Shortcut] | None = None, clear: bool = False) -> InquirerResult[
    list[str | Choice]]:
    app: InquirerApp[list[str | Choice]] = InquirerApp()
    app.widget = InquirerCheckbox(message, choices, enabled=enabled, mandatory=mandatory)
    app.shortcuts = shortcuts
    return app.run(inline=True, inline_no_clear=not clear)


def confirm(message: str, default: bool = False, mandatory: bool = False, shortcuts: list[Shortcut] | None = None,
            clear: bool = False) -> InquirerResult[bool]:
    app: InquirerApp[bool] = InquirerApp()
    app.widget = InquirerConfirm(message, default=default, mandatory=mandatory)
    app.shortcuts = shortcuts
    return app.run(inline=True, inline_no_clear=not clear)


def editor(message: str) -> InquirerResult[str]:
    app: InquirerApp[str] = InquirerApp()
    app.widget = InquirerEditor(message)
    return app.run(inline=False)


def external(widget: InquirerWidget, shortcuts: list[Shortcut] | None = None, clear: bool = False) -> Any:
    app: InquirerApp[Any] = InquirerApp()
    app.widget = widget
    app.shortcuts = shortcuts
    return app.run(inline=True, inline_no_clear=not clear)


def multi(widgets: dict[str, InquirerWidget], shortcuts: list[Shortcut] | None = None, clear: bool = False) -> \
        InquirerResult[dict[str, Any]]:
    app: InquirerApp[dict[str, Any]] = InquirerApp()
    app.widget = InquirerMulti(widgets)
    app.shortcuts = shortcuts
    return app.run(inline=True, inline_no_clear=not clear)


def number(message: str, mandatory: bool = False, shortcuts: list[Shortcut] | None = None, clear: bool = False) -> \
        InquirerResult[int]:
    app: InquirerApp[int] = InquirerApp()
    app.widget = InquirerNumber(message, mandatory=mandatory)
    app.shortcuts = shortcuts
    return app.run(inline=True, inline_no_clear=not clear)


def path(message: str, exists: bool = False, path_type: PathType = PathType.ANY, mandatory: bool = False,
         shortcuts: list[Shortcut] | None = None, clear: bool = False) -> InquirerResult[str]:
    app: InquirerApp[str] = InquirerApp()
    app.widget = InquirerPath(message, exists=exists, path_type=path_type, mandatory=mandatory)
    app.shortcuts = shortcuts
    return app.run(inline=True, inline_no_clear=not clear)


def pattern(message: str, choices: list[str | Choice], default: str | Choice | None = None,
            mandatory: bool = False, shortcuts: list[Shortcut] | None = None, clear: bool = False) -> InquirerResult[
    str | Choice]:
    app: InquirerApp[str | Choice] = InquirerApp()
    app.widget = InquirerPattern(message, choices, default=default, mandatory=mandatory)
    app.shortcuts = shortcuts
    return app.run(inline=True, inline_no_clear=not clear)


def secret(message: str, mandatory: bool = False, shortcuts: list[Shortcut] | None = None, clear: bool = False) -> \
        InquirerResult[str]:
    app: InquirerApp[str] = InquirerApp()
    app.widget = InquirerSecret(message, mandatory=mandatory)
    app.shortcuts = shortcuts
    return app.run(inline=True, inline_no_clear=not clear)


def select(message: str, choices: list[str | Choice], default: str | Choice | None = None,
           mandatory: bool = False, shortcuts: list[Shortcut] | None = None, clear: bool = False) -> InquirerResult[
    str | Choice]:
    app: InquirerApp[str | Choice] = InquirerApp()
    app.widget = InquirerSelect(message, choices, default=default, mandatory=mandatory)
    app.shortcuts = shortcuts
    return app.run(inline=True, inline_no_clear=not clear)


def text(message: str, default: str = '', validators: Validator | Iterable[Validator] | None = None,
         mandatory: bool = False, shortcuts: list[Shortcut] | None = None, clear: bool = False) -> InquirerResult[str]:
    app: InquirerApp[str] = InquirerApp()
    app.widget = InquirerText(message, default=default, validators=validators, mandatory=mandatory)
    app.shortcuts = shortcuts
    return app.run(inline=True, inline_no_clear=not clear)
