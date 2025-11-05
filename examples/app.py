from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.widgets.InquirerSelect import InquirerSelect
from inquirer_textual.widgets.InquirerText import InquirerText


def wizard(app: InquirerApp):
    name = app.prompt(InquirerText('What is your name?'))
    language = app.prompt(InquirerSelect(f'{name}, what is your favorite programming language?',
                                         ['python', 'javascript', 'rust', 'go']))
    app.prompt(InquirerSelect(f'And what do you like so much about {language}?',
                              ['Syntax', 'Performance', 'Community', 'Libraries']))
    app.stop()


def main():
    app: InquirerApp[str] = InquirerApp()
    app.run(inline=True, inquiry_func=wizard)


if __name__ == '__main__':
    main()
