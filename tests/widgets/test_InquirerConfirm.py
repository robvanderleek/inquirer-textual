from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.widgets.InquirerConfirm import InquirerConfirm
from inquirer_textual.widgets.Result import Result


def test_snapshot(snap_compare):
    widget = InquirerConfirm('Are you sure?')
    app = InquirerApp(widget)

    assert snap_compare(app)


def test_snapshot_default_yes(snap_compare):
    widget = InquirerConfirm('Are you sure?', default=True)
    app = InquirerApp(widget)

    assert snap_compare(app)


def test_snapshot_custom_chars(snap_compare):
    widget = InquirerConfirm('Are you sure?', confirm_character='a', reject_character='b')
    app = InquirerApp(widget)

    assert snap_compare(app)


async def test_confirm_yes():
    widget = InquirerConfirm('Are you sure?')
    app = InquirerApp(widget)

    async with app.run_test() as pilot:
        assert widget.value is False
        await pilot.press("y")
    result: Result[bool] = app._return_value

    assert result.value


async def test_confirm_no():
    widget = InquirerConfirm('Are you sure?')
    app = InquirerApp(widget)

    async with app.run_test() as pilot:
        assert widget.value is False
        await pilot.press("n")
    result: Result[bool] = app._return_value

    assert not result.value


async def test_mandatory():
    widget = InquirerConfirm('Are you sure?', mandatory=True)
    app = InquirerApp(widget)

    async with app.run_test() as pilot:
        await pilot.press("ctrl+c")
    result: Result[Choice] = app._return_value

    assert result is None


async def test_not_mandatory():
    widget = InquirerConfirm('Are you sure?', mandatory=False)
    app = InquirerApp(widget)

    async with app.run_test() as pilot:
        await pilot.press("ctrl+c")
    result: Result[Choice] = app._return_value

    assert result.command is None
    assert result.value is None
