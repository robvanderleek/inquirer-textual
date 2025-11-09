from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.widgets.InquirerSelect import InquirerSelect
from inquirer_textual.widgets.InquirerText import InquirerText


def wizard(app: InquirerApp):
    name = app.prompt(InquirerText('What is your name?'))
    language = app.prompt(InquirerSelect(f'Hi {name}, what is your favorite programming language?',
                                         ['python', 'javascript', 'rust', 'go']))
    why = app.prompt(InquirerSelect(f'And what do you like so much about {language}?',
                                    ['Syntax', 'Performance', 'Community', 'Libraries']))
    app.stop({'name': name.value, 'language': language.value, 'why': why.value})


def main():
    result = InquirerApp().run(inline=True, inquiry_func=wizard)
    print(result)


if __name__ == '__main__':
    main()
