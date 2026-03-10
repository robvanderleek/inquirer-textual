from __future__ import annotations

from inquirer_textual.common.Candidate import Candidate
from inquirer_textual.common.Choice import Choice
from inquirer_textual.common.match_utils import fuzzy_match
from inquirer_textual.widgets.InquirerPattern import InquirerPattern


class InquirerFuzzy(InquirerPattern):
    """A select widget that allows a single selection from a list of choices with fuzzy filtering."""

    def __init__(self, message: str, choices: list[str | Choice], name: str | None = None,
                 default: str | Choice | None = None, mandatory: bool = True, height: int | str | None = None):
        """
        Args:
            message (str): The prompt message to display.
            choices (list[str | Choice]): A list of choices to present to the user.
            default (str | Choice | None): The default choice to pre-select.
            mandatory (bool): Whether a response is mandatory.
            height (int | str | None): If None, for inline apps the height will be determined based on the number of choices.
        """
        super().__init__(message, choices, name=name, default=default, mandatory=mandatory, height=height)

    def filter_candidates(self, query: str) -> list[Candidate]:
        query = query.lower()
        if query == '':
            return [Candidate(c) for c in self.choices]
        else:
            return fuzzy_match(query, self.choices)
