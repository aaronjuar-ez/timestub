from textual.app import App
from textual.widgets import Input
from textual.widgets import Label
from textual.widgets import Button
from textual.containers import HorizontalGroup

class timestub(App):
    def compose(self):
        yield Label("timestub ~ pay calculator")
        yield Input(placeholder="what's your hourly wage?",id="hourly_pay")
        yield Label (id="pay_label")
        with HorizontalGroup():
            yield Button("yes", id="yesss_button")
            yield Button("no", id="nooo_button")
    def on_input_submitted(self, user_pay_input):
        pay_result_label = self.query_one("#pay_label")
        pay = float (user_pay_input.value)
        pay_result_label.update("your pay is " + f"${pay:.2f}" + " correct?")
    def on_button_pressed(self, event_button_id_thing):
        if event_button_id_thing.button.id == "yesss_button":
            pay_result_label = self.query_one("#pay_label")
            pay_result_label.update("confirmed")
        elif event_button_id_thing.button.id == "nooo_button":
            self.exit()
# starts interface/cli
app = timestub()
app.run()