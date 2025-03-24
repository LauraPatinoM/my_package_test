import typer
from . import add

cli = typer.Typer()


@cli.command(name="add")
def add_wrapper(input1: float, input2: float):
    print(add(input1, input2))