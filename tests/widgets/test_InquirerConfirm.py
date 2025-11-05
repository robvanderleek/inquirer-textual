from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.common.Result import Result
from inquirer_textual.widgets.InquirerConfirm import InquirerConfirm


def test_snapshot(snap_compare):
    app = InquirerApp()
    app.widget = InquirerConfirm('Are you sure?')

    assert snap_compare(app)


def test_snapshot_default_yes(snap_compare):
    app = InquirerApp()
    app.widget = InquirerConfirm('Are you sure?', default=True)

    assert snap_compare(app)


def test_snapshot_custom_chars(snap_compare):
    app = InquirerApp()
    app.widget = InquirerConfirm('Are you sure?', confirm_character='a', reject_character='b')

    assert snap_compare(app)


async def test_confirm_yes():
    app = InquirerApp()
    app.widget = InquirerConfirm('Are you sure?')

    async with app.run_test() as pilot:
        await pilot.press("y")
    result: Result[bool] = app._return_value

    assert result.value


async def test_confirm_no():
    app = InquirerApp()
    app.widget = InquirerConfirm('Are you sure?')

    async with app.run_test() as pilot:
        await pilot.press("n")
    result: Result[bool] = app._return_value

    assert not result.value


async def test_mandatory():
    app = InquirerApp()
    app.widget = InquirerConfirm('Are you sure?', mandatory=True)

    async with app.run_test() as pilot:
        await pilot.press("ctrl+c")
    result: Result[bool] = app._return_value

    assert result is None


async def test_not_mandatory():
    app = InquirerApp()
    app.widget = InquirerConfirm('Are you sure?', mandatory=False)

    async with app.run_test() as pilot:
        await pilot.press("ctrl+c")
    result: Result[bool] = app._return_value

    assert result.command is None
    assert result.value is None
