from textual.app import App
from textual.widgets import Static

from inquirer_textual import prompts
from inquirer_textual.widgets.Shortcut import Shortcut


def example_select():
    shortcuts = [Shortcut('v', 'view')]
    answer = prompts.select('Environment:', [l for l in
                                             ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'a', 'b', 'c',
                                              'd',
                                              'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
                                              'h',
                                              'i', 'j', 'k', 'l', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                                              'l']],
                            shortcuts)
    print(f'Your answer: {answer}')


def example_text():
    shortcuts = [Shortcut('escape', 'select')]
    answer = prompts.text("Enter your name:", shortcuts)
    print(f'Your answer: {answer}')


def example_number():
    shortcuts = [Shortcut('escape', 'select')]
    answer = prompts.number(
        message="Enter integer:",
        shortcuts=shortcuts
        # min_allowed=-2,
        # max_allowed=10,
        # validate=EmptyInputValidator(),
    )
    print(f'Your answer: {answer}')


class TestApp(App):
    CSS = """
            Screen {
                border-top: none;
                border-bottom: none;
                height: 3;
            }
            """
    INLINE_PADDING = 0

    def __init__(self):
        super().__init__()

    def on_key(self, _):
        self.screen.styles.height = 0
        self.app.call_after_refresh(lambda: self.app.exit())

    def compose(self):
        yield Static("Hello world!")


if __name__ == "__main__":
    # TestApp().run(inline=True)
    example_text()
    example_select()
    example_number()
