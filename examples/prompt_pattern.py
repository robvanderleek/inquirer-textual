from inquirer_textual import prompts

if __name__ == '__main__':
    result = prompts.pattern('Select element:', ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron',
                                               'Carbon'])
    print(result)
