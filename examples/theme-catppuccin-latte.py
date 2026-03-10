from inquirer_textual import prompts

if __name__ == '__main__':
    result = prompts.select('Planet:', ['Mercury', 'Venus', 'Earth', 'Mars', 
        'Jupiter', 'Saturn', 'Uranus', 'Neptune'],
        settings=prompts.PromptSettings(theme='catppuccin-latte'))
    print(result)
