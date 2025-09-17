from inquirer_textual import prompts
from inquirer_textual.widgets.Shortcut import Shortcut

if __name__ == '__main__':
    shortcuts = [Shortcut('escape', 'select')]
    answer = prompts.number(
        message="Enter integer:",
        shortcuts=shortcuts
    )
    print(f'Your answer: {answer}')
