from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.common.Shortcut import Shortcut
from inquirer_textual.widgets.InquirerSelect import InquirerSelect


def wizard(app: InquirerApp):
    language = app.prompt(InquirerSelect('What is your favorite programming language?',
                                         ['go', 'javascript', 'python', 'rust']),
                          shortcuts=[Shortcut('c', 'select', 'Choose')])
    app.stop({'language': language.value})


def main():
    result = InquirerApp().run(inline=True, inquiry_func=wizard)
    print(result)


if __name__ == '__main__':
    main()
