from inquirer_textual import prompts
from inquirer_textual.common.PromptSettings import PromptSettings
from inquirer_textual.common.Shortcut import Shortcut

if __name__ == '__main__':
    content = "Hello world!\n" * 50
    shortcuts = [Shortcut('q', 'quit')]
    prompts.echo(content, settings=PromptSettings(inline=True, shortcuts=shortcuts))
