from inquirer_textual.select import select

if __name__ == "__main__":
    answer = select('Environment:', ['production', 'staging', 'development'])
    print(f'You selected: {answer}')
