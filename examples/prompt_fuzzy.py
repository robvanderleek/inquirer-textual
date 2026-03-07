from inquirer_textual import prompts

if __name__ == '__main__':
    result = prompts.fuzzy('Select element:', ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron',
                                               'Carbon'])
    print(result)
