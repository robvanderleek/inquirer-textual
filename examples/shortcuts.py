from inquirer_textual import prompts
from inquirer_textual.common.Shortcut import Shortcut

if __name__ == '__main__':
    answer = prompts.select('Planet:', ['Mercury', 'Venus', 'Earth', 'Mars',
        'Jupiter', 'Saturn', 'Uranus', 'Neptune'], 
        shortcuts=[Shortcut('escape', 'select'), Shortcut('q', 'quit')])
    print(f'Your answer: {answer}')
