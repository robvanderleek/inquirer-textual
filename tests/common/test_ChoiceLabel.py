from textual.app import App, ComposeResult

from inquirer_textual.common.ChoiceLabel import ChoiceLabel


def test_snapshot_without_pointer(snap_compare):
    class TestApp(App):
        def compose(self) -> ComposeResult:
            yield ChoiceLabel('Hydrogen')

    app = TestApp()

    assert snap_compare(app)


def test_snapshot_with_pointer(snap_compare):
    class TestApp(App):
        def compose(self) -> ComposeResult:
            label = ChoiceLabel('Hydrogen')
            label.add_pointer()
            yield label

    app = TestApp()

    assert snap_compare(app)


def test_snapshot_with_pattern(snap_compare):
    class TestApp(App):
        def compose(self) -> ComposeResult:
            label = ChoiceLabel('Hydrogen', 'gen')
            label.add_pointer()
            yield label

    app = TestApp()

    assert snap_compare(app)
