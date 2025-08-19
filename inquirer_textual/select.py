from textual.app import App, ComposeResult
from textual.widgets import ListView, Label, ListItem


class SelectApp(App[str]):
    CSS = """
    ListItem.-highlight {
        color: white;
        background: black 0%;
    }
    """

    def __init__(self, message: str, choices: list[str]):
        super().__init__()
        self.message = message
        self.choices = choices
        self.list_view: ListView | None = None
        self.selected: str | None = None

    def on_mount(self) -> None:
        self.app.styles.background = 'black 0%'
        self.screen.styles.border_top = "none"
        self.screen.styles.border_bottom = "none"
        self.screen.styles.background = 'black 0%'
        self.list_view.styles.background = 'black 0%'
        self.list_view.styles.height = len(self.choices)

    def on_list_view_selected(self, event: ListView.Selected) -> None:
        self.exit(self.choices[event.index])

    def compose(self) -> ComposeResult:
        items: list[ListItem] = []
        for choice in self.choices:
            list_item = ListItem(Label(choice))
            items.append(list_item)
        self.list_view = ListView(*items)
        yield self.list_view


def select(message: str, choices: list[str]) -> str:
    app = SelectApp(message, choices)
    return app.run(inline=True)
