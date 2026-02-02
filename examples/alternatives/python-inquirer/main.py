#!/usr/bin/env -S uv run --script

# /// script
# dependencies = [
#   "inquirer",
# ]
# ///

import inquirer

def editor():
    questions = [
        inquirer.Editor('{"name": "value"}', message="JSON editor")
    ]
    return inquirer.prompt(questions)

def text():
    questions = [
        inquirer.Text('name', message="What's your name")
    ]
    return inquirer.prompt(questions)

def path():
    questions = [
        inquirer.Path('log_file',
            message="Where logs should be located?",
            exists=True,
            path_type=inquirer.Path.DIRECTORY,
        )
    ]
    return inquirer.prompt(questions)

def select():
    questions = [
        inquirer.List('size',
            message="What size do you need?",
            choices=['Jumbo', 'Large', 'Standard', 'Medium', 'Small', 'Micro'],
        ),
    ]
    return inquirer.prompt(questions)

if __name__ == "__main__":
    print(select())
