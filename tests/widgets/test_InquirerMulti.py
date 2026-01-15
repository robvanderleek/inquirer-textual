from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.widgets.InquirerCheckbox import InquirerCheckbox
from inquirer_textual.widgets.InquirerConfirm import InquirerConfirm
from inquirer_textual.widgets.InquirerMulti import InquirerMulti
from inquirer_textual.widgets.InquirerNumber import InquirerNumber
from inquirer_textual.widgets.InquirerSecret import InquirerSecret
from inquirer_textual.widgets.InquirerSelect import InquirerSelect
from inquirer_textual.widgets.InquirerText import InquirerText


def test_snapshot(snap_compare):
    app = InquirerApp()
    app.widget = InquirerMulti([
        ('name', InquirerText('Name:')),
        ('password', InquirerSecret('Password:')),
        ('memory', InquirerNumber('Memory:'))
    ])

    assert snap_compare(app)


def test_snapshot_second_input(snap_compare):
    app = InquirerApp()
    app.widget = InquirerMulti([
        ('name', InquirerText('Name:')),
        ('password', InquirerSecret('Password:')),
        ('memory', InquirerNumber('Memory:'))
    ])

    async def run_before(pilot) -> None:
        await pilot.press('r', 'o', 'b')
        await pilot.press('enter')

    assert snap_compare(app, run_before=run_before)


def test_snapshot_third_input(snap_compare):
    app = InquirerApp()
    app.widget = InquirerMulti([
        ('name', InquirerText('Name:')),
        ('password', InquirerSecret('Password:')),
        ('memory', InquirerNumber('Memory:'))
    ])

    async def run_before(pilot) -> None:
        await pilot.press('r', 'o', 'b')
        await pilot.press('enter')
        await pilot.press('s', 'e', 'c', 'r', 'e', 't')
        await pilot.press('enter')

    assert snap_compare(app, run_before=run_before)


def test_snapshot_fourth_input(snap_compare):
    app = InquirerApp()
    app.widget = InquirerMulti([
        ('name', InquirerText('Name:')),
        ('password', InquirerSecret('Password:')),
        ('memory', InquirerNumber('Memory:')),
        ('proceed', InquirerConfirm('Proceed?'))
    ])

    async def run_before(pilot) -> None:
        await pilot.press('r', 'o', 'b')
        await pilot.press('enter')
        await pilot.press('s', 'e', 'c', 'r', 'e', 't')
        await pilot.press('enter')
        await pilot.press('1', '2', '3', '4', '5', '6')
        await pilot.press('enter')

    assert snap_compare(app, run_before=run_before)


def test_snapshot_fifth_input(snap_compare):
    app = InquirerApp()
    app.widget = InquirerMulti([
        ('name', InquirerText('Name:')),
        ('password', InquirerSecret('Password:')),
        ('memory', InquirerNumber('Memory:')),
        ('proceed', InquirerConfirm('Proceed?')),
        ('planet', InquirerSelect('Planet?', ['Earth', 'Mars', 'Venus'], default='Mars'))
    ])

    async def run_before(pilot) -> None:
        await pilot.press('r', 'o', 'b')
        await pilot.press('enter')
        await pilot.press('s', 'e', 'c', 'r', 'e', 't')
        await pilot.press('enter')
        await pilot.press('1', '2', '3', '4', '5', '6')
        await pilot.press('enter')
        await pilot.press('N')
        await pilot.press('enter')

    assert snap_compare(app, run_before=run_before)


def test_snapshot_fifth_input_pick_default(snap_compare):
    app = InquirerApp()
    app.widget = InquirerMulti([
        ('name', InquirerText('Name:')),
        ('password', InquirerSecret('Password:')),
        ('memory', InquirerNumber('Memory:')),
        ('proceed', InquirerConfirm('Proceed?')),
        ('planet', InquirerSelect('Planet?', ['Earth', 'Mars', 'Venus'], default='Mars')),
        ('people', InquirerCheckbox("People?", choices=['Alice', 'Bob', 'Charlie']))
    ])

    async def run_before(pilot) -> None:
        await pilot.press('r', 'o', 'b')
        await pilot.press('enter')
        await pilot.press('s', 'e', 'c', 'r', 'e', 't')
        await pilot.press('enter')
        await pilot.press('1', '2', '3', '4', '5', '6')
        await pilot.press('enter')
        await pilot.press('enter')

    assert snap_compare(app, run_before=run_before)
