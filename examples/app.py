from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.widgets.InquirerSelect import InquirerSelect
from inquirer_textual.widgets.InquirerText import InquirerText


def wizard(app: InquirerApp):
    name = app.prompt(InquirerText('What is your name?'))
    language = app.prompt(InquirerSelect(f'Hi {name}, what is your favorite programming language?',
                                         ['python', 'javascript', 'rust', 'go']))
    what = app.prompt(InquirerSelect(f'And what do you like so much about {language}?',
                                     ['Syntax', 'Performance', 'Community', 'Libraries']))
    app.stop([name.value if name else None, language.value if language else None, what.value if what else None])


def main():
    result = InquirerApp().run(inline=True, inquiry_func=wizard)
    print(result)


if __name__ == '__main__':
    main()
