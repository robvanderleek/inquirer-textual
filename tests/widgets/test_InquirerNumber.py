from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.widgets.InquirerNumber import InquirerNumber


def test_snapshot(snap_compare):
    widget = InquirerNumber('Repeat:')
    app = InquirerApp(widget)

    assert snap_compare(app)

