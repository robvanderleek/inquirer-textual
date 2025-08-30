from inquirer_textual.prompts import select, text

if __name__ == "__main__":
    # answer = text("Enter your name:")
    # print(f'Your answer: {answer}')
    answer = select('Environment:', [l for l in
                                     ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'a', 'b', 'c', 'd',
                                      'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                                      'i', 'j', 'k', 'l', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']])
    print(f'Your answer: {answer}')
