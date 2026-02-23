from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.common.Choice import COMMAND_SELECT
from inquirer_textual.common.InquirerResult import InquirerResult
from inquirer_textual.widgets.InquirerWaitForKey import InquirerWaitForKey


def test_snapshot(snap_compare):
    app = InquirerApp()
    app.widget = InquirerWaitForKey('Press enter to continue')

    assert snap_compare(app)


async def test_press_enter():
    app = InquirerApp()
    app.widget = InquirerWaitForKey('Press enter to continue')

    async with app.run_test() as pilot:
        await pilot.press('enter')
    result = app._return_value

    assert isinstance(result, InquirerResult)
    assert result.command == COMMAND_SELECT
    assert result.value is None


async def test_press_other_key():
    app = InquirerApp()
    app.widget = InquirerWaitForKey('Press enter to continue')

    async with app.run_test() as pilot:
        await pilot.press('y')
    result = app._return_value

    assert isinstance(result, type(None))
