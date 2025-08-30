from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.widgets.Choice import Choice
from inquirer_textual.widgets.InquirerSelect import InquirerSelect
from inquirer_textual.widgets.InquirerText import InquirerText


def text(message: str) -> str:
    text_widget = InquirerText(message)
    app = InquirerApp(text_widget)
    return app.run(inline=True, inline_no_clear=True)


def select(message: str, choices: list[str | Choice]) -> str:
    if all(isinstance(c, str) for c in choices):
        choices = [Choice(name=c) for c in choices]
    select_widget = InquirerSelect(message, choices)
    app = InquirerApp(select_widget)
    return app.run(inline=True, inline_no_clear=True)
