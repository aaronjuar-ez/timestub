## import libraries
from textual.app import App
from textual.widgets import Input
from textual.widgets import Label
from textual.widgets import Button
## define app/class?
class timestub(App):
    # what if i was writing css but i didn't know what i was doing?
    # well that's exactly what i'm going to do
    CSS = """
    Screen { align: center top; }
    Input { width: 40; border: round; }
    #worked_hours, #future_hours { display: none; }
    """
    def compose(self):
        yield Label(r"""
▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▌
▐   _     _                            _             _       |   ▌
▐  | |_  (_)  _ __ ___     ___   ___  | |_   _   _  | |__    |   ▌
▐  | __| | | | '_ ` _ \   / _ \ / __| | __| | | | | | '_ \   |   ▌
▐  | |_  | | | | | | | | |  __/ \__ \ | |_  | |_| | | |_) |  |   ▌
▐   \__| |_| |_| |_| |_|  \___| |___/  \__|  \__,_| |_.__/   .   ▌
▐▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▌
        """)
        yield Input(placeholder="what's your hourly wage?",id="hourly_pay")
        yield Input(placeholder="hours worked?", id="worked_hours")
        yield Input(placeholder="hours scheduled in the future?", id="future_hours")
        yield Button("next ——>", id="calculate_button")
        yield Label (id="pay_label")
    def on_button_pressed(self, event_button_id_thing):
            ## the ACTUAL math (and converting strings to real numbers)
            hourly_input = self.query_one("#hourly_pay")
            worked_input = self.query_one("#worked_hours")
            # https://music.apple.com/us/album/the-most-dear-and-the-future/1832581930
            the_most_dear_and_the_future_input = self.query_one("#future_hours")
            if hourly_input.display:
                hourly_input.display = False
                worked_input.display = True
                worked_input.focus()
            elif worked_input.display:
                worked_input.display = False
                the_most_dear_and_the_future_input.display = True
                the_most_dear_and_the_future_input.focus()
            else:
                the_most_dear_and_the_future_input.display = False
                event_button_id_thing.button.display = False
                hourly_pay = float(hourly_input.value)
                worked_hours = float(worked_input.value)
                future_hours = float(the_most_dear_and_the_future_input.value)
                self.query_one("#pay_label").update(f"you made ${hourly_pay * worked_hours:.2f} already\n\nyou are predicted to make ${hourly_pay * future_hours:.2f}\n\ntotaling ${(future_hours + worked_hours) * hourly_pay:.2f}!")
# starts interface/cli
app = timestub()
app.run()