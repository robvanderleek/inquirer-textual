from inquirer_textual import prompts

if __name__ == "__main__":
    name = prompts.text('Enter your name:')
    print(f'Hello, {name}! 👋')
