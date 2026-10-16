from textual.app import App
from textual.widgets import Input
from textual.widgets import Label
# defines input and prompts 
class timestub(App):
    def compose(self):
        yield Label("timestub ~ pay calculator")
        yield Input(placeholder="what's your hourly wage?",id="hourly_pay")
# starts interface
app = timestub()
app.run()