from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.widgets.InquirerText import InquirerText

if __name__ == '__main__':
    widget = InquirerText('What is your name?')
    app: InquirerApp[str] = InquirerApp(widget)
    result = app.run()
    print(result)