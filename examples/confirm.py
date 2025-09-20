from inquirer_textual import prompts

if __name__ == '__main__':
    answer = prompts.confirm("Proceed?")
    print(f'Your answer: {answer}')
