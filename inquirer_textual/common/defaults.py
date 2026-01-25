from textual.theme import Theme

DEFAULT_THEME = Theme(
    name="inquirer-textual-default",
    primary="#0178D4",
    secondary="#004578",
    accent="#ffa62b",
    warning="#ffa62b",
    error="#e06c75",
    success="#4EBF71",
    foreground="#e0e0e0",
    background="black",
    variables={
        'inquirer-textual-app-background': 'black',
        'inquirer-textual-background': 'transparent',
        'inquirer-textual-question-mark': '#e5c07b',
        'inquirer-textual-input-color': '#98c379',
        'inquirer-textual-prompt-color': '#c678dd',
        'inquirer-textual-highlight-foreground': '#61afef',
        'inquirer-textual-highlight-background': 'transparent',
    }
)

POINTER_CHARACTER = '\u276f'
