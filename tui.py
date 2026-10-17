# import libraries
from textual.app import App
from textual.widgets import Input
from textual.widgets import Label
from textual.widgets import Button
# define app/class?
class timestub(App):
    def compose(self):
        yield Label("timestub ~ pay calculator")
        yield Input(placeholder="what's your hourly wage?",id="hourly_pay")
        yield Input(placeholder="hours worked?", id="worked_hours")
        yield Input(placeholder="hours scheduled in the future?", id="future_hours")
        yield Button("calculate", id="calculate_button")
        yield Label (id="pay_label")
    def on_button_pressed(self, event_button_id_thing):
        if event_button_id_thing.button.id == "calculate_button":
            pay_result_label = self.query_one("#pay_label")
            pay_result_label.update("confirmed")
            hourly_pay = self.query_one("#hourly_pay").value
# starts interface/cli
app = timestub()
app.run()