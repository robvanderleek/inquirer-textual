from inquirer_textual import prompts

if __name__ == '__main__':
    result = prompts.secret('Password:')
    print(result)
