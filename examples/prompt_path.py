from inquirer_textual import prompts
from inquirer_textual.widgets.InquirerPath import PathType

if __name__ == '__main__':
    answer = prompts.path('Output directory:', exists=True, path_type=PathType.FILE)
    print(answer)
