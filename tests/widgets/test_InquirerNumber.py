from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.widgets.InquirerNumber import InquirerNumber


def test_snapshot(snap_compare):
    app = InquirerApp()
    app.widget = InquirerNumber('Repeat:')

    assert snap_compare(app)


async def test_named():
    widget = InquirerNumber('Repeat:', name='repeat')
    app = InquirerApp[int]()
    app.widget = widget

    async with app.run_test() as pilot:
        await pilot.press('7')
        await pilot.press("enter")
    result = app._return_value

    assert result.value == 7
    assert result.name == 'repeat'
