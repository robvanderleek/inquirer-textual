from __future__ import annotations

from typing import Any, Iterable, Literal

from textual.validation import Validator

from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.common.Choice import Choice
from inquirer_textual.common.InquirerResult import InquirerResult
from inquirer_textual.common.PromptSettings import PromptSettings
from inquirer_textual.widgets.InquirerCheckbox import InquirerCheckbox
from inquirer_textual.widgets.InquirerConfirm import InquirerConfirm
from inquirer_textual.widgets.InquirerEditor import InquirerEditor
from inquirer_textual.widgets.InquirerFuzzy import InquirerFuzzy
from inquirer_textual.widgets.InquirerMulti import InquirerMulti
from inquirer_textual.widgets.InquirerNumber import InquirerNumber
from inquirer_textual.widgets.InquirerPath import InquirerPath, PathType
from inquirer_textual.widgets.InquirerPattern import InquirerPattern
from inquirer_textual.widgets.InquirerSecret import InquirerSecret
from inquirer_textual.widgets.InquirerSelect import InquirerSelect
from inquirer_textual.widgets.InquirerText import InquirerText
from inquirer_textual.widgets.InquirerTextArea import InquirerTextArea
from inquirer_textual.widgets.InquirerWaitForKey import InquirerWaitForKey
from inquirer_textual.widgets.InquirerWidget import InquirerWidget


def checkbox(message: str, choices: list[str | Choice], enabled: list[str | Choice] | None = None,
             settings: PromptSettings = PromptSettings()) -> InquirerResult[
    list[str | Choice]]:
    app: InquirerApp[list[str | Choice]] = InquirerApp()
    app.widget = InquirerCheckbox(message, choices, enabled=enabled, mandatory=settings.mandatory)
    app.shortcuts = settings.shortcuts
    return app.run(inline=True, inline_no_clear=not settings.clear, mouse=settings.mouse)


def confirm(message: str, default: bool = False, settings: PromptSettings = PromptSettings()) -> InquirerResult[bool]:
    app: InquirerApp[bool] = InquirerApp()
    app.widget = InquirerConfirm(message, default=default, mandatory=settings.mandatory)
    app.shortcuts = settings.shortcuts
    return app.run(inline=True, inline_no_clear=not settings.clear, mouse=settings.mouse)


def editor(message: str, settings: PromptSettings = PromptSettings()) -> InquirerResult[str]:
    app: InquirerApp[str] = InquirerApp()
    app.widget = InquirerEditor(message)
    return app.run(inline=False, mouse=settings.mouse)


def external(widget: InquirerWidget, settings: PromptSettings = PromptSettings()) -> Any:
    app: InquirerApp[Any] = InquirerApp()
    app.widget = widget
    app.shortcuts = settings.shortcuts
    return app.run(inline=True, inline_no_clear=not settings.clear, mouse=settings.mouse)


def fuzzy(message: str, choices: list[str | Choice], default: str | Choice | None = None,
          settings: PromptSettings = PromptSettings()) -> InquirerResult[str | Choice]:
    app: InquirerApp[str | Choice] = InquirerApp()
    app.widget = InquirerFuzzy(message, choices, default=default, mandatory=settings.mandatory)
    app.shortcuts = settings.shortcuts
    return app.run(inline=True, inline_no_clear=not settings.clear, mouse=settings.mouse)


def multi(widgets: dict[str, InquirerWidget], settings: PromptSettings = PromptSettings()) -> InquirerResult[
    dict[str, Any]]:
    app: InquirerApp[dict[str, Any]] = InquirerApp()
    app.widget = InquirerMulti(widgets)
    app.shortcuts = settings.shortcuts
    return app.run(inline=True, inline_no_clear=not settings.clear, mouse=settings.mouse)


def number(message: str, default: int | float | None = None, input_type: Literal['integer', 'number'] = 'integer',
           settings: PromptSettings = PromptSettings()) -> InquirerResult[int | float]:
    app: InquirerApp[int | float] = InquirerApp()
    app.widget = InquirerNumber(message, default=default, input_type=input_type, mandatory=settings.mandatory)
    app.shortcuts = settings.shortcuts
    return app.run(inline=True, inline_no_clear=not settings.clear, mouse=settings.mouse)


def path(message: str, exists: bool = False, path_type: PathType = PathType.ANY,
         settings: PromptSettings = PromptSettings()) -> InquirerResult[str]:
    app: InquirerApp[str] = InquirerApp()
    app.widget = InquirerPath(message, exists=exists, path_type=path_type, mandatory=settings.mandatory)
    app.shortcuts = settings.shortcuts
    return app.run(inline=True, inline_no_clear=not settings.clear, mouse=settings.mouse)


def pattern(message: str, choices: list[str | Choice], default: str | Choice | None = None,
            settings: PromptSettings = PromptSettings()) -> InquirerResult[str | Choice]:
    app: InquirerApp[str | Choice] = InquirerApp()
    app.widget = InquirerPattern(message, choices, default=default, mandatory=settings.mandatory)
    app.shortcuts = settings.shortcuts
    return app.run(inline=True, inline_no_clear=not settings.clear, mouse=settings.mouse)


def secret(message: str, settings: PromptSettings = PromptSettings()) -> InquirerResult[str]:
    app: InquirerApp[str] = InquirerApp()
    app.widget = InquirerSecret(message, mandatory=settings.mandatory)
    app.shortcuts = settings.shortcuts
    return app.run(inline=True, inline_no_clear=not settings.clear, mouse=settings.mouse)


def select(message: str, choices: list[str | Choice], default: str | Choice | None = None,
           height: int | str | None = None, settings: PromptSettings = PromptSettings()) -> InquirerResult[
    str | Choice]:
    app: InquirerApp[str | Choice] = InquirerApp()
    app.widget = InquirerSelect(message, choices, default=default, mandatory=settings.mandatory, height=height)
    app.shortcuts = settings.shortcuts
    return app.run(inline=True, inline_no_clear=not settings.clear, mouse=settings.mouse)


def text(message: str, default: str = '', validators: Validator | Iterable[Validator] | None = None,
         settings: PromptSettings = PromptSettings()) -> InquirerResult[str]:
    app: InquirerApp[str] = InquirerApp()
    app.widget = InquirerText(message, default=default, validators=validators, mandatory=settings.mandatory)
    app.shortcuts = settings.shortcuts
    return app.run(inline=True, inline_no_clear=not settings.clear, mouse=settings.mouse)


def text_area(message: str, default: str = '', settings: PromptSettings = PromptSettings()) -> InquirerResult[str]:
    app: InquirerApp[str] = InquirerApp()
    app.widget = InquirerTextArea(message, default=default, mandatory=settings.mandatory)
    app.shortcuts = settings.shortcuts
    return app.run(inline=True, inline_no_clear=not settings.clear, mouse=settings.mouse)


def wait_for_key(message: str, key: str = 'enter', settings: PromptSettings = PromptSettings()) -> InquirerResult[None]:
    app: InquirerApp[None] = InquirerApp()
    app.widget = InquirerWaitForKey(message, key=key, mandatory=settings.mandatory)
    app.shortcuts = settings.shortcuts
    return app.run(inline=True, inline_no_clear=not settings.clear, mouse=settings.mouse)
