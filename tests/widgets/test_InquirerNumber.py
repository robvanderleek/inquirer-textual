from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.widgets.InquirerNumber import InquirerNumber


def test_snapshot(snap_compare):
    app = InquirerApp()
    app.widget = InquirerNumber('Repeat:')

    assert snap_compare(app)
