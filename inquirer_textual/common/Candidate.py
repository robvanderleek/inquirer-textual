from dataclasses import dataclass

from inquirer_textual.common.Choice import Choice


@dataclass
class Candidate:
    choice: Choice | str
    match_indices: list[int] | None = None
