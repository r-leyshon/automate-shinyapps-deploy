from shiny import App, render, ui
from datetime import datetime

app_ui = ui.page_fluid(
    ui.h2("Testing Deploy Schedule."),
    ui.output_text("txt"),
)

def server(input, output, session):
    @output
    @render.text
    def txt():
        nw = datetime.now()
        nw = datetime.strftime(nw, "%Y-%m-%d %H:%M:%S")
        return f"Deployed at {nw}."

app = App(app_ui, server)
