from shiny import App, render, ui
# get the saved time
with open("saved_time.txt", "r") as f:
    nw = f.readlines()[0]
    f.close()

app_ui = ui.page_fluid(
    ui.h2("Testing Deploy Schedule."),
    ui.output_text("txt"),
)

def server(input, output, session):
    @output
    @render.text
    def txt():
        return f"Deployed at {nw}."

app = App(app_ui, server)
