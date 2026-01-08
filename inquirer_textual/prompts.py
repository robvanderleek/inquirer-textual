from typing import Any, Iterable

from textual.validation import Validator

from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.common.AppConfig import AppConfig
from inquirer_textual.common.Choice import Choice
from inquirer_textual.common.Result import Result
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
             mandatory: bool = False, app_config: AppConfig = AppConfig()) -> Result[list[str | Choice]]:
    app: InquirerApp[list[str | Choice]] = InquirerApp()
    app.widget = InquirerCheckbox(message, choices, enabled, mandatory=mandatory)
    app.shortcuts = app_config.shortcuts
    app.show_footer = bool(app_config.shortcuts)
    return app.run(inline=app_config.inline)


def confirm(message: str, default: bool = False, mandatory: bool = False, app_config: AppConfig = AppConfig()) -> \
        Result[bool]:
    app: InquirerApp[bool] = InquirerApp()
    app.widget = InquirerConfirm(message, default=default, mandatory=mandatory)
    app.shortcuts = app_config.shortcuts
    app.show_footer = bool(app_config.shortcuts)
    return app.run(inline=app_config.inline)


def editor(message: str, app_config: AppConfig = AppConfig()) -> Result[str]:
    app: InquirerApp[str] = InquirerApp()
    app.widget = InquirerEditor(message)
    app.shortcuts = app_config.shortcuts
    app.show_footer = bool(app_config.shortcuts)
    return app.run(inline=False)


def external(widget: InquirerWidget, app_config: AppConfig = AppConfig()) -> Result[int]:
    app: InquirerApp[int] = InquirerApp()
    app.widget = widget
    app.shortcuts = app_config.shortcuts
    app.show_footer = bool(app_config.shortcuts)
    return app.run(inline=app_config.inline)


def pattern(message: str, choices: list[str | Choice], default: str | Choice | None = None, mandatory: bool = False,
            app_config: AppConfig = AppConfig()) -> Result[str | Choice]:
    app: InquirerApp[str | Choice] = InquirerApp()
    app.widget = InquirerPattern(message, choices, default, mandatory=mandatory)
    app.shortcuts = app_config.shortcuts
    app.show_footer = bool(app_config.shortcuts)
    return app.run(inline=app_config.inline)


def multi(widgets: list[InquirerWidget], app_config: AppConfig = AppConfig()) -> Result[list[Any]]:
    app: InquirerApp[list[Any]] = InquirerApp()
    app.widget = InquirerMulti(widgets)
    app.shortcuts = app_config.shortcuts
    app.show_footer = bool(app_config.shortcuts)
    return app.run(inline=app_config.inline)


def number(message: str, mandatory: bool = False, app_config: AppConfig = AppConfig()) -> Result[int]:
    app: InquirerApp[int] = InquirerApp()
    app.widget = InquirerNumber(message, mandatory=mandatory)
    app.shortcuts = app_config.shortcuts
    app.show_footer = bool(app_config.shortcuts)
    return app.run(inline=app_config.inline)


def path(message: str, exists: bool = False, path_type: PathType = PathType.ANY, is_dir: bool = True,
         mandatory: bool = False, app_config: AppConfig = AppConfig()) -> Result[str]:
    app: InquirerApp[str] = InquirerApp()
    app.widget = InquirerPath(message, exists=exists, path_type=path_type, mandatory=mandatory)
    app.shortcuts = app_config.shortcuts
    app.show_footer = bool(app_config.shortcuts)
    return app.run(inline=app_config.inline)


def secret(message: str, mandatory: bool = False, app_config: AppConfig = AppConfig()) -> Result[str]:
    app: InquirerApp[str] = InquirerApp()
    app.widget = InquirerSecret(message, mandatory=mandatory)
    app.shortcuts = app_config.shortcuts
    app.show_footer = bool(app_config.shortcuts)
    return app.run(inline=app_config.inline)


def select(message: str, choices: list[str | Choice], default: str | Choice | None = None, mandatory: bool = False,
           app_config: AppConfig = AppConfig()) -> Result[str | Choice]:
    app: InquirerApp[str | Choice] = InquirerApp()
    app.widget = InquirerSelect(message, choices, default, mandatory=mandatory)
    app.shortcuts = app_config.shortcuts
    app.show_footer = bool(app_config.shortcuts)
    return app.run(inline=app_config.inline)


def text(message: str, validators: Validator | Iterable[Validator] | None = None, mandatory: bool = False,
         app_config: AppConfig = AppConfig()) -> Result[str]:
    app: InquirerApp[str] = InquirerApp()
    app.widget = InquirerText(message, validators=validators, mandatory=mandatory)
    app.shortcuts = app_config.shortcuts
    app.show_footer = bool(app_config.shortcuts)
    return app.run(inline=app_config.inline)
