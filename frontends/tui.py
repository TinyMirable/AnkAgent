from textual.app import App,ComposeResult
from textual.containers import HorizontalGroup,VerticalScroll

from textual.widgets import Header, Footer,Button,Digits


class TimeDisplay(Digits):
    """A widget to display elapsed time."""

class Stopwatch(HorizontalGroup):
    """A stopwatch widget"""
    def on_button_pressed(self,event: Button.Pressed) -> None:
        """Event handler when a butto is pressed"""
        if event.button.id == "start":
            self.add_class("started")
        elif event.button.id == "stop":
            self.remove_class("started")
    def compose(self) -> ComposeResult:
        yield Button("Start",id="start",variant="success")
        yield Button("Stop",id="stop",variant="error")
        yield Button("Reset",id="reset")
        yield TimeDisplay("00:00:00.00")


class StopwatchApp(App):
    """A Textual app to manage stopwatches"""
    BINDINGS = [("d","toggle_dark","Toggle dark mode")]
    CSS_PATH = "css/tui.tcss"
    def compose(self)-> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()
        yield VerticalScroll(Stopwatch(),Stopwatch(),Stopwatch())

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode"""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-dark"
        )

if __name__ == "__main__":
    app = StopwatchApp()
    app.run()