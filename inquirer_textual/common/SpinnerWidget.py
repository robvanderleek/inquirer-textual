from textual.widgets import Static


class SpinnerWidget(Static):
    DEFAULT_CSS = """
        SpinnerWidget {
            width: 1;
            margin-right: 1;
        }
        """

    def __init__(self, name: str | None = None):
        super().__init__(name=name)
        self.spinner_frames = [
            "⠋",
            "⠙",
            "⠹",
            "⠸",
            "⠼",
            "⠴",
            "⠦",
            "⠧",
            "⠇",
            "⠏"
        ]
        self.current_frame_index = 0

    def on_mount(self):
        self.set_interval(0.1, self.update_spinner)

    def update_spinner(self):
        self.update(self.spinner_frames[self.current_frame_index])
        self.current_frame_index = (self.current_frame_index + 1) % len(self.spinner_frames)
