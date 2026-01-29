from textual.validation import Regex

from inquirer_textual import prompts
from inquirer_textual.widgets.InquirerCheckbox import InquirerCheckbox
from inquirer_textual.widgets.InquirerConfirm import InquirerConfirm
from inquirer_textual.widgets.InquirerNumber import InquirerNumber
from inquirer_textual.widgets.InquirerSelect import InquirerSelect
from inquirer_textual.widgets.InquirerText import InquirerText

if __name__ == "__main__":
    print("Hi, welcome to Python Pizza!")
    answers = prompts.multi([
        ('toBeDelivered', InquirerConfirm('Is this for delivery?')),
        ('phone', InquirerText('What is your phone number?', validators=Regex('\d+[-]\d+'))),
        ('size', InquirerSelect('What size do you need?', ['Large', 'Medium', 'Small'])),
        ('quantity', InquirerNumber('How many do you need?')),
        ('toppings', InquirerCheckbox('What about the toppings?', choices=['Pepperoni', 'Mushrooms', 'Onions'])),
        ('beverage', InquirerSelect('You also get a free 2L beverage, what would you like?', ["Pepsi", "7up", "Coke"])),
        ('comments', InquirerText('Any comments on your purchase experience?', default='Nope, all good!'))
    ])
    print(answers)
