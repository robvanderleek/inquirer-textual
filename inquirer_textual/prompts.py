from typing import Any, Iterable

from textual.validation import Validator

from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.common.Choice import Choice
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
             mandatory: bool = False) -> list[str | Choice]:
    app: InquirerApp[list[str | Choice]] = InquirerApp()
    app.widget = InquirerCheckbox(message, choices, enabled=enabled, mandatory=mandatory)
    return app.run(inline=True).value


def confirm(message: str, default: bool = False, mandatory: bool = False) -> bool:
    app: InquirerApp[bool] = InquirerApp()
    app.widget = InquirerConfirm(message, default=default, mandatory=mandatory)
    return app.run(inline=True).value


def editor(message: str) -> str:
    app: InquirerApp[str] = InquirerApp()
    app.widget = InquirerEditor(message)
    return app.run(inline=True).value


def external(widget: InquirerWidget) -> Any:
    app: InquirerApp[Any] = InquirerApp()
    app.widget = widget
    return app.run(inline=True).value


def multi(widgets: list[tuple[str, InquirerWidget]]) -> dict[str, Any]:
    app: InquirerApp[dict[str, Any]] = InquirerApp()
    app.widget = InquirerMulti(widgets)
    return app.run(inline=True).value


def number(message: str, mandatory: bool = False) -> int:
    app: InquirerApp[int] = InquirerApp()
    app.widget = InquirerNumber(message, mandatory=mandatory)
    return app.run(inline=True).value


def path(message: str, exists: bool = False, path_type: PathType = PathType.ANY, mandatory: bool = False) -> str:
    app: InquirerApp[str] = InquirerApp()
    app.widget = InquirerPath(message, exists=exists, path_type=path_type, mandatory=mandatory)
    return app.run(inline=True).value


def pattern(message: str, choices: list[str | Choice], default: str | Choice | None = None,
            mandatory: bool = False) -> str | Choice:
    app: InquirerApp[str | Choice] = InquirerApp()
    app.widget = InquirerPattern(message, choices, default=default, mandatory=mandatory)
    return app.run(inline=True).value


def secret(message: str, mandatory: bool = False) -> str:
    app: InquirerApp[str] = InquirerApp()
    app.widget = InquirerSecret(message, mandatory=mandatory)
    return app.run(inline=True).value


def select(message: str, choices: list[str | Choice], default: str | Choice | None = None,
           mandatory: bool = False) -> str | Choice:
    app: InquirerApp[str | Choice] = InquirerApp()
    app.widget = InquirerSelect(message, choices, default=default, mandatory=mandatory)
    return app.run(inline=True).value


def text(message: str, default: str = '', validators: Validator | Iterable[Validator] | None = None,
         mandatory: bool = False) -> str:
    app: InquirerApp[str] = InquirerApp()
    app.widget = InquirerText(message, default=default, validators=validators, mandatory=mandatory)
    return app.run(inline=True).value
