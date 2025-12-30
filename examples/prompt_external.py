from textual import on, events
from textual.app import ComposeResult
from textual.containers import HorizontalGroup, VerticalGroup
from textual.widgets import Label
from textual_slider import Slider

from inquirer_textual import prompts
from inquirer_textual.common.PromptMessage import PromptMessage
from inquirer_textual.widgets.InquirerWidget import InquirerWidget


class InquirerSlider(InquirerWidget):
    DEFAULT_CSS = """
    InquirerSlider {
        height: auto;
    }
    """

    def __init__(self, message: str):
        super().__init__()
        self.message = message
        self.slider: Slider | None = None

    def current_value(self):
        return self.slider.value if self.slider else None

    def compose(self) -> ComposeResult:
        with VerticalGroup():
            with HorizontalGroup():
                yield PromptMessage(self.message)
                yield Label(id="slider-value")
            self.slider = Slider(min=0, max=1024, step=16, id="slider")
            yield self.slider

    def on_mount(self) -> None:
        value_label = self.query_one("#slider-value", Label)
        value_label.update(str(self.slider.value))

    @on(Slider.Changed, "#slider")
    def on_slider_changed(self, event: Slider.Changed) -> None:
        value_label = self.query_one("#slider-value", Label)
        value_label.update(str(event.value))

    def on_key(self, event: events.Key):
        if event.key == 'enter':
            event.stop()
            self.submit_current_value()


if __name__ == '__main__':
    answer = prompts.external(InquirerSlider('Memory:'))
    print(answer)
