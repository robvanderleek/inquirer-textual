from textual import events
from textual.app import ComposeResult
from textual.widgets import Input

from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.widgets.InquirerWidget import InquirerWidget


async def test_named():
    class ExternalWidget(InquirerWidget):
        def __init__(self, name: str | None = None):
            super().__init__(name=name)

        def current_value(self):
            return 42

        def compose(self) -> ComposeResult:
            yield Input()

        def on_key(self, event: events.Key):
            if event.key == 'enter':
                event.stop()
                self.submit_current_value()

    app = InquirerApp()
    app.widget = ExternalWidget(name='external_widget')

    async with app.run_test() as pilot:
        await pilot.press('enter')
    result = app._return_value

    assert result.value == 42
    assert result.name == 'external_widget'
