from typing import Any

from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.widgets.InquirerSelect import InquirerSelect

if __name__ == '__main__':
    app: InquirerApp[dict[str, Any]] = InquirerApp(theme='solarized-light')
    app.widget = InquirerSelect('Planet:', ['Mercury', 'Venus', 'Earth', 'Mars',
        'Jupiter', 'Saturn', 'Uranus', 'Neptune'])
    answer = app.run(inline=True).value
    print(answer)
