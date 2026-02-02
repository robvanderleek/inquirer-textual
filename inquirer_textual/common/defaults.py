from textual.theme import Theme

DEFAULT_THEME = Theme(
    name="inquirer-textual-default",
    primary="#0178D4",
    secondary="#004578",
    accent="#c678dd",
    warning="#ffa62b",
    error="#e06c75",
    success="#4EBF71",
    foreground="#e0e0e0",
    background="black",
    surface="transparent",
    variables={
        'block-cursor-foreground': '#61afef',
        'block-cursor-background': 'transparent',
        'block-cursor-blurred-foreground': '#61afef',
        'block-cursor-blurred-background': 'transparent',
        'inquirer-textual-question-mark': '#e5c07b',
        'inquirer-textual-input-color': '#98c379',
    }
)

POINTER_CHARACTER = '\u276f'
