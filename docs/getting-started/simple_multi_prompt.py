from inquirer_textual import prompts
from inquirer_textual.widgets.InquirerText import InquirerText

if __name__ == "__main__":
    answers = first_name = prompts.multi({
        'first_name': InquirerText('First name:'),
        'last_name': InquirerText('Last name:')
    })
    print(f'Hello, {answers["first_name"]} {answers["last_name"]}! 👋')
