#!/usr/bin/env -S uv run --script
#
# https://inquirerpy.readthedocs.io/

# /// script
# dependencies = [
#   "inquirerpy",
# ]
# ///

from InquirerPy import inquirer
from InquirerPy.validator import EmptyInputValidator

def confirm():
    return inquirer.confirm(message='Do you want to save this entry?').execute()

def fuzzy():
    return inquirer.fuzzy(
        message="Select element:",
        choices=["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", 
            "Carbon"],
        default="Lithium",
    ).execute()

def number():
    return inquirer.number(
        message="Enter integer:",
        min_allowed=-2,
        max_allowed=10,
        validate=EmptyInputValidator(),
    ).execute()

if __name__ == "__main__":
    print(fuzzy())
