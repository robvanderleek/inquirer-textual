from inquirer_textual import prompts
from inquirer_textual.widgets.InquirerCheckbox import InquirerCheckbox
from inquirer_textual.widgets.InquirerConfirm import InquirerConfirm
from inquirer_textual.widgets.InquirerNumber import InquirerNumber
from inquirer_textual.widgets.InquirerSecret import InquirerSecret
from inquirer_textual.widgets.InquirerSelect import InquirerSelect
from inquirer_textual.widgets.InquirerText import InquirerText

if __name__ == '__main__':
    answer = prompts.multi([
        ('name', InquirerText('Name:')),
        ('password', InquirerSecret('Password:')),
        ('memory', InquirerNumber('Memory:')),
        ('proceed', InquirerConfirm('Proceed?')),
        ('planet', InquirerSelect('Planet?', ['Earth', 'Mars', 'Venus'], default='Mars')),
        ('people', InquirerCheckbox("People?", choices=['Alice', 'Bob', 'Charlie']))
    ])
    print(answer)
