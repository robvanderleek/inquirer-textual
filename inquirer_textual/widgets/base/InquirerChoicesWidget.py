from __future__ import annotations

from inquirer_textual.common.Choice import Choice
from inquirer_textual.widgets.base.InquirerWidget import InquirerWidget


class InquirerChoicesWidget(InquirerWidget):
    """Base class for list-based widgets like InquirerSelect and InquirerCheckbox."""

    def __init__(self, choices: list[str | Choice], name: str | None = None, mandatory: bool = False,
                 height: int | str | None = None):
        """
            Args:
                choices (list[str | Choice]): A list of choices to present to the user.
                name (str | None): The name of the input field.
                mandatory (bool): Whether at least one selection is mandatory.
                height (int | str | None): If None, for inline apps the height will be determined based on the number
                of choices.
        """
        super().__init__(name=name, mandatory=mandatory)
        self._choices = choices
        self.height = height

    def on_mount(self):
        super().on_mount()
        if self.height is not None:
            if self.height == 'auto':
                self.styles.min_height = 10
            self.styles.height = self.height
        elif self.app.is_inline:
            self.styles.height = min(10, len(self._choices) + 1)
        else:
            self.styles.height = '1fr'
