from inquirer_textual import prompts

if __name__ == '__main__':
    answer = prompts.fuzzy('Select element:', ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron',
                                               'Carbon'])
    print(answer)
