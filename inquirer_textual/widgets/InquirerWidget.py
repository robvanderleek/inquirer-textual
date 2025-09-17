from textual.widget import Widget


class InquirerWidget(Widget):

    def current_value(self):
        raise NotImplementedError("Subclasses must implement current_value method")
