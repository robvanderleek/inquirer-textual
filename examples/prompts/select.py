from inquirer_textual import prompts

if __name__ == '__main__':
    answer = prompts.select('Planet:', ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'])
    print(answer)
