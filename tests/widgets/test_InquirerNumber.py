from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.common.InquirerContext import InquirerContext
from inquirer_textual.widgets.InquirerNumber import InquirerNumber


def test_snapshot(snap_compare):
    widget = InquirerNumber('Repeat:')
    context = InquirerContext(widget)
    app = InquirerApp(context)

    assert snap_compare(app)
