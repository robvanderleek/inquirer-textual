from textual.app import App
from textual.containers import Horizontal
from textual.widgets import ListItem, ListView, Static, Label

from inquirer_textual.prompts import select, text
from inquirer_textual.widgets.Shortcut import Shortcut


def test_select():
    shortcuts = [Shortcut('v', 'view', 'View')]
    answer = select('Environment:', [l for l in
                                     ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'a', 'b', 'c', 'd',
                                      'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                                      'i', 'j', 'k', 'l', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']],
                    shortcuts)
    print(f'Your answer: {answer}')


def test_text():
    answer = text("Enter your name:")
    print(f'Your answer: {answer}')


class TestApp(App):
    CSS = """
        
        #hello {
            width: 6;
        }
        Horizontal {
            height: 1;
        }
    """

    def __init__(self):
        super().__init__()

    def on_mount(self):
        self.screen.styles.height = 10

    def compose(self):
        with Horizontal():
            yield Static("Hello ", id='hello')
            yield Static("World!")
        yield ListView(
            ListItem(Label("Item 1")),
            ListItem(Label("Item 2")),
            ListItem(Label("Item 3")),
        )


if __name__ == "__main__":
    # TestApp().run(inline=True, inline_no_clear=True)
    test_select()
