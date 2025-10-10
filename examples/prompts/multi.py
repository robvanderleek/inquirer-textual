from inquirer_textual import prompts
from inquirer_textual.widgets.InquirerCheckbox import InquirerCheckbox
from inquirer_textual.widgets.InquirerConfirm import InquirerConfirm
from inquirer_textual.widgets.InquirerNumber import InquirerNumber
from inquirer_textual.widgets.InquirerSecret import InquirerSecret
from inquirer_textual.widgets.InquirerText import InquirerText
from inquirer_textual.widgets.InquirerSelect import InquirerSelect

if __name__ == '__main__':
    text_widget = InquirerText('Name:')
    password_widget = InquirerSecret('Password:')
    number_widget = InquirerNumber('Memory:')
    confirm_widget = InquirerConfirm('Proceed?')
    select_widget = InquirerSelect('Planet?', ['Earth', 'Mars', 'Venus'], default='Mars')
    checkbox_widget = InquirerCheckbox("People?", choices=['Alice', 'Bob', 'Charlie'])
    answer = prompts.multi(
        [text_widget, password_widget, number_widget, confirm_widget, select_widget, checkbox_widget])
    print(answer)
