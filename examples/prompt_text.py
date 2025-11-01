from inquirer_textual import prompts

if __name__ == '__main__':
    answer = prompts.text('Name:')
    print(answer)
