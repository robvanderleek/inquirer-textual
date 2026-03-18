from inquirer_textual import prompts

if __name__ == '__main__':
    result = prompts.autocomplete('Planet:',
                                  candidates=['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus',
                                              'Neptune'])
    print(result)
