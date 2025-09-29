from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.widgets.InquirerMulti import InquirerMulti
from inquirer_textual.widgets.InquirerNumber import InquirerNumber
from inquirer_textual.widgets.InquirerSecret import InquirerSecret
from inquirer_textual.widgets.InquirerText import InquirerText


def test_snapshot(snap_compare):
    text_widget = InquirerText('Name:')
    password_widget = InquirerSecret('Password:')
    number_widget = InquirerNumber('Memory:')
    widget = InquirerMulti([text_widget, password_widget, number_widget])
    app = InquirerApp(widget)

    assert snap_compare(app)


def test_snapshot_second_input(snap_compare):
    text_widget = InquirerText('Name:')
    password_widget = InquirerSecret('Password:')
    number_widget = InquirerNumber('Memory:')
    widget = InquirerMulti([text_widget, password_widget, number_widget])
    app = InquirerApp(widget)

    async def run_before(pilot) -> None:
        await pilot.press('r', 'o', 'b')
        await pilot.press('enter')

    assert snap_compare(app, run_before=run_before)


def test_snapshot_third_input(snap_compare):
    text_widget = InquirerText('Name:')
    password_widget = InquirerSecret('Password:')
    number_widget = InquirerNumber('Memory:')
    widget = InquirerMulti([text_widget, password_widget, number_widget])
    app = InquirerApp(widget)

    async def run_before(pilot) -> None:
        await pilot.press('r', 'o', 'b')
        await pilot.press('enter')
        await pilot.press('s', 'e', 'c', 'r', 'e', 't')
        await pilot.press('enter')

    assert snap_compare(app, run_before=run_before)
