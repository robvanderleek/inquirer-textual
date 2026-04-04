from inquirer_textual import prompts

if __name__ == '__main__':
    result = prompts.autocomplete('Planet:',
                                  completions=['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus',
                                               'Neptune'])
    print(result)
