from __future__ import annotations

from tempfile import NamedTemporaryFile

from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.widgets.InquirerPath import InquirerPath, PathType


def test_snapshot(snap_compare):
    app = InquirerApp()
    app.widget = InquirerPath('Output directory:')

    assert snap_compare(app)


def test_snapshot_with_default_value(snap_compare):
    app = InquirerApp()
    app.widget = InquirerPath('Output directory:', exists=True, path_type=PathType.DIRECTORY, default='/var/log')

    assert snap_compare(app)


def test_validation_failure(snap_compare):
    with NamedTemporaryFile(delete=True) as tmpfile:
        widget = InquirerPath('Output directory:', path_type=PathType.DIRECTORY, exists=True)
        app = InquirerApp()
        app.widget = widget

        async def run_before(pilot) -> None:
            await pilot.press(*[c for c in tmpfile.name])
            await pilot.press("enter")

        assert snap_compare(app, run_before=run_before)
