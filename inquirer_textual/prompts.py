from typing import Any, Iterable

from textual.validation import Validator

from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.common.AppConfig import AppConfig
from inquirer_textual.common.Choice import Choice
from inquirer_textual.common.InquirerResult import InquirerResult
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


def checkbox(message: str, choices: list[str | Choice], name: str | None = None,
             enabled: list[str | Choice] | None = None, mandatory: bool = False, app_config: AppConfig = AppConfig()) \
        -> \
                InquirerResult[list[str | Choice]]:
    app: InquirerApp[list[str | Choice]] = InquirerApp()
    app.widget = InquirerCheckbox(message, choices, name=name, enabled=enabled, mandatory=mandatory)
    app.shortcuts = app_config.shortcuts
    app.show_footer = bool(app_config.shortcuts)
    return app.run(inline=app_config.inline)


def confirm(message: str, name: str | None = None, default: bool = False, mandatory: bool = False,
            app_config: AppConfig = AppConfig()) -> InquirerResult[bool]:
    app: InquirerApp[bool] = InquirerApp()
    app.widget = InquirerConfirm(message, name=name, default=default, mandatory=mandatory)
    app.shortcuts = app_config.shortcuts
    app.show_footer = bool(app_config.shortcuts)
    return app.run(inline=app_config.inline)


def editor(message: str, name: str | None = None, app_config: AppConfig = AppConfig()) -> InquirerResult[str]:
    app: InquirerApp[str] = InquirerApp()
    app.widget = InquirerEditor(message, name=name)
    app.shortcuts = app_config.shortcuts
    app.show_footer = bool(app_config.shortcuts)
    return app.run(inline=False)


def external(widget: InquirerWidget, app_config: AppConfig = AppConfig()) -> InquirerResult[int]:
    app: InquirerApp[int] = InquirerApp()
    app.widget = widget
    app.shortcuts = app_config.shortcuts
    app.show_footer = bool(app_config.shortcuts)
    return app.run(inline=app_config.inline)


def multi(widgets: list[InquirerWidget], app_config: AppConfig = AppConfig()) -> InquirerResult[list[Any]]:
    app: InquirerApp[list[Any]] = InquirerApp()
    app.widget = InquirerMulti(widgets)
    app.shortcuts = app_config.shortcuts
    app.show_footer = bool(app_config.shortcuts)
    return app.run(inline=app_config.inline)


def number(message: str, name: str | None = None, mandatory: bool = False, app_config: AppConfig = AppConfig()) -> \
        InquirerResult[int]:
    app: InquirerApp[int] = InquirerApp()
    app.widget = InquirerNumber(message, name=name, mandatory=mandatory)
    app.shortcuts = app_config.shortcuts
    app.show_footer = bool(app_config.shortcuts)
    return app.run(inline=app_config.inline)


def path(message: str, name: str | None = None, exists: bool = False, path_type: PathType = PathType.ANY,
         mandatory: bool = False, app_config: AppConfig = AppConfig()) -> InquirerResult[str]:
    app: InquirerApp[str] = InquirerApp()
    app.widget = InquirerPath(message, name=name, exists=exists, path_type=path_type, mandatory=mandatory)
    app.shortcuts = app_config.shortcuts
    app.show_footer = bool(app_config.shortcuts)
    return app.run(inline=app_config.inline)


def pattern(message: str, choices: list[str | Choice], name: str | None = None, default: str | Choice | None = None,
            mandatory: bool = False, app_config: AppConfig = AppConfig()) -> InquirerResult[str | Choice]:
    app: InquirerApp[str | Choice] = InquirerApp()
    app.widget = InquirerPattern(message, choices, name=name, default=default, mandatory=mandatory)
    app.shortcuts = app_config.shortcuts
    app.show_footer = bool(app_config.shortcuts)
    return app.run(inline=app_config.inline)


def secret(message: str, name: str | None = None, mandatory: bool = False, app_config: AppConfig = AppConfig()) -> \
        InquirerResult[str]:
    app: InquirerApp[str] = InquirerApp()
    app.widget = InquirerSecret(message, name=name, mandatory=mandatory)
    app.shortcuts = app_config.shortcuts
    app.show_footer = bool(app_config.shortcuts)
    return app.run(inline=app_config.inline)


def select(message: str, choices: list[str | Choice], name: str | None = None, default: str | Choice | None = None,
           mandatory: bool = False, app_config: AppConfig = AppConfig()) -> InquirerResult[str | Choice]:
    app: InquirerApp[str | Choice] = InquirerApp()
    app.widget = InquirerSelect(message, choices, name=name, default=default, mandatory=mandatory)
    app.shortcuts = app_config.shortcuts
    app.show_footer = bool(app_config.shortcuts)
    return app.run(inline=app_config.inline)


def text(message: str, name: str | None = None, default: str = '',
         validators: Validator | Iterable[Validator] | None = None, mandatory: bool = False,
         app_config: AppConfig = AppConfig()) -> InquirerResult[str]:
    app: InquirerApp[str] = InquirerApp()
    app.widget = InquirerText(message, name=name, default=default, validators=validators, mandatory=mandatory)
    app.shortcuts = app_config.shortcuts
    app.show_footer = bool(app_config.shortcuts)
    return app.run(inline=app_config.inline)
