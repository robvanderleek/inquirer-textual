from inquirer_textual import prompts

if __name__ == '__main__':
    answer = prompts.number(message='Memory:')
    print(answer)
