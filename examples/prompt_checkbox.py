from inquirer_textual import prompts

if __name__ == '__main__':
    answer = prompts.checkbox("Planets:", choices=[
        'Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 
        'Uranus', 'Neptune'
    ])
    print(answer)
