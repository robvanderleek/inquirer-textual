from inquirer_textual import prompts
from inquirer_textual.common.Shortcut import Shortcut

if __name__ == '__main__':
    answer = prompts.text('Enter your name:', shortcuts=[Shortcut('escape', 'select')])
    print(f'Your answer: {answer}')
