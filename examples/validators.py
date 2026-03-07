from inquirer_textual import prompts
from inquirer_textual.common.PromptSettings import PromptSettings
from inquirer_textual.validators.NotEmptyValidator import NotEmptyValidator
from inquirer_textual.validators.UniqueValidator import UniqueValidator

if __name__ == '__main__':
    answer = prompts.text('Name:', validators=[NotEmptyValidator(), UniqueValidator(['Alice', 'Bob'])],
                          settings=PromptSettings(mandatory=True))
    print(answer)
