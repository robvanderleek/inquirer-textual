from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.widgets.InquirerSelect import InquirerSelect
from inquirer_textual.widgets.InquirerText import InquirerText


def text(message: str) -> str:
    text_widget = InquirerText(message)
    app = InquirerApp(text_widget)
    return app.run(inline=True, inline_no_clear=True)


def select(message: str, choices: list[str]) -> str:
    select_widget = InquirerSelect(message, choices)
    app = InquirerApp(select_widget)
    return app.run(inline=True, inline_no_clear=True)


if __name__ == "__main__":
    answer = text("Enter your name:")
    print(f'Your answer: {answer}')
    answer = select('Environment:', ['production', 'staging', 'development'])
    print(f'Your answer: {answer}')
