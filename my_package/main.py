import typer
from commands import init

app = typer.Typer()

app.command(name="init")(init.run)
# init - import name
# run - function to run

def main():
    app()
