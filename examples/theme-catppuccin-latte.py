from inquirer_textual import prompts
from inquirer_textual.common.PromptSettings import PromptSettings

if __name__ == '__main__':
    result = prompts.select('Planet:', ['Mercury', 'Venus', 'Earth', 'Mars',
                                        'Jupiter', 'Saturn', 'Uranus', 'Neptune'],
                            settings=PromptSettings(theme='catppuccin-latte'))
    print(result)
