from inquirer_textual import prompts
from inquirer_textual.widgets.Shortcut import Shortcut

if __name__ == '__main__':
    shortcuts = [Shortcut('escape', 'select')]
    answer = prompts.select('Planet:', ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'],
                            shortcuts)
    print(f'Your answer: {answer}')
