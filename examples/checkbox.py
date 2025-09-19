from inquirer_textual import prompts

if __name__ == '__main__':
    answer = prompts.checkbox(message="Select planets:", choices=[
        'Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'
    ])
    print(f'Your answer: {answer}')