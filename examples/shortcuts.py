from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.common.Shortcut import Shortcut
from inquirer_textual.widgets.InquirerText import InquirerText

if __name__ == '__main__':
    app: InquirerApp[str] = InquirerApp()
    app.widget = InquirerText('Enter your name:')
    app._shortcuts = [Shortcut('escape', 'select')]
    app.show_footer = True
    answer = app.run()
    print(f'Your answer: {answer}')
