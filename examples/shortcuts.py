from inquirer_textual import prompts
from inquirer_textual.common.AppConfig import AppConfig
from inquirer_textual.common.Shortcut import Shortcut

if __name__ == '__main__':
    shortcuts = [Shortcut('escape', 'select')]
    answer = prompts.text("Enter your name:", app_config=AppConfig(shortcuts=shortcuts))
    print(f'Your answer: {answer}')
