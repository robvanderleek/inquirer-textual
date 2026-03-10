import sys
from typing import Any

from textual.theme import BUILTIN_THEMES
from textual.validation import Regex

from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.widgets.InquirerCheckbox import InquirerCheckbox
from inquirer_textual.widgets.InquirerConfirm import InquirerConfirm
from inquirer_textual.widgets.InquirerMulti import InquirerMulti
from inquirer_textual.widgets.InquirerNumber import InquirerNumber
from inquirer_textual.widgets.InquirerSelect import InquirerSelect
from inquirer_textual.widgets.InquirerText import InquirerText

if __name__ == '__main__':
    all_themes = BUILTIN_THEMES.keys()
    if len(sys.argv) == 0:
        theme = 'inquirer-textual-default'
    elif sys.argv[1] in all_themes:
        theme = sys.argv[1]
    else:
        print(f"Theme '{sys.argv[1]}' is not recognized. Available themes are: {', '.join(all_themes)}")
        sys.exit(1)
    app: InquirerApp[dict[str, Any]] = InquirerApp(theme=theme)
    app.widget = InquirerMulti({
        'toBeDelivered': InquirerConfirm('Is this for delivery?'),
        'phone': InquirerText('What is your phone number?', validators=Regex('\\d+[-]\\d+')),
        'size': InquirerSelect('What size do you need?', ['Large', 'Medium', 'Small']),
        'quantity': InquirerNumber('How many do you need?'),
        'toppings': InquirerCheckbox('What about the toppings?', choices=['Pepperoni', 'Mushrooms', 'Onions']),
        'beverage': InquirerSelect('You also get a free 2L beverage, what would you like?', ["Pepsi", "7up", "Coke"]),
        'comments': InquirerText('Any comments on your purchase experience?', default='Nope, all good!')
    })
    answers = app.run().value
    print(answers)
