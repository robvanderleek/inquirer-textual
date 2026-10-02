from inquirer_textual import prompts
from inquirer_textual.widgets.InquirerText import InquirerText

if __name__ == "__main__":
    answers = first_name = prompts.multi({
        'first_name': InquirerText('First name:'),
        'last_name': InquirerText('Last name:')
    })
    if answers.value is not None:
        print(f'Hello, {answers.value["first_name"]} {answers.value["last_name"]}! 👋')
