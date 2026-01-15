from inquirer_textual import prompts

if __name__ == '__main__':
    result = prompts.number(message='Memory:')
    print(result)
