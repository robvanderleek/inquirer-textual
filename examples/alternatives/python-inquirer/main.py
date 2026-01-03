#!/usr/bin/env -S uv run --script

# /// script
# dependencies = [
#   "inquirer",
# ]
# ///

import re

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

if __name__ == "__main__":
    print(text())
