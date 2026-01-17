from inquirer_textual import prompts

if __name__ == "__main__":
    first_name = prompts.text('First name:')
    last_name = prompts.text('Last name:')
    print(f'Hello, {first_name} {last_name}! 👋')
