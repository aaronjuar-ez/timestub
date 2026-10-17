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
            ## the ACTUAL math (and converting strings to real numbers)
            pay_result_label = self.query_one("#pay_label")
            hourly_pay = float(self.query_one("#hourly_pay").value)
            worked_hours = float(self.query_one("#worked_hours").value)
            future_hours = float(self.query_one("#future_hours").value)
            pay_result_label.update(f"so far you made ${(worked_hours * hourly_pay):.2f}\nand you're projected to make ${(future_hours * hourly_pay):.2f} by the end of the current pay period\ntotaling a paycheck of ${((worked_hours + future_hours) * hourly_pay):.2f}")
# starts interface/cli
app = timestub()
app.run()